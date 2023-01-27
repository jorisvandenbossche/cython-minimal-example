
cdef class _Weakrefable:
    cdef object __weakref__


cdef class MyBaseClass(_Weakrefable):

    cdef readonly:
        object obj

    def __init__(self):
        pass


cdef class MyClass(MyBaseClass):
    pass
