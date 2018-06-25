# coding=utf-8

"""
Simple metamodel for object states.
The metamodel represents two views:
* an abstract view in which object/slots and links are
  represented without and order,
* a story view that represents the same entities but
  as they are defined, as in a story, in a sequential order
  and with Annotated OBject (AOB) text blocks, that is text
  blocks nested definitions.


    Abstract view
        ObjectModel
        <>--* Object
            <>--* Slot
        <>--* Link
        <>--* LinkObject

        StateElement
        <|-- Object
        <|-- Link

        Link, Object
        <|-- LinkObject

    Story view
        Definition
        <|-- CoreDefinition
             <|-- Object
             <|-- Slot
             <|-- Link
        <|-- AnnotatedTextBlock
            <>--* CoreDefinition
"""


from collections import OrderedDict
from typing import List, Optional, Dict, Text, Union
from abc import ABCMeta, abstractmethod

# TODO: to be continued
from modelscripts.megamodels.py import (
    MAttribute
)
from modelscripts.megamodels.elements import SourceModelElement
from modelscripts.base.metrics import Metrics
from modelscripts.megamodels.metamodels import Metamodel
from modelscripts.megamodels.models import (
    Model,
    Placeholder)
from modelscripts.megamodels.dependencies.metamodels import (
    MetamodelDependency
)
# used for typing
from modelscripts.metamodels.classes import (
    ClassModel,
    Class,
    Attribute,
    Association,
    METAMODEL as CLASS_METAMODEL
)
from modelscripts.metamodels.textblocks import (
    TextBlock
)

__all__=(
    'ObjectModel',
    'StateElement',
    'Object',
    'AOBTextBlock',
    'PlainObject',
    'BasicValue',
    'Slot',
    'Link',
    'PlainLink',
    'LinkObject',
)


class ObjectModel(Model):

    def __init__(self):
        super(ObjectModel, self).__init__()

        # ALL packages, not only the top level ones
        self.packageNamed=OrderedDict() #type: Dict[Text, Package]

        self._objectNamed = OrderedDict()
        # type: Dict[Text, Object]
        """
        All objects (plain objects and link objects).
        Link object are also registered in _links.
        """

        self._links=[]
        # type: List[Link]
        """
        All plain links (no link object).
        Link objects are also regitered in _objectNamed.
        """

        self._classModel=None
        #type: Optional[ClassModel]
        # filled by property

        self.storyEvaluation=None
        #type: Optional['StoryEvaluation']
        # Filled only if this model is the result of a story evaluation.
        # Otherwise this is most probably a handmade model.

    @property
    def classModel(self):
        #type: ()-> ClassModel
        if self._classModel is None:
            self._classModel=self.theModel(CLASS_METAMODEL)
        return self._classModel

    def object(self, name):
        if name in self._objectNamed:
            return self._objectNamed[name]
        else:
            return None

    @property
    def objects(self):
        #type: () -> List[Object]
        return self._objectNamed.values()

    @property
    def plainObjects(self):
        #type: () -> List[PlainObject]
        return [
            o for o in self.objects if isinstance(o, PlainObject) ]

    @property
    def linkObjects(self):
        #type: () -> List[LinkObject]
        return [
            o for o in self.objects if isinstance(o, LinkObject) ]

    @property
    def links(self):
        #type: () -> List[Link]
        return self._links

    @property
    def plainLinks(self):
        #type: () -> List[PlainLink]
        return [
            l for l in self._links if isinstance(l, PlainLink) ]


    @property
    def metrics(self):
        #type: () -> Metrics
        ms=super(ObjectModel, self).metrics
        ms.addList((
            ('object', len(self.objects)),
            ('link', len(self.links)),
            ('plain object', len(self.plainObjects)),
            ('plain link', len(self.plainLinks)),
            ('link object', len(self.linkObjects)),
            ('slot',sum(
                len(o.slots)
                for o in self.objects))
        ))
        return ms

    @property
    def metamodel(self):
        #type: () -> Metamodel
        return METAMODEL



