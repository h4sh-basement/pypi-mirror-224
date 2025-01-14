# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.1.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _scene
else:
    import _scene

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
import cmlibs.zinc.scenefilter
import cmlibs.zinc.sceneviewer
import cmlibs.zinc.shader
import cmlibs.zinc.tessellation
import cmlibs.zinc.timekeeper
import cmlibs.zinc.timenotifier
import cmlibs.zinc.streamregion
import cmlibs.zinc.stream
import cmlibs.zinc.streamimage
import cmlibs.zinc.selection
import cmlibs.zinc.scenepicker
import cmlibs.zinc.streamscene
class Scene(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _scene.Scene_swiginit(self, _scene.new_Scene(*args))
    __swig_destroy__ = _scene.delete_Scene

    def isValid(self):
        return _scene.Scene_isValid(self)

    def getId(self):
        return _scene.Scene_getId(self)

    def beginChange(self):
        return _scene.Scene_beginChange(self)

    def endChange(self):
        return _scene.Scene_endChange(self)

    def convertToPointCloud(self, filter, nodeset, coordinateField, lineDensity, lineDensityScaleFactor, surfaceDensity, surfaceDensityScaleFactor):
        return _scene.Scene_convertToPointCloud(self, filter, nodeset, coordinateField, lineDensity, lineDensityScaleFactor, surfaceDensity, surfaceDensityScaleFactor)

    def convertPointsToNodes(self, filter, nodeset, coordinateField):
        return _scene.Scene_convertPointsToNodes(self, filter, nodeset, coordinateField)

    def createGraphics(self, graphicsType):
        return _scene.Scene_createGraphics(self, graphicsType)

    def createGraphicsContours(self):
        return _scene.Scene_createGraphicsContours(self)

    def createGraphicsLines(self):
        return _scene.Scene_createGraphicsLines(self)

    def createGraphicsPoints(self):
        return _scene.Scene_createGraphicsPoints(self)

    def createGraphicsStreamlines(self):
        return _scene.Scene_createGraphicsStreamlines(self)

    def createGraphicsSurfaces(self):
        return _scene.Scene_createGraphicsSurfaces(self)

    def createSelectionnotifier(self):
        return _scene.Scene_createSelectionnotifier(self)

    def findGraphicsByName(self, name):
        return _scene.Scene_findGraphicsByName(self, name)

    def getCoordinatesRange(self, filter):
        return _scene.Scene_getCoordinatesRange(self, filter)

    def getFirstGraphics(self):
        return _scene.Scene_getFirstGraphics(self)

    def getNextGraphics(self, refGraphics):
        return _scene.Scene_getNextGraphics(self, refGraphics)

    def getPreviousGraphics(self, refGraphics):
        return _scene.Scene_getPreviousGraphics(self, refGraphics)

    def getNumberOfGraphics(self):
        return _scene.Scene_getNumberOfGraphics(self)

    def getRegion(self):
        return _scene.Scene_getRegion(self)

    def getFontmodule(self):
        return _scene.Scene_getFontmodule(self)

    def getGlyphmodule(self):
        return _scene.Scene_getGlyphmodule(self)

    def getLightmodule(self):
        return _scene.Scene_getLightmodule(self)

    def getMaterialmodule(self):
        return _scene.Scene_getMaterialmodule(self)

    def getScenefiltermodule(self):
        return _scene.Scene_getScenefiltermodule(self)

    def getSceneviewermodule(self):
        return _scene.Scene_getSceneviewermodule(self)

    def getShadermodule(self):
        return _scene.Scene_getShadermodule(self)

    def getSpectrummodule(self):
        return _scene.Scene_getSpectrummodule(self)

    def getTessellationmodule(self):
        return _scene.Scene_getTessellationmodule(self)

    def getTimekeepermodule(self):
        return _scene.Scene_getTimekeepermodule(self)

    def getSelectionField(self):
        return _scene.Scene_getSelectionField(self)

    def setSelectionField(self, selectionField):
        return _scene.Scene_setSelectionField(self, selectionField)

    def getSpectrumDataRange(self, filter, spectrum, valuesCount):
        return _scene.Scene_getSpectrumDataRange(self, filter, spectrum, valuesCount)

    def clearTransformation(self):
        return _scene.Scene_clearTransformation(self)

    def hasTransformation(self):
        return _scene.Scene_hasTransformation(self)

    def getTransformationField(self):
        return _scene.Scene_getTransformationField(self)

    def setTransformationField(self, transformationField):
        return _scene.Scene_setTransformationField(self, transformationField)

    def getTransformationMatrix(self):
        return _scene.Scene_getTransformationMatrix(self)

    def setTransformationMatrix(self, valuesIn16):
        return _scene.Scene_setTransformationMatrix(self, valuesIn16)

    def getVisibilityFlag(self):
        return _scene.Scene_getVisibilityFlag(self)

    def setVisibilityFlag(self, visibilityFlag):
        return _scene.Scene_setVisibilityFlag(self, visibilityFlag)

    def moveGraphicsBefore(self, graphics, refGraphics):
        return _scene.Scene_moveGraphicsBefore(self, graphics, refGraphics)

    def removeAllGraphics(self):
        return _scene.Scene_removeAllGraphics(self)

    def removeGraphics(self, graphics):
        return _scene.Scene_removeGraphics(self, graphics)

    def writeDescription(self):
        return _scene.Scene_writeDescription(self)

    def readDescription(self, description, overwrite):
        return _scene.Scene_readDescription(self, description, overwrite)

    def createScenepicker(self):
        return _scene.Scene_createScenepicker(self)

    def write(self, streaminformationScene):
        return _scene.Scene_write(self, streaminformationScene)

    def read(self, streaminformationScene):
        return _scene.Scene_read(self, streaminformationScene)

    def createStreaminformationScene(self):
        return _scene.Scene_createStreaminformationScene(self)

    def __eq__(self, other):
        return _scene.Scene___eq__(self, other)

# Register Scene in _scene:
_scene.Scene_swigregister(Scene)

def __eq__(*args):
    return _scene.__eq__(*args)

