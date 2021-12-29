import numpy
def rot():
    I = numpy.identity(3,dtype=int)
    for x in 1,-1:
        for y in 1,-1:
            for z in 1,-1:
                for p in [
                    [0,1,2],
                    [0,2,1],
                    [1,0,2],
                    [1,2,0],
                    [2,0,1],
                    [2,1,0],
                ]
                if numpy.linalg.det(m[:,p] * [x,y,z]) > 0.5
                yield p,[x,y,z]


for m in rot():
    print(m, numpy.linalg.det(m))
