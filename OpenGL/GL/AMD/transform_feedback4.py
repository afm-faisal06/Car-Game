'''OpenGL extension AMD.transform_feedback4

This module customises the behaviour of the 
OpenGL.raw.GL.AMD.transform_feedback4 to provide a more 
Python-friendly API

Overview (from the spec)
	
	Transform feedback is a mechanism to record the output of the vertex,
	tessellation evaluation or geometry shader into one or more buffers for
	further processing, recursive rendering or read-back by the client.
	ARB_transform_feedback3 (and OpenGL 4.0) extended the transform feedback
	subsystem to allow multiple streams of primitive information to be
	captured. However, it imposed a limitation that the primitive type for all
	streams must be POINTS if more than one stream is to be captured.
	AMD_transform_feedback3_lines_triangles relaxed that restriction to allow
	lines or triangles to be captured, in the case where multiple streams are
	to be processed. However, it still required that all streams share the same
	primitive type. Additionally, with all current extensions to transform
	feedback, only a single primitive stream may be rasterized.
	
	This extension enhances transform feedback in two significant ways. First,
	it allows multiple transform feedback streams to be captured, each with its
	own, independent primitve type. Second, it allows any combination of streams
	to be rasterized. As an example, this enables the geometry shader to take
	a single stream of triangle geometry and emit filled triangles with a
	wireframe outline and a point at each vertex, all in a single pass through
	the input vertices. Combined with features such those provided by
	ARB_viewport_array, layered rendering, shader subroutines and so on, an
	application can render several views of its geoemtry, each with a
	radically different style, all in a single pass.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/AMD/transform_feedback4.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.AMD.transform_feedback4 import *
from OpenGL.raw.GL.AMD.transform_feedback4 import _EXTENSION_NAME

def glInitTransformFeedback4AMD():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION