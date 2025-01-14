"""Classes related to enzymes:
 - Enzyme: Constraints relating enzymes to reactions. Including upper and lower bound enzyme constraints
 - EnzymeVariable: Variable related to an enzyme. The value of this variable represent the concentration.
"""
import cobra.core
import sys
import cobra
from cobra import Reaction
from cobra.exceptions import OptimizationError
from cobra.util.solver import check_solver_status
import sys

import optlang
from optlang.symbolics import Zero

sys.path.append('../../../')
from PAMpy.CatalyticEvent import CatalyticEvent
from typing import Dict, Union, Optional
from cobra import DictList
from warnings import warn



class Enzyme():
    """Upper level Enzyme object containing information about the enzyme
    and link to the EnzymeVariables for each reaction the
    enzyme catalyzes.
    This class is used to generate enzyme instances from kcat values and contains
    information about the forward as well as the backward catalysis.

    The enzyme is linked to individual cobra.Reaction variables with CatalyticEvent objects.

    There are two scenarios:
    - Promiscuous enzymes: a single enzyme can catalyze multiple reactions
    - Other: a single enzyme catalyzes a single reaction

    Parameters
    -------
    id : str
        Identifier for the enzyme (e.g. Uniprot ID)
    rxn2kcat: Dict
        Dictionary with reaction ID, kcat value pairs for the forward (f)
        and backward (b) reaction
        (Example: {'PGI': {'f': 30, 'b': 0.1}})
    upper_bound: float
        Upper bound for the enzyme variable (default 1000.0)
    lower_bound: float
        Lower bound for the enzyme variable (default 0)
    name: str
        Name of the enzyme (default None)
    molmass: float
        Molar mass of the enzyme (default 3.947778784340140e04)
    """

    
    # constant parameters
    DEFAULT_ENZYME_MOL_MASS = 3.947778784340140e04  # mean enzymes mass E.coli [g/mol]
    
    def __init__(
        self,
        id: str,
        rxn2kcat: Dict,
        upper_bound: Union[int, float] = 1000.0,
        lower_bound: Union[int, float] = 0,
        name: Optional[str] = None,
        molmass: Union[int, float] = DEFAULT_ENZYME_MOL_MASS,
    ):

        self.rxn2kcat = rxn2kcat
        self.molmass = molmass
        self.id = id # use e.g. Uniprot ID
        self.name = name
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound

        #create enzyme variable associated with theis enzyme
        self.enzyme_variable = None
        self.create_enzyme_variable()

        self.catalytic_event_id = 'CE_' + '{0}' # generic template for the catalytic events IDs
        # initialize CatalyticEvent interfaces for each associated reaction (promiscuity)
        self.catalytic_events = DictList()
        for rxn_id, kcats in rxn2kcat.items():
            self.create_catalytic_event(rxn_id, kcats)

        self._constraints = {} # dict with constraint_id:optlang.Constraint, key:value pairs.
        self._model = None
        self.enzyme_complex = [] #is the enzyme in a complex?
        self.annotation = {'type':'Constraint'}#you can add an annotation for an enzyme
     
    @property
    def kcat_values(self):
        """returns a dictionary with kcat values for each associated reaction
        """
        return self.get_kcat_values()

    @property
    def concentration(self, units:str = 'mmol/gDW', return_units:bool = False) -> float:
        """returns the enzyme's total concentration
        Any associated reaction is considered

        Parameters
        -------
        units: optional, string
            units in which the concentration is calculated (default is mmol/gDW), other option is 'g/gDW'
        return_units: optional, bool
            determines wheter the units should be returned as well

        Returns
        -------
        float
            Enzyme concentration
        """

        # sum up concentrations (aka fluxes) of all enzyme objects
        concentration = 0.0
        for catalytic_event in self.catalytic_events:
            concentration += catalytic_event.flux()
        if units == 'g/gDW':
            #converting mmol to grams of protein:
            # [g] = [mmol]* 1e-3 [mol/mmol] * MW[g/mol]
            concentration = concentration * 1e-3 * self.molmass
        if return_units:
            return concentration, units
        return concentration

    def create_constraint(self, extension: str = None):
        if extension is None: extension = ''
        else: extension = '_' + extension
        # return cobra.core.Metabolite(id = f'EC_{self.id}{extension}', compartment='Enzymes')
        return optlang.Constraint(Zero, name= f'EC_{self.id}{extension}', lb=0, ub=0)

    def add_catalytic_event(self, ce: CatalyticEvent, kcats: Dict):
        """
        Adding catalytic event associated to a reaction to an enzyme
        Parameters
        ----------
        ce: PAModelpy.Variables.CatalyticEvent
            The catalytic event object to which the enzyme should be added
        kcats: dict
            A list with dicts containing direction, kcat key value pairs
        Returns
        -------

        """
        self.catalytic_events += [ce]
        self.enzyme_variable.add_catalytic_events([ce],[kcats])

    def create_catalytic_event(self, rxn_id: str, kcats: Dict):
        """creates enzyme variables that link to reactions

        Parameters
        ----------
        rxn_id : str
            ID of the associated reaction in the model
        kcats : Dict
            kcat values for the forward and backward reaction
        Returns
        -------
        Variables.CatalyticEvent
            Enzyme variable object
        """
        
        # create unique enzyme object name and id
        catalytic_event_id = self.catalytic_event_id.format(rxn_id)
        if self.name is not None:
            enzyme_object_name = rxn_id + '_' + self.name 
        else:
            enzyme_object_name = rxn_id + '_'  + self.id
        
        # create enzymatic reaction object inherited from cobra.Reaction
        catalytic_event= CatalyticEvent(
            id=catalytic_event_id,
            rxn_id=rxn_id,
            kcats2enzymes={self: kcats},
            name=enzyme_object_name
        )

        self.add_catalytic_event(catalytic_event, kcats)

    def create_enzyme_variable(self):
        """creates enzyme variables that link  enzyme to reactions
        """
        # create enzymatic reaction object inherited from cobra.Reaction
        enzyme_variable = EnzymeVariable(
            id=self.id,
            kcats2rxns=self.rxn2kcat,
            upper_bound=self.upper_bound,
        )

        self.enzyme_variable = enzyme_variable

    def change_kcat_values(self, rxn2kcat: Dict):
        """changes the kcat values for the enzyme
        and updates the enzyme variable (enzymatic reaction) accordingly

        Parameters
        ----------
        rxn2kcat : Dict
            Dictionary with reaction ID, kcat value pairs for the forward (f)
            and backward (b) reaction
            (Example: {'PGI': {'f': 30, 'b': 0.1}})
        """

        # update the enzyme variables
        for rxn_id, kcats in rxn2kcat.items():
            catalytic_event_id = self.catalytic_event_id.format(rxn_id)
            # is there already a link between enzyme and reaction?
            if catalytic_event_id not in self.catalytic_events:
                warn(f'Reaction {rxn_id} is not associated with enzyme {self.id}. Skip')
            else:
                # change kcat values of existing enzyme variable
                self.catalytic_events.get_by_id(catalytic_event_id).change_kcat_values({self.id: kcats})


    def get_kcat_values(self, rxn_ids: Union[str, list] = None) -> Dict:
        """returns the kcat values for a specific enzyme and all
        enzyme-associated reactions

        Parameters
        ----------
        rxn_ids : str or list
            ID of the reactions for which the kcat values should be returned

        Returns
        -------
        Dict
            kcat values for the forward and backward reaction
        """
        
        if isinstance(rxn_ids, str):
            rxn_ids = [rxn_ids]
         
        rxn2kcat = {}   
        if rxn_ids is None:
            # return all kcat values
            rxn2kcat = self.rxn2kcat
        else:
            # return reaction specific kcat values
            for rxn_id in rxn_ids:
                catalytic_event_id = self.catalytic_event_id.format(rxn_id)
                if catalytic_event_id not in self.catalytic_events:
                    warn('No reaction {0} found'.format(rxn_id))
                else:
                    # get kcat values
                    rxn2kcat[rxn_id] = self.rxn2kcat[rxn_id]
                    
        return rxn2kcat

    def remove_catalytic_event(self, catalytic_event: Union[CatalyticEvent, str]):
        """
        Function to remove a catalytic event from an enzyme
        Parameters
        ----------
        catalytic_event: CatalyticEvent or str
            catalytic event or identifier to remove
        """
        if isinstance(catalytic_event, str):
            try:
                catalytic_event = self.catalytic_events.get_by_id(catalytic_event)
            except:
                print(f'Catalytic event {catalytic_event} is not related to this enzyme and can thus not be removed!')

        #remove the event from the DictList
        self.catalytic_events.remove(catalytic_event)

        
