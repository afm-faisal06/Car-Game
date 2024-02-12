'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_AMD_stencil_operation_extended'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_AMD_stencil_operation_extended',error_checker=_errors._error_checker)
GL_REPLACE_VALUE_AMD=_C('GL_REPLACE_VALUE_AMD',0x874B)
GL_SET_AMD=_C('GL_SET_AMD',0x874A)
GL_STENCIL_BACK_OP_VALUE_AMD=_C('GL_STENCIL_BACK_OP_VALUE_AMD',0x874D)
GL_STENCIL_OP_VALUE_AMD=_C('GL_STENCIL_OP_VALUE_AMD',0x874C)
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glStencilOpValueAMD(face,value):pass