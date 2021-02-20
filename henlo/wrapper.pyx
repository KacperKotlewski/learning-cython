# distutils: language = c++
# distutils: sources = "henlo/lib/henlo.cpp"
# ####### cython: language_level  = 3

cimport libWarp

# # imported version
# from .subpkg import util # if python type used in function cimport don't work properly fur such function
#
# cpdef test(str name):
#     cdef:
#         bytes b = util._chars(name)
#         char* s = b
#     libWarp.henlo(s)

# single file version
cdef char* _chars(str pystring):
    cdef:
        bytes bstr = pystring.encode('utf-8')
        char* s = bstr
    return s

cpdef test(str name):
    cdef:
        char* s = _chars(name)
    libWarp.henlo(s)