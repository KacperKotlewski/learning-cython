# distutils: language = c++

from henloWarp cimport henlo

cdef char* _chars(str pystring):
    cdef:
        char* s
    bstr = pystring.encode('utf-8')
    s = bstr
    return s


def test(str name):
    cdef:
        char* s;
    s = _chars(name)
    henlo(s)