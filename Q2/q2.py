import numpy as np
from numpy import array, dot
from numpy.linalg import norm

def Cos(Doc, Query):
    return dot(Doc, Query) / (norm(Doc)*norm(Query))

def main() -> int:
    Docs = array([[1,1,0,1,0,1],[1,1,1,0,1,0],[1,1,0,1,0,0]])
    Query = array([1,1,0,0,1,0])
    for index, doc in enumerate(Docs):
        print('doc{0}={1:.2f}'.format(index + 1,Cos(doc, Query)))

# entry point of program
if __name__ == '__main__':
    main()
