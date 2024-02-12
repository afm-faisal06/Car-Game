'''OpenGL extension IMG.read_format

This module customises the behaviour of the 
OpenGL.raw.GLES2.IMG.read_format to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension is intended to supplement the GL_OES_read_format
	extension by adding support for more format/type combinations to be used
	when calling ReadPixels.  ReadPixels currently accepts one fixed
	format/type combination (format RGBA and type UNSIGNED_BYTE) for
	portability, and an implementation specific format/type combination
	queried using the tokens IMPLEMENTATION_COLOR_READ_FORMAT_OES and
	IMPLEMENTATION_COLOR_READ_TYPE_OES (GL_OES_read_format extension).  This
	extension adds the following format/type combinations to those currently
	allowed to be returned by GetIntegerV:
	
	format                      type
	------                      ----
	BGRA_IMG                    UNSIGNED_BYTE
	BGRA_IMG                    UNSIGNED_SHORT_4_4_4_4_REV_IMG
	
	E.g. Calling GetIntegerv with a <pname> parameter of
	IMPLEMENTATION_COLOR_READ_FORMAT_OES can now return BGRA, with the
	corresponding call to GetIntegerv using a <pname> parameter of
	IMPLEMENTATION_COLOR_READ_TYPE_OES returning UNSIGNED_BYTE;

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/IMG/read_format.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.IMG.read_format import *
from OpenGL.raw.GLES2.IMG.read_format import _EXTENSION_NAME

def glInitReadFormatIMG():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION