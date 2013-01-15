from General import *
import math

class Cos(MathObject):
    def __init__(self, inner):
        self.inner = inner
    def eval(self, **vars):
        return math.cos(self.inner.eval(**vars))
    def str(self, context=C_PARENTH):
        return "cos(" + self.inner.str(C_PARENTH) + ")"
    def latex(self, context=C_PARENTH):
        return "\\cos\\left(" + self.inner.latex(C_PARENTH) + "\\right)"
    
    def derivate(self, var):
        if self.inner.dependsOn(var):
            if type(self.inner) == Variable:
                return Sin(self.inner)
            else:
                return Product[Sin(self.inner), self.inner.derivate(var)]
            
        
        
class Sin(MathObject):
    def __init__(self, inner):
        self.inner = inner
    def eval(self, **vars):
        return math.sin(self.inner.eval(**vars))
    def str(self, context=C_PARENTH):
        return "sin(" + self.inner.str(C_PARENTH) + ")"
    def latex(self, context=C_PARENTH):
        return "\\sin\\left(" + self.inner.latex(C_PARENTH) + "\\right)"
    