class ElementFromStep(SourceModelElement):
    """
    All elements that can come from a story step.
    Serve as a superclass of other class and add
    a step attribut. This attribute could be None.
    If this attribute exist its astNode is taken
    to locate the element, unless a new position
    is defined.
    """
    __metaclass__ = ABCMeta

    def __init__(self,
                 name,
                 model,
                 step=None,
                 astNode=None,
                 lineNo=None, description=None):
        #type: (Optional['Step']) -> None
        if astNode is None and step is not None:
            ast_node=step.astNode
        else:
            ast_node=astNode
        if lineNo is None and step is not None:
            line_no=step.lineNo
        else:
            line_no=lineNo
        if description is None and step is not None:
            description_=step.description
        else:
            description_=description
        super(ElementFromStep, self).__init__(
            model=model,
            name=name,
            astNode=ast_node,
            lineNo=line_no, description=description_)
        self.step=step


class PackagableElement(ElementFromStep):
    """
    Top level element.
    """
    __metaclass__ = ABCMeta

    def __init__(self,
                 name,
                 model,
                 package=None,
                 step=None,
                 lineNo=None, astNode=None, description=None):
        super(PackagableElement, self).__init__(
            model=model,
            name=name,
            step=step,
            astNode=astNode,
            lineNo=lineNo, description=description)
        self.package=package
        if self.package is not None:
            self.package.addElement(self)

    @MAttribute('String')
    def label(self):
        if self.package is not None:
            return '%s.%s' % (
                self.package.label,
                self.name)
        else:
            return self.name




class ResourceInstance(object):
    __metaclass__ = ABCMeta
    """ 
    Currently not used, but can be useful to describes
    access instances. 
    This corresponds to the instance level of Resource.
    See modelscripts.metamodels.permissions.sar.Resource
    """

class Entity(ResourceInstance):
    __metaclass__ = ABCMeta


class Member(ResourceInstance):
    __metaclass__ = ABCMeta


# TODO: generalize and improve packages
#       This class comes from metamodels.class
#       It would make sense to move this to a upper level

class Package(PackagableElement):
    """
    Packages.
    """
    def __init__(self,
                 name,
                 model,
                 package=None,
                 step=None,
                 lineNo=None, astNode=None, description=None):
        PackagableElement.__init__(
            self,
            name=name,
            model=model,
            package=package,
            step=None,
            lineNo=lineNo, astNode=astNode, description=description)
        self._elememts=[]
        self.model.packageNamed[name]=self


    @property
    def elements(self):
        return self._elememts

    def addElement(self, element):
        assert element is not None
        if element not in self._elememts:
            self._elememts.append(element)
            element.package=self


class Object(PackagableElement, Entity):
    """
    An object. Either a plain object or a link object.
    Link object
    """
    __metaclass__ = ABCMeta

    def __init__(self, model, name, class_,
                 package=None,
                 step=None,
                 lineNo=None, description=None, astNode=None):
        #type: (ObjectModel, Text, Union[Class, Placeholder], Optional[package], Optional['Step'], Optional[int], Optional[TextBlock], Optional['ASTNode'] )-> None
        PackagableElement.__init__(
            self,
            model=model,
            name=name,
            package=package,
            step=step,
            astNode=astNode,
            lineNo=lineNo,
            description=description
        )
        Entity.__init__(self)

        self.class_ = class_
        #type: Union[Placeholder, Class]

        self._slotNamed = OrderedDict()
        #type: Dict[Text, Slot]
        # Slots of the object indexed by attribute name (not attribute)

        #TODO: check for duplicates to avoid loosing objects
        # Register the object in the model for the abstract view
        model._objectNamed[name]=self

    @property
    def slots(self):
        return list(self._slotNamed.values())

    def slot(self, name):
        if name in self._slotNamed:
            return self._slotNamed[name]
        else:
            return None

    @abstractmethod
    def isPlainObject(self):
        # just used to prevent creating object of this class
        # (ABCMeta is not enough)
        raise NotImplementedError()

    # def delete(self):
    #     #TODO:  implement delete operation on objects
    #
    #     raise NotImplementedError('Delete operation on objects is not implemented')



class PlainObject(Object):

    def __init__(self, model, name, class_,
                 package=None,
                 step=None,
                 lineNo=None, description=None, astNode=None):
        #type: (ObjectModel, Text, Union[Class, Placeholder], Optional[package], Optional['Step'], Optional[int], Optional['ASTNode'] )-> None
        super(PlainObject, self).__init__(
            model=model,
            name=name,
            class_=class_,
            package=package,
            step=step,
            astNode=astNode,
            lineNo=lineNo,
            description=description
        )

    def isPlainObject(self):
        return True


BasicValue=Union[Text, 'Bool', int, float]



class Slot(ElementFromStep, Member):

    def __init__(self, object, attribute, value,
                 step=None,
                 description=None, lineNo=None, astNode=None):
        #type: (Object, Union[Attribute, Placeholder], BasicValue,  Optional['Step'], Optional[TextBlock], Optional[int], 'ASTNode') -> None
        attribute_name=(
            attribute.placeholderValue
                if isinstance(attribute, Placeholder)
            else attribute.name
        )
        ElementFromStep.__init__(
            self,
            model=object.model,
            name='%s.%s' % (object.name, attribute_name),
            step=step,
            astNode=astNode,
            lineNo=lineNo,
            description=description)
        Member.__init__(self)
        self.object=object

        self.attribute=attribute
        self.value=value
        object._slotNamed[attribute_name]=self



class Link(PackagableElement, Entity):
    __metaclass__ = ABCMeta

    def __init__(self,
                 model, association,
                 sourceObject, targetObject,
                 name=None,
                 package=None,
                 step=None,
                 astNode=None, lineNo=None,
                 description=None):
        #type: (ObjectModel, Union[Association, Placeholder], Object, Object, Optional[Text], Optional[Package], Optional['Step'],Optional['ASTNode'], Optional[int], Optional[TextBlock]) -> None
        PackagableElement.__init__(
            self,
            model=model,
            name=name,
            package=package,
            step=step,
            astNode=astNode,
            lineNo=lineNo,
            description=description
        )
        Entity.__init__(self)

        self.association=association
        #type: association

        self.sourceObject = sourceObject
        # type: Object

        self.targetObject = targetObject
        # type: Object

        model._links.append(self)

    @abstractmethod
    def isPlainLink(self):
        # just used to prevent creating object of this class
        # (ABCMeta is not enough)
        raise NotImplementedError()


class PlainLink(Link):

    def __init__(self,
                 model, association,
                 sourceObject, targetObject,
                 name=None,
                 package=None,
                 step=None,
                 astNode=None, lineNo=None,
                 description=None):
        #type: (ObjectModel, Union[Association, Placeholder], Object, Object, Optional[Text], Optional[Package], Optional['Step'], Optional['ASTNode'], Optional[int], Optional[TextBlock]) -> None
        super(PlainLink, self).__init__(
            model=model,
            association=association,
            sourceObject=sourceObject,
            targetObject=targetObject,
            name=name,
            package=package,
            step=step,
            astNode=astNode,
            lineNo=lineNo,
            description=description
        )

    def isPlainLink(self):
        return True

    # def delete(self):
    #     self.state.links=[l for l in self.state.links if l != self]



class LinkObject(Object, Link):

    def __init__(self, model, associationClass,
                 sourceObject, targetObject,
                 name,
                 package=None,
                 step=None,
                 astNode=None, lineNo=None,
                 description=None):
        Object.__init__(
            self,
            model=model,
            name=name,
            class_=associationClass,
            package=package,
            step=step,
            astNode=astNode,
            lineNo=lineNo,
            description=description
        )
        # the linkObject has been added to _objectNamed

        Link.__init__(
            self,
            model=model,
            association=associationClass,
            sourceObject=sourceObject,
            targetObject=targetObject,
            name=name,
            package=package,
            step=step,
            astNode=astNode,
            lineNo=lineNo,
            description=description
        )
        # the linkObject has been added to _links

        # just make sure that the name of this link object is set.
        # This avoid relying on the implementation of Link constructor.
        # This could be an issue otherwize since link have no name.
        self.name=name


    # def delete(self):
    #     #TODO:  implement delete operation on link objects
    #     raise NotImplementedError('Delete operation on link object is not implemented')

    def isPlainLink(self):
        return False

    def isPlainObject(self):
        return False


METAMODEL = Metamodel(
    id='ob',
    label='object',
    extension='.obs',
    modelClass=ObjectModel
)
MetamodelDependency(
    sourceId='ob',
    targetId='gl',
    optional=True,
    multiple=True,
)
MetamodelDependency(
    sourceId='ob',
    targetId='ob',
    optional=True,
    multiple=True,
)
MetamodelDependency(
    sourceId='ob',
    targetId='cl',
    optional=False,
    multiple=True,
)