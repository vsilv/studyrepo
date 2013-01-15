

from General                   import *
from GeneralFunctions          import *
from TrigonometricFunctions    import *

if __name__ == "__main__":
    x = Variable("x")
    s = Square(x)

    f = Function("f", ['x'], Pow(Sum([Product( [Sum([s], [x])], [Number(5)] ), s ] ), Sum([x, Number(2)])) )

    print(f.str())
    print(f.latex())
    
    print(f.call(5))
    
    print(Cos(x).eval(x=5))
    
    print(Cos(x).derivate('x').str())
    
    
    
    