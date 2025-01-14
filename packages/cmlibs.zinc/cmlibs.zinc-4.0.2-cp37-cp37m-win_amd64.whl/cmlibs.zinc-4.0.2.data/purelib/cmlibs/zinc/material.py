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
    from . import _material
else:
    import _material

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


import cmlibs.zinc.context
import cmlibs.zinc.font
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
import cmlibs.zinc.scene
import cmlibs.zinc.scenefilter
import cmlibs.zinc.selection
import cmlibs.zinc.timekeeper
import cmlibs.zinc.timenotifier
import cmlibs.zinc.scenepicker
import cmlibs.zinc.sceneviewer
import cmlibs.zinc.light
import cmlibs.zinc.shader
import cmlibs.zinc.spectrum
import cmlibs.zinc.streamscene
import cmlibs.zinc.stream
import cmlibs.zinc.streamregion
import cmlibs.zinc.streamimage
import cmlibs.zinc.glyph
import cmlibs.zinc.tessellation
import cmlibs.zinc.logger
class Material(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _material.Material_swiginit(self, _material.new_Material(*args))
    __swig_destroy__ = _material.delete_Material

    def isValid(self):
        return _material.Material_isValid(self)

    def getId(self):
        return _material.Material_getId(self)
    ATTRIBUTE_INVALID = _material.Material_ATTRIBUTE_INVALID
    ATTRIBUTE_ALPHA = _material.Material_ATTRIBUTE_ALPHA
    ATTRIBUTE_AMBIENT = _material.Material_ATTRIBUTE_AMBIENT
    ATTRIBUTE_DIFFUSE = _material.Material_ATTRIBUTE_DIFFUSE
    ATTRIBUTE_EMISSION = _material.Material_ATTRIBUTE_EMISSION
    ATTRIBUTE_SHININESS = _material.Material_ATTRIBUTE_SHININESS
    ATTRIBUTE_SPECULAR = _material.Material_ATTRIBUTE_SPECULAR
    CHANGE_FLAG_NONE = _material.Material_CHANGE_FLAG_NONE
    CHANGE_FLAG_ADD = _material.Material_CHANGE_FLAG_ADD
    CHANGE_FLAG_REMOVE = _material.Material_CHANGE_FLAG_REMOVE
    CHANGE_FLAG_IDENTIFIER = _material.Material_CHANGE_FLAG_IDENTIFIER
    CHANGE_FLAG_DEFINITION = _material.Material_CHANGE_FLAG_DEFINITION
    CHANGE_FLAG_FULL_RESULT = _material.Material_CHANGE_FLAG_FULL_RESULT
    CHANGE_FLAG_FINAL = _material.Material_CHANGE_FLAG_FINAL

    def isManaged(self):
        return _material.Material_isManaged(self)

    def setManaged(self, value):
        return _material.Material_setManaged(self, value)

    def getAttributeReal(self, attribute):
        return _material.Material_getAttributeReal(self, attribute)

    def setAttributeReal(self, attribute, value):
        return _material.Material_setAttributeReal(self, attribute, value)

    def getAttributeReal3(self, attribute):
        return _material.Material_getAttributeReal3(self, attribute)

    def setAttributeReal3(self, attribute, valuesIn3):
        return _material.Material_setAttributeReal3(self, attribute, valuesIn3)

    def getName(self):
        return _material.Material_getName(self)

    def setName(self, name):
        return _material.Material_setName(self, name)

    def getTextureField(self, textureNumber):
        return _material.Material_getTextureField(self, textureNumber)

    def setTextureField(self, textureNumber, textureField):
        return _material.Material_setTextureField(self, textureNumber, textureField)

    def getShaderuniforms(self):
        return _material.Material_getShaderuniforms(self)

    def setShaderuniforms(self, shaderuniforms):
        return _material.Material_setShaderuniforms(self, shaderuniforms)

    def getShaderprogram(self):
        return _material.Material_getShaderprogram(self)

    def setShaderprogram(self, shaderprogram):
        return _material.Material_setShaderprogram(self, shaderprogram)

    def __eq__(self, other):
        return _material.Material___eq__(self, other)

# Register Material in _material:
_material.Material_swigregister(Material)


def __eq__(*args):
    return _material.__eq__(*args)
class Materialiterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _material.Materialiterator_swiginit(self, _material.new_Materialiterator(*args))
    __swig_destroy__ = _material.delete_Materialiterator

    def isValid(self):
        return _material.Materialiterator_isValid(self)

    def next(self):
        return _material.Materialiterator_next(self)

# Register Materialiterator in _material:
_material.Materialiterator_swigregister(Materialiterator)

class Materialmodule(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _material.Materialmodule_swiginit(self, _material.new_Materialmodule(*args))
    __swig_destroy__ = _material.delete_Materialmodule

    def isValid(self):
        return _material.Materialmodule_isValid(self)

    def getId(self):
        return _material.Materialmodule_getId(self)

    def createMaterial(self):
        return _material.Materialmodule_createMaterial(self)

    def createMaterialiterator(self):
        return _material.Materialmodule_createMaterialiterator(self)

    def findMaterialByName(self, name):
        return _material.Materialmodule_findMaterialByName(self, name)

    def beginChange(self):
        return _material.Materialmodule_beginChange(self)

    def endChange(self):
        return _material.Materialmodule_endChange(self)

    def defineStandardMaterials(self):
        return _material.Materialmodule_defineStandardMaterials(self)

    def getContext(self):
        return _material.Materialmodule_getContext(self)

    def getDefaultMaterial(self):
        return _material.Materialmodule_getDefaultMaterial(self)

    def setDefaultMaterial(self, material):
        return _material.Materialmodule_setDefaultMaterial(self, material)

    def getDefaultSelectedMaterial(self):
        return _material.Materialmodule_getDefaultSelectedMaterial(self)

    def setDefaultSelectedMaterial(self, material):
        return _material.Materialmodule_setDefaultSelectedMaterial(self, material)

    def getDefaultSurfaceMaterial(self):
        return _material.Materialmodule_getDefaultSurfaceMaterial(self)

    def setDefaultSurfaceMaterial(self, material):
        return _material.Materialmodule_setDefaultSurfaceMaterial(self, material)

    def readDescription(self, description):
        return _material.Materialmodule_readDescription(self, description)

    def writeDescription(self):
        return _material.Materialmodule_writeDescription(self)

    def createMaterialmodulenotifier(self):
        return _material.Materialmodule_createMaterialmodulenotifier(self)

# Register Materialmodule in _material:
_material.Materialmodule_swigregister(Materialmodule)

class Materialmoduleevent(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _material.Materialmoduleevent_swiginit(self, _material.new_Materialmoduleevent(*args))
    __swig_destroy__ = _material.delete_Materialmoduleevent

    def isValid(self):
        return _material.Materialmoduleevent_isValid(self)

    def getId(self):
        return _material.Materialmoduleevent_getId(self)

    def getMaterialChangeFlags(self, material):
        return _material.Materialmoduleevent_getMaterialChangeFlags(self, material)

    def getSummaryMaterialChangeFlags(self):
        return _material.Materialmoduleevent_getSummaryMaterialChangeFlags(self)

# Register Materialmoduleevent in _material:
_material.Materialmoduleevent_swigregister(Materialmoduleevent)

class Materialmodulecallback(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _material.delete_Materialmodulecallback

# Register Materialmodulecallback in _material:
_material.Materialmodulecallback_swigregister(Materialmodulecallback)

class Materialmodulenotifier(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _material.Materialmodulenotifier_swiginit(self, _material.new_Materialmodulenotifier(*args))
    __swig_destroy__ = _material.delete_Materialmodulenotifier

    def isValid(self):
        return _material.Materialmodulenotifier_isValid(self)

    def getId(self):
        return _material.Materialmodulenotifier_getId(self)

    def setCallback(self, *args):
        return _material.Materialmodulenotifier_setCallback(self, *args)

    def clearCallback(self):
        return _material.Materialmodulenotifier_clearCallback(self)

# Register Materialmodulenotifier in _material:
_material.Materialmodulenotifier_swigregister(Materialmodulenotifier)



