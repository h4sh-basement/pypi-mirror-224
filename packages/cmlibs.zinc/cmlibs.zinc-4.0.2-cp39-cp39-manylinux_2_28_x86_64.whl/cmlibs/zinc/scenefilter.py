# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.1.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _scenefilter
else:
    import _scenefilter

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import cmlibs.zinc.graphics
import cmlibs.zinc.field
import cmlibs.zinc.differentialoperator
import cmlibs.zinc.element
import cmlibs.zinc.node
import cmlibs.zinc.fieldassignment
import cmlibs.zinc.fieldcache
import cmlibs.zinc.fieldmodule
import cmlibs.zinc.scenecoordinatesystem
import cmlibs.zinc.timesequence
import cmlibs.zinc.optimisation
import cmlibs.zinc.fieldsmoothing
import cmlibs.zinc.fieldparameters
import cmlibs.zinc.fieldrange
import cmlibs.zinc.region
import cmlibs.zinc.context
import cmlibs.zinc.font
import cmlibs.zinc.glyph
import cmlibs.zinc.material
import cmlibs.zinc.spectrum
import cmlibs.zinc.light
import cmlibs.zinc.logger
import cmlibs.zinc.sceneviewer
import cmlibs.zinc.scene
import cmlibs.zinc.selection
import cmlibs.zinc.timekeeper
import cmlibs.zinc.timenotifier
import cmlibs.zinc.scenepicker
import cmlibs.zinc.shader
import cmlibs.zinc.streamscene
import cmlibs.zinc.stream
import cmlibs.zinc.tessellation
import cmlibs.zinc.streamregion
import cmlibs.zinc.streamimage
class Scenefilter(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _scenefilter.Scenefilter_swiginit(self, _scenefilter.new_Scenefilter(*args))
    __swig_destroy__ = _scenefilter.delete_Scenefilter

    def isValid(self):
        return _scenefilter.Scenefilter_isValid(self)

    def getId(self):
        return _scenefilter.Scenefilter_getId(self)

    def isManaged(self):
        return _scenefilter.Scenefilter_isManaged(self)

    def setManaged(self, value):
        return _scenefilter.Scenefilter_setManaged(self, value)

    def evaluateGraphics(self, graphics):
        return _scenefilter.Scenefilter_evaluateGraphics(self, graphics)

    def isInverse(self):
        return _scenefilter.Scenefilter_isInverse(self)

    def setInverse(self, value):
        return _scenefilter.Scenefilter_setInverse(self, value)

    def getName(self):
        return _scenefilter.Scenefilter_getName(self)

    def setName(self, name):
        return _scenefilter.Scenefilter_setName(self, name)

    def castOperator(self):
        return _scenefilter.Scenefilter_castOperator(self)

    def __eq__(self, other):
        return _scenefilter.Scenefilter___eq__(self, other)

# Register Scenefilter in _scenefilter:
_scenefilter.Scenefilter_swigregister(Scenefilter)

def __eq__(*args):
    return _scenefilter.__eq__(*args)
class ScenefilterOperator(Scenefilter):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _scenefilter.ScenefilterOperator_swiginit(self, _scenefilter.new_ScenefilterOperator(*args))

    def appendOperand(self, operand):
        return _scenefilter.ScenefilterOperator_appendOperand(self, operand)

    def getFirstOperand(self):
        return _scenefilter.ScenefilterOperator_getFirstOperand(self)

    def getNextOperand(self, refOperand):
        return _scenefilter.ScenefilterOperator_getNextOperand(self, refOperand)

    def isOperandActive(self, operand):
        return _scenefilter.ScenefilterOperator_isOperandActive(self, operand)

    def setOperandActive(self, operand, isActive):
        return _scenefilter.ScenefilterOperator_setOperandActive(self, operand, isActive)

    def insertOperandBefore(self, operand, refOperand):
        return _scenefilter.ScenefilterOperator_insertOperandBefore(self, operand, refOperand)

    def removeOperand(self, operand):
        return _scenefilter.ScenefilterOperator_removeOperand(self, operand)
    __swig_destroy__ = _scenefilter.delete_ScenefilterOperator

# Register ScenefilterOperator in _scenefilter:
_scenefilter.ScenefilterOperator_swigregister(ScenefilterOperator)
class Scenefiltermodule(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _scenefilter.Scenefiltermodule_swiginit(self, _scenefilter.new_Scenefiltermodule(*args))
    __swig_destroy__ = _scenefilter.delete_Scenefiltermodule

    def isValid(self):
        return _scenefilter.Scenefiltermodule_isValid(self)

    def getId(self):
        return _scenefilter.Scenefiltermodule_getId(self)

    def createScenefilterVisibilityFlags(self):
        return _scenefilter.Scenefiltermodule_createScenefilterVisibilityFlags(self)

    def createScenefilterFieldDomainType(self, domainType):
        return _scenefilter.Scenefiltermodule_createScenefilterFieldDomainType(self, domainType)

    def createScenefilterGraphicsName(self, matchName):
        return _scenefilter.Scenefiltermodule_createScenefilterGraphicsName(self, matchName)

    def createScenefilterGraphicsType(self, graphicsType):
        return _scenefilter.Scenefiltermodule_createScenefilterGraphicsType(self, graphicsType)

    def createScenefilterRegion(self, matchRegion):
        return _scenefilter.Scenefiltermodule_createScenefilterRegion(self, matchRegion)

    def createScenefilterOperatorAnd(self):
        return _scenefilter.Scenefiltermodule_createScenefilterOperatorAnd(self)

    def createScenefilterOperatorOr(self):
        return _scenefilter.Scenefiltermodule_createScenefilterOperatorOr(self)

    def findScenefilterByName(self, name):
        return _scenefilter.Scenefiltermodule_findScenefilterByName(self, name)

    def beginChange(self):
        return _scenefilter.Scenefiltermodule_beginChange(self)

    def endChange(self):
        return _scenefilter.Scenefiltermodule_endChange(self)

    def getDefaultScenefilter(self):
        return _scenefilter.Scenefiltermodule_getDefaultScenefilter(self)

    def setDefaultScenefilter(self, filter):
        return _scenefilter.Scenefiltermodule_setDefaultScenefilter(self, filter)

# Register Scenefiltermodule in _scenefilter:
_scenefilter.Scenefiltermodule_swigregister(Scenefiltermodule)

