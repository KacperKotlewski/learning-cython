# distutils: language = c++

from cwork cimport do_stuff

def py_do_stuff(stri):
    cdef char* s
    temp = stri.encode('utf-8')
    s = temp
    do_stuff(temp)
