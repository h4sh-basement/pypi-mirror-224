# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _optimisation
else:
    import _optimisation

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
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
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


import cmlibs.zinc.field
import cmlibs.zinc.differentialoperator
import cmlibs.zinc.element
import cmlibs.zinc.node
import cmlibs.zinc.fieldassignment
import cmlibs.zinc.fieldcache
import cmlibs.zinc.fieldmodule
import cmlibs.zinc.scenecoordinatesystem
import cmlibs.zinc.timesequence
import cmlibs.zinc.fieldsmoothing
import cmlibs.zinc.fieldparameters
import cmlibs.zinc.fieldrange
import cmlibs.zinc.region
import cmlibs.zinc.context
import cmlibs.zinc.font
import cmlibs.zinc.graphics
import cmlibs.zinc.glyph
import cmlibs.zinc.material
import cmlibs.zinc.spectrum
import cmlibs.zinc.tessellation
import cmlibs.zinc.light
import cmlibs.zinc.logger
import cmlibs.zinc.scenefilter
import cmlibs.zinc.sceneviewer
import cmlibs.zinc.scene
import cmlibs.zinc.selection
import cmlibs.zinc.timekeeper
import cmlibs.zinc.timenotifier
import cmlibs.zinc.scenepicker
import cmlibs.zinc.shader
import cmlibs.zinc.streamscene
import cmlibs.zinc.stream
import cmlibs.zinc.streamregion
import cmlibs.zinc.streamimage
class Optimisation(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _optimisation.Optimisation_swiginit(self, _optimisation.new_Optimisation(*args))
    __swig_destroy__ = _optimisation.delete_Optimisation

    def isValid(self):
        return _optimisation.Optimisation_isValid(self)
    METHOD_INVALID = _optimisation.Optimisation_METHOD_INVALID
    METHOD_QUASI_NEWTON = _optimisation.Optimisation_METHOD_QUASI_NEWTON
    METHOD_LEAST_SQUARES_QUASI_NEWTON = _optimisation.Optimisation_METHOD_LEAST_SQUARES_QUASI_NEWTON
    METHOD_NEWTON = _optimisation.Optimisation_METHOD_NEWTON
    ATTRIBUTE_FUNCTION_TOLERANCE = _optimisation.Optimisation_ATTRIBUTE_FUNCTION_TOLERANCE
    ATTRIBUTE_GRADIENT_TOLERANCE = _optimisation.Optimisation_ATTRIBUTE_GRADIENT_TOLERANCE
    ATTRIBUTE_STEP_TOLERANCE = _optimisation.Optimisation_ATTRIBUTE_STEP_TOLERANCE
    ATTRIBUTE_MAXIMUM_ITERATIONS = _optimisation.Optimisation_ATTRIBUTE_MAXIMUM_ITERATIONS
    ATTRIBUTE_MAXIMUM_FUNCTION_EVALUATIONS = _optimisation.Optimisation_ATTRIBUTE_MAXIMUM_FUNCTION_EVALUATIONS
    ATTRIBUTE_MAXIMUM_STEP = _optimisation.Optimisation_ATTRIBUTE_MAXIMUM_STEP
    ATTRIBUTE_MINIMUM_STEP = _optimisation.Optimisation_ATTRIBUTE_MINIMUM_STEP
    ATTRIBUTE_LINESEARCH_TOLERANCE = _optimisation.Optimisation_ATTRIBUTE_LINESEARCH_TOLERANCE
    ATTRIBUTE_MAXIMUM_BACKTRACK_ITERATIONS = _optimisation.Optimisation_ATTRIBUTE_MAXIMUM_BACKTRACK_ITERATIONS
    ATTRIBUTE_TRUST_REGION_SIZE = _optimisation.Optimisation_ATTRIBUTE_TRUST_REGION_SIZE
    ATTRIBUTE_FIELD_PARAMETERS_TIME = _optimisation.Optimisation_ATTRIBUTE_FIELD_PARAMETERS_TIME

    def getId(self):
        return _optimisation.Optimisation_getId(self)

    def getConditionalField(self, dependentField):
        return _optimisation.Optimisation_getConditionalField(self, dependentField)

    def setConditionalField(self, dependentField, conditionalField):
        return _optimisation.Optimisation_setConditionalField(self, dependentField, conditionalField)

    def addFieldassignment(self, fieldassignment):
        return _optimisation.Optimisation_addFieldassignment(self, fieldassignment)

    def getMethod(self):
        return _optimisation.Optimisation_getMethod(self)

    def setMethod(self, method):
        return _optimisation.Optimisation_setMethod(self, method)

    def getAttributeInteger(self, attribute):
        return _optimisation.Optimisation_getAttributeInteger(self, attribute)

    def setAttributeInteger(self, attribute, value):
        return _optimisation.Optimisation_setAttributeInteger(self, attribute, value)

    def getAttributeReal(self, attribute):
        return _optimisation.Optimisation_getAttributeReal(self, attribute)

    def setAttributeReal(self, attribute, value):
        return _optimisation.Optimisation_setAttributeReal(self, attribute, value)

    def getFirstDependentField(self):
        return _optimisation.Optimisation_getFirstDependentField(self)

    def getNextDependentField(self, refField):
        return _optimisation.Optimisation_getNextDependentField(self, refField)

    def addDependentField(self, field):
        return _optimisation.Optimisation_addDependentField(self, field)

    def removeDependentField(self, field):
        return _optimisation.Optimisation_removeDependentField(self, field)

    def getFirstObjectiveField(self):
        return _optimisation.Optimisation_getFirstObjectiveField(self)

    def getNextObjectiveField(self, refField):
        return _optimisation.Optimisation_getNextObjectiveField(self, refField)

    def addObjectiveField(self, field):
        return _optimisation.Optimisation_addObjectiveField(self, field)

    def removeObjectiveField(self, field):
        return _optimisation.Optimisation_removeObjectiveField(self, field)

    def getSolutionReport(self):
        return _optimisation.Optimisation_getSolutionReport(self)

    def optimise(self):
        return _optimisation.Optimisation_optimise(self)

# Register Optimisation in _optimisation:
_optimisation.Optimisation_swigregister(Optimisation)