class EnzymeComplex(Enzyme):
    """Upper level EnzymeComplex object containing information about the enzymes in a complex
       and link to the enzyme variables (CatalyticEvents) for each reaction the
       enzyme complex catalyzes.
       This class is used to generate enzyme instances from kcat values and contains
       information about the forward as well as the backward catalysis.

       There are two scenarios:
       - Promiscuous enzymes: a single enzyme complex can catalyze multiple reactions
       - Other: a single enzyme complex catalyzes a single reaction

       Parameters
       -------
       id : str
           Identifier for the enzyme complex (e.g. Uniprot ID)
       enzymes: DictList of cobra.core.Enzyme
            Enzyme objects associated with the enzyme complex
       rxn2kcat: Dict
           Dictionary with reaction ID, kcat value pairs for the forward (f)
           and backward (b) reaction
           (Example: {'PGI': {'f': 30, 'b': 0.1}})
       upper_bound: float
           Upper bound for the enzyme variable (default 1000.0)
       name: str
           Name of the enzyme (default None)
       molmass: float
           Molar mass of the enzyme (default 3.947778784340140e04)

       """

    # constant parameters
    DEFAULT_ENZYME_MOL_MASS = 3.947778784340140e04  # mean enzymes mass E.coli [g/mol]

    def __init__(
            self,
            id: str,
            enzymes: DictList,
            rxn2kcat: Dict,
            upper_bound: Union[int, float] = 1000.0,
            name: Optional[str] = None,
            molmass: Union[int, float] = DEFAULT_ENZYME_MOL_MASS,
    ):
        super().__init__(
            id = id,
            rxn2kcat=rxn2kcat,
            upper_bound = upper_bound,
            name=name,
            molmass=molmass
        )

        self.enzymes = None
        self.add_enzymes(enzymes)

    def add_enzymes(self, enzymes: DictList):
        for enzyme in enzymes:
            self.enzymes.append(enzyme)
            enzyme.enzyme_complex.append(self.id)
            self.molmass += enzyme.molmass


