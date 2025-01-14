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
    from . import _logger
else:
    import _logger

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


class Logger(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _logger.Logger_swiginit(self, _logger.new_Logger(*args))
    __swig_destroy__ = _logger.delete_Logger
    CHANGE_FLAG_NONE = _logger.Logger_CHANGE_FLAG_NONE
    CHANGE_FLAG_NEW_MESSAGE = _logger.Logger_CHANGE_FLAG_NEW_MESSAGE
    CHANGE_FLAG_FINAL = _logger.Logger_CHANGE_FLAG_FINAL
    MESSAGE_TYPE_INVALID = _logger.Logger_MESSAGE_TYPE_INVALID
    MESSAGE_TYPE_ERROR = _logger.Logger_MESSAGE_TYPE_ERROR
    MESSAGE_TYPE_WARNING = _logger.Logger_MESSAGE_TYPE_WARNING
    MESSAGE_TYPE_INFORMATION = _logger.Logger_MESSAGE_TYPE_INFORMATION

    def isValid(self):
        return _logger.Logger_isValid(self)

    def getId(self):
        return _logger.Logger_getId(self)

    def getNumberOfMessages(self):
        return _logger.Logger_getNumberOfMessages(self)

    def getMessageTypeAtIndex(self, index):
        return _logger.Logger_getMessageTypeAtIndex(self, index)

    def getMessageTextAtIndex(self, index):
        return _logger.Logger_getMessageTextAtIndex(self, index)

    def setMaximumNumberOfMessages(self, number):
        return _logger.Logger_setMaximumNumberOfMessages(self, number)

    def removeAllMessages(self):
        return _logger.Logger_removeAllMessages(self)

    def createLoggernotifier(self):
        return _logger.Logger_createLoggernotifier(self)

    def __eq__(self, other):
        return _logger.Logger___eq__(self, other)

# Register Logger in _logger:
_logger.Logger_swigregister(Logger)


def __eq__(a, b):
    return _logger.__eq__(a, b)
class Loggerevent(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _logger.Loggerevent_swiginit(self, _logger.new_Loggerevent(*args))
    __swig_destroy__ = _logger.delete_Loggerevent

    def isValid(self):
        return _logger.Loggerevent_isValid(self)

    def getId(self):
        return _logger.Loggerevent_getId(self)

    def getChangeFlags(self):
        return _logger.Loggerevent_getChangeFlags(self)

    def getMessageType(self):
        return _logger.Loggerevent_getMessageType(self)

    def getMessageText(self):
        return _logger.Loggerevent_getMessageText(self)

    def getLogger(self):
        return _logger.Loggerevent_getLogger(self)

# Register Loggerevent in _logger:
_logger.Loggerevent_swigregister(Loggerevent)

class Loggercallback(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _logger.delete_Loggercallback

# Register Loggercallback in _logger:
_logger.Loggercallback_swigregister(Loggercallback)

class Loggernotifier(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _logger.Loggernotifier_swiginit(self, _logger.new_Loggernotifier(*args))
    __swig_destroy__ = _logger.delete_Loggernotifier

    def isValid(self):
        return _logger.Loggernotifier_isValid(self)

    def getId(self):
        return _logger.Loggernotifier_getId(self)

    def setCallback(self, *args):
        return _logger.Loggernotifier_setCallback(self, *args)

    def clearCallback(self):
        return _logger.Loggernotifier_clearCallback(self)

# Register Loggernotifier in _logger:
_logger.Loggernotifier_swigregister(Loggernotifier)



