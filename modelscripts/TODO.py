# coding=utf-8

#================================================================
#   General
#================================================================

# TODO:9 check modelc interface
#   -> Check current state
#   -> old comment:
#       currently the modelc interpreter support only general
#       options independent from models.
#       The scenario printer configuration has model option
#       but they are not used since modelc interpeter does not create
#       a ScenarioPrinterConfiguration.
#       It is necessary to find a way to change this to support
#       model specific option. Currently the SecenarioPrinter
#       add some attributs on the fly. This should be removed.

# TODO:9 bracket syntax error
#   ??? on a postit
#   bracket.py might raise an exception not caught by parser

# TODO:6 create coloring scheme for GEdit

# TODO:5 only one class model
#   Having more than glossary/class model do not make too much
#   sense. This imply strange configuration where a model is used
#   in one place and another in the same import graph.
#   This could be added in the megamodel infrastructure.
#   This should apply for 'cl', 'gl', 'us', 'pe',
#   everything apart from 'ob', 'sc'

# TODO:2 fix strange printing for models


#================================================================
#   Class model
#================================================================


# TODO:7 add inheritance of oppositeRoles

# TODO:6 add inheritance of played roles

# TODO:6 add / test link object
#   ??? on a postit "link object copy"
#   -> check syntax in class model
#   -> check syntax in story model
#   -> check current implementation
#   the resolution order should be
#   object > link object > link
#   but this could fail if link object depends on link object
#   Not a priority a priori

# TODO:4 OCL: ocl bracket
#   Currenly the ocl expression for invariants must
#   follow the regular nested indentation.
#   This is not convenient. One good option would be
#   to make some kind of preprocessing in the module brackets.py
#   to allow any string between line 'ocl' and a dedent line.



# TODO:4 add composition
#   -> schema: constraint [0..1,1]
#   -> state : no cycle in object  (statechecker.py)

# TODO:4 add check for 'abstract' classes

# TODO: add support for diagram generation (-d ?)

# TODO:3 add stereotype/tags to classes

# TODO:3 add stereotype/tags to associations

# TODO:???  on post it 'inv resolve -> variant str ???'

# TODO:2 datatype Date < String
#   This mostly impact story with value conformity


#================================================================
#   Scenarios/object model
#================================================================

# TODO:4 add a check for "context/fragment" unused

# TODO:2 add OCL assert support in scenario
#        add name in metamodel and output
#        assert inv a: False
#        assert inv b: Failure
#        assert inv b
#        assert 2+3=5
#        assert b : 2+6=3

# TODO:3 deal with link deletion
#   This case should be rather easy to implement as there
#   is *a priori* nothing to check.
#   It should be possible to remove the
#   link from the current state. This is due to the fact that
#   the whole story infrastructure has been designed for this.

# TODO:2 deal with (link) object deletion
#   Like link deletion (see to do) but a bit more complicated
#   since we need to check that there is no link around
#   (option around).
#   (2) A bit more complicated that for

#================================================================
#   Object model
#================================================================

# TODO:5 avoid duplicate object state model
#   At some point objects models seem to have two analysis
#   most probably for the last frozenState generated by the
#   story evaluation and another one from the object model.
#   Check in the trace if still the case.

# TODO:5 remove useless location for checks in error messages
#   For instance
#       ... link01.obs:16:story.after_11:The attribute
#   -> adding an attribute to ObjectModel to distingush
#   object creation from scenario creation
#   -> locate ObjectModelSource et ScenarioModelSource


#================================================================
#   Infrastructure
#================================================================


# TODO:2 add hierachical metrics



#================================================================
#   Relational class model / relation model
#================================================================

# TODO:1  relational class model checks
# - pas d'association n-n
# - pas de classes associatives
# - pas de composition avec 0..1 du coté du composite
# - pas d'aggregation
# - pas de generalisation
# - pas de classe abstraite

# TODO:0 add support for code generation/transformation




#================================================================
#   Mis
#================================================================


# TODO:2 Installation procedure.
#       chmod +x for internal model-use
#       chmox +x for bin/*
# TODO:2 full support for addOnly, readOnly
# TODO:2 add [0..1] constraint   not self.x->isUndefined

#TODO: check what to do with  (link)object destruction

#TODO3: check plantuml generation

#TODO: add support for @assert inv / query
#TODO: add support for 'include x.obm' in scenarios

# #TODO: plantuml, check how to get errors from generation

# megamodels
# ----------
# * parser
# * summary/metrics
#
# glossaries
# ----------
#
# * metamodel
# * parser
# * integration in other models
# * summary/metrics
#
# usecases
# --------
#
# * summary
# * error checking
# * printer
# * add management of description
# * priority, interface, etc.
# * scm coverage - scm
# * pmm/clm coverage -- pmm ucm
#
# classes
# -------
#
# * refactor associationClass
# * add package statement
# * spec for clm language ?
# * check a few things in the parser
# * check if comment handling is ok
# * add a few test to check result
# * coverage of invariant wrt class model
# * pmm/ucm coverage -- pmm ucm
#
# objects
# -------
#
# * summary/metrics
# * add description
# * add the possibility to include other obm files at the begining
#   (avoid circular dependencies)
# * clm coverage
#
# scenarios
# ---------
#
# * summary/metrics
# * generation of access model
# * add the possibility to include a obm
# * add description
# * spec for scm as own language (while based on soil)
# * implement assertions (inv + query)
# * ucm coverage
# * clm coverage
# * plm coverage
#
# permissions
# -----------
#
# * summary/metrics?
# * improve language
# * pmm/
#
# access
# ------
#
# * define objectives
# * define language
#
