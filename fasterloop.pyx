
cpdef int faster_for_loop(int init, int end):
    cdef int i
    for i in range(init+1, end+1):
        print(i)