class EnzymeVariable(Reaction):
    """
           EnzymeVariable is a class for holding information regarding the
           variable representing an enzyme in the model. For each reaction, the enzyme variables are
           summarized in a CatalyticEvent
           There are three different scenarios:
           - Enzyme complex: multiple enzymes together are associated with an EnzymeComplex object
           - isozymes: multiple enzymes independently associated with a single catalytic event
           - Other: a single enzyme is associated with a single catalytic event

           Parameters
           ----------
           kcats2rxns: Dict
               A Dict with reaction_id, kcat key, value pairs to connect the
               enzyme with the associated reaction the kcat is another dict with 'f' and 'b'
               for the forward and backward reactions respectively.
           id : str, optional
               The identifier to associate with this enzyme (default None)
           name : str, optional
               A human-readable name for the reaction (default "").
           subsystem : str, optional
               Subsystem where the reaction is meant to occur (default "").
           lower_bound : float
               The lower flux bound (default 0.0).
           upper_bound : float, optional
               The upper flux bound (default None).
           **kwargs:
               Further keyword arguments are passed on to the parent class.
           """
    DEFAULT_ENZYME_MOL_MASS = 3.947778784340140e04  # mean enzymes mass E.coli [g/mol]

    def __init__(
            self,
            kcats2rxns: Dict,
            molmass: Union[int, float] = DEFAULT_ENZYME_MOL_MASS,
            id: Optional[str] = None,  # ID of enzymatic reaction,
            name: str = "",
            upper_bound: Optional[float] = None,
            **kwargs
    ):
        super().__init__(
            id=id,
            name=name,
            subsystem='Enzymes',
            lower_bound=-upper_bound,
            upper_bound=upper_bound,
            **kwargs
        )
        self.kcats = kcats2rxns
        self.molmass = molmass
        self.rxn_ids = [rxn for rxn in kcats2rxns.keys()]
        self.enzyme = None #store the enzyme associated to the enzyme variable
        self.catalytic_events = DictList() #store the interfaces to reactions related to this enzyme
        self.reactions = DictList()
        self.constraints = {}  # store IDs of constraint the enzyme is associated with
        self._model = None
        self.annotation = {'type': 'Variable'}
        self.variables = dict()

    @property
    def kcat_values(self):
        """returns a dictionary with kcat values and reactions
        """
        return self.kcats

    @property
    def flux(self) -> float:
        """
        Get the flux value in the most recent solution.
        Flux is the primal value of the corresponding variable in the model.
        Returns
        -------
        flux: float
            Flux is the primal value of the corresponding variable in the model.
        Warnings
        --------
        * Accessing reaction fluxes through a `Solution` object is the safer,
          preferred, and only guaranteed to be correct way. You can see how to
          do so easily in the examples.
        * Reaction flux is retrieved from the currently defined
          `self._model.solver`. The solver status is checked but there are no
          guarantees that the current solver state is the one you are looking
          for.
        * If you modify the underlying model after an optimization, you will
          retrieve the old optimization values.
        Raises
        ------
        RuntimeError
            If the underlying model was never optimized beforehand or the
            reaction is not part of a model.
        OptimizationError
            If the solver status is anything other than 'optimal'.
        AssertionError
            If the flux value is not within the bounds.
        Examples
        --------
        >>> from cobra.io import load_model
        >>> model = load_model("textbook")
        >>> solution = model.optimize()
        >>> model.variables.PFK.flux
        7.477381962160283
        >>> solution.fluxes.PFK
        7.4773819621602833
        """
        try:
            check_solver_status(self._model.solver.status)
            return self.forward_variable.primal + self.reverse_variable.primal
        except AttributeError:
            raise RuntimeError(f"reaction '{self.id}' is not part of a model")
        # Due to below all-catch, which sucks, need to reraise these.
        except (RuntimeError, OptimizationError) as err:
            raise err
        # Would love to catch CplexSolverError and GurobiError here.
        except Exception as err:
            raise OptimizationError(
                f"Likely no solution exists. Original solver message: {str(err)}."
            ) from err

    @property
    def concentration(self) -> float:
        """
        Get the enzyme concentration value of the most recent solution.
        The enzyme concentration equals the flux value

        Returns
        -------
        float
            enzyme concentration [mmol/gDW]
        """
        return self.flux

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model
        # setting up the relations to the model
        # add enzyme instance
        enzyme_ids = [enz.id for enz in self._model.enzymes]
        if self.id not in enzyme_ids:
            enzyme = Enzyme(id =self.id,
                            rxn2kcat = self.kcat,
                            molmass=self.molmass
                            )
            self._model.add_enzymes([enzyme])
        self.enzyme = self._model.enzymes.get_by_id(self.id)
        self.constraints = self.enzyme._constraints
        self._model.enzyme_variables.append(self)

        # create new forward and reverse variables
        forward_variable = self._model.problem.Variable(name=self.id, ub=self.upper_bound, lb=0)
        reverse_variable = self._model.problem.Variable(name=self.reverse_id, ub=-self.lower_bound, lb=0)
        self.variables = {'forward_variable': forward_variable, 'reverse_variable': reverse_variable}
        self._model.add_cons_vars([forward_variable, reverse_variable])


        # add catalytic event and reaction instances
        for rxn_id in self.rxn_ids:
            if not rxn_id in self._model.reactions:
                # create new reaction and add to model
                rxn = cobra.Reaction(id=rxn_id)
                self._model.add_reactions([rxn])
            if not rxn_id in self.reactions:
                self.reactions.append(self._model.reactions.get_by_id(rxn_id))
            #create a catalytic event if it doesn't exist already
            if not f'CE_{rxn_id}' in self._model.catalytic_events:
                kcats2enzymes = {self.enzyme: self.kcats[rxn_id]}
                ce = CatalyticEvent(id = f'CE_{rxn_id}',
                                    kcats2enzymes=kcats2enzymes,
                                    rxn_id=rxn_id)
                ce.model = model
                self._model.catalytic_events.append(ce)
            # if catalytic event exist, add the enzyme to it
            else:
                self._model.catalytic_events.get_by_id(f'CE_{rxn_id}').add_enzymes({self.enzyme: self.kcats[rxn_id]})
            # if catalytic event is not related to the enzyme variable yet, add it.
            if f'CE_{rxn_id}' not in self.catalytic_events:
                self.catalytic_events.append(self._model.catalytic_events.get_by_id(f'CE_{rxn_id}'))

    @property
    def forward_variable(self):
        if self._model is not None:
            return self._model.variables[self.id]
        else:
            return self.variables['forward_variable']

    @property
    def reverse_variable(self):
        if self._model is not None:
            return self._model.variables[self.reverse_id]
        else:
            return self.variables['reverse_variable']

    def add_catalytic_events(self, catalytic_events:list, kcats:list):
        """
        Adding a catalytic event to an enzyme variable

        Parameters
        ----------
        catalytic_events: list
            Catalytic events to add
        kcats:list
            A list with dicts containing direction, kcat key value pairs
        """

        for i, ce in enumerate(catalytic_events):
            if ce in self.catalytic_events:
                warn(f'Catalytic event {ce.id} is already associated with enzyme variable {self.id}. '
                     f'Continue with other catalytic events')
            else:
                if not ce.enzyme_variables.has_id(self.id):
                    ce.enzyme_variables.append(self)
                self.catalytic_events.append(ce)
            if not self.reactions.has_id(ce.rxn_id):
                self.add_reactions({ce.rxn_id: kcats[i]})

    def add_reactions(self, reaction_kcat_dict: dict):
        """
        Add reactions to the enzyme variable and create bindings to the related model.
        If there are multiple reactions related to a single enzyme, this is an isozyme.

        Parameters
        ----------
        reaction_kcat_dict: nested dict
            A Dict with the reaction_id, kcat key, value pairs to connect the
            enzyme with the associated reaction the kcat is another dict with 'f' and 'b'
            for the forward and backward reactions respectively.


        """
        for reaction, kcat in reaction_kcat_dict.items():
            # check if the enzyme is already associated to the catalytic event
            try:
                self.reactions.get_by_id(reaction.id)
                warn(
                    f'Reaction {reaction.id} is already associated with the enzyme {self.id}. The enzyme variable will be updated')
                self.change_kcat_values(kcat)
                return
            except:
                pass

            self.kcats[reaction] = kcat

            if self._model is None:
                continue

            # check if enzyme is in the model
            try:
                self._model.reactions.get_by_id(reaction)
            # if not: add the enzyme to the model
            except:
                rxn = Reaction(id = reaction)
                self._model.add_reactions([rxn])

            rxn = self._model.reactions.get_by_id(reaction)
            self.reactions.append(rxn)

            for direction in kcat.keys():
                if direction != 'f' and direction != 'b':
                    warn(f'Invalid direction {direction} for kcat value for enzyme variable {self.id}! Skip!')
                    continue

            # add enzyme to catalytic event and the related variable
            for direction, kcatvalue in kcat.items():
                coeff = kcatvalue * 3600 * 1e-6
                # add enzyme to the associated reaction with kinetic constants
                # and relate enzyme to the catalytic event
                if direction == 'f':
                    self.constraints[f'EC_{self.id}_{direction}'].set_linear_coefficients({
                        rxn.forward_variable: 1 / coeff,
                        self.forward_variable: -1
                    })

                elif direction == 'b':
                    self.constraints[f'EC_{self.id}_{direction}'].set_linear_coefficients({
                        rxn.reverse_variable: 1 / coeff,
                        self.reverse_variable: -1
                    })

    def remove_catalytic_event(self, catalytic_event: Union[CatalyticEvent, str]):
        """
        Function to remove a catalytic event from an enzyme
        Parameters
        ----------
        catalytic_event: CatalyticEvent or str
            catalytic event or identifier to remove
        """
        if isinstance(catalytic_event, str):
            try:
                catalytic_event = self.catalytic_events.get_by_id(catalytic_event)
            except:
                print(f'Catalytic event {catalytic_event} is not related to this enzyme and can thus not be removed!')

        #remove the event from the DictList
        self.catalytic_events.remove(catalytic_event.id)

    def remove_reactions(self, reaction_list: list):
        """
        Remove reaction from the enzyme variable and remove the reaction from the
        constraint expressions related to the enzyme

        Parameters
        ----------
        reaction_list: list
            A list with Cbra.Reaction objects which should be removed. If a list of identifiers (str)
            is provided, the corresponding enzyme will be obtained from the EnzymeVariables.reaction attribute
        """
        # check the input
        if not hasattr(reaction_list, "__iter__"):
            enzyme_list = [reaction_list]
        if len(reaction_list) == 0:
            return None

        # check whether the input is an PAModelpy.Package.Enzyme or string and find the corresponding enzyme if needed
        for i, rxn in enumerate(reaction_list):
            if isinstance(rxn, str):
                try:
                    reaction_list[i] = self.reactions.get_by_id(rxn)
                except:
                    print(
                        f'Reaction {rxn} is not associated with the enzyme variable {self.id}. This reaction cannot be removed. \n')
                    pass

        for rxn in reaction_list:
            # remove from kcat dict
            del self.kcats[rxn.id]
            # remove from reactions dictlist
            self.reaction.remove(rxn)
            # set coefficient in constraint to 0
            for constraint in self.enzyme._constraints.values():
                self.constraints[constraint.name] = constraint
                coeff = 0
                # set coefficients to 0
                if constraint.name[-1] == 'f':
                    constraint.set_linear_coefficients({
                        rxn.forward_variable: coeff,
                        self.forward_variable: 0
                    })

                elif constraint.name[-1] == 'b':
                    constraint.set_linear_coefficients({
                        rxn.reverse_variable: coeff,
                        self.reverse_variable: 0
                    })
                # remove constraint from list of r=constraints
                del self.constraints[constraint.name]

    def change_kcat_values(self, reaction_kcat_dict: dict):
        """changes kcat values for the enzyme variable
        Parameters
        ----------
        reaction_kcat_dict: nested Dict
            A Dict with Cobra.Reaction, kcat key, value pairs to connect the
            enzyme with the associated reaction the kcat is another dict with 'f' and 'b'
            for the forward and backward reactions respectively.

        """
        # apply changes to internal dicts (one by one to avoid deleting kcat values)
        kcats_change = {}
        for rxn, kcat_dict in reaction_kcat_dict.items():
            # save change in dict
            self.kcats[rxn.id] = kcat_dict
            for direction, kcat in kcat_dict.items():
                if direction != 'f' and direction != 'b':
                    warn(f'Invalid direction {direction} for kcat value for enzyme variable {self.id}! Skip!')
                    continue

                kcats_change[direction] = kcat

            # is enzyme variable already integrated into a model
            if self._model is None:
                warn(f'Catalytic event {self.id} is not integrated into a model!')

            for direction, kcat in kcats_change.items():
                # get constraint
                constraint_id = f'EC_{rxn.id}_{direction}'
                constraint = self.enzyme._constraints[constraint_id]
                # change kcat value in the constraint
                coeff = kcat * 3600 * 1e-6
                if direction == 'f':
                    constraint.set_linear_coefficients({
                        self.reaction.forward_variable: 1 / coeff
                    })
                elif direction == 'b':
                    constraint.set_linear_coefficients({
                        self.reaction.reverse_variable: 1 / coeff
                    })
            self._model.solver.update()
