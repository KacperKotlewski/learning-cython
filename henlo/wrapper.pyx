# distutils: language = c++
# distutils: sources = "henlo/lib/henlo.cpp"
# ####### cython: language_level  = 3

cimport libWarp

# from .subpkg import util
#
# cpdef test(str name):
#     cdef:
#         bytes b = util._chars(name)
#         char* s = b
#     libWarp.henlo(s)

cdef char* _chars(str pystring):
    cdef:
        bytes bstr = pystring.encode('utf-8')
        char* s = bstr
    return s

cpdef test(str name):
    cdef:
        char* s = _chars(name)
    libWarp.henlo(s)