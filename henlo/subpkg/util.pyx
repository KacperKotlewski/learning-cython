cpdef char* _chars(str pystring):
    cdef:
        bytes bstr = pystring.encode('utf-8')
        char* s = bstr
    return s