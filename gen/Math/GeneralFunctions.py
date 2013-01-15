
from General import *
import math

class Sum(MathObject):
    def __init__(self, summands=[], subtrahends=[]):
        self.summands   = summands
        self.subtrahends = subtrahends
    
    def addSummand(self, funct):
        self.summands.append(funct)
        
    def addSubtrahend(self, funct):
        self.subtrahends.append(funct)
    
    def eval(self, **vars):
        sum=0
        for summand in self.summands:
            sum += summand.eval(**vars)
        for subtrahend in self.subtrahends:
            sum -= subtrahend.eval(**vars)
        return sum
    def str(self, context=C_PARENTH):
        str = ""
        if context > C_SUM:  str += "("
        str += self.summands[0].str(C_SUM)
        for term in self.summands[1:]:
            str += " + " + term.str()
        for term in self.subtrahends:
            str += " - " + term.str(C_SUM)
        if context > C_SUM:  str += ")"
        return str
    
    def latex(self, context=C_PARENTH):
        str = ""
        if context > C_SUM:  str += "\\left("
        str += self.summands[0].latex()
        for term in self.summands[1:]:
            str += " + " + term.latex(C_SUM)
        for term in self.subtrahends:
            str += " - " + term.latex(C_SUM)
        if context > C_SUM:  str += "\\right)"
        return str
            
            
        

class Product(MathObject):
    def __init__(self, factors=[], divisors=[]):
        self.factors   = factors
        self.divisors  = divisors
    
    def addFactor(self, funct):
        self.factors.append(funct)
        
    def addDivisor(self, funct):
        self.divisors.append(funct)
    
    def eval(self, **vars):
        prod=1
        for factor in self.factors:
            prod *= factor.eval(**vars)
        for divisor in self.divisors:
            prod *= divisor.eval(**vars)
        return prod
    
    def str(self, context=C_PARENTH):
        str = ""
        if context > C_PRODUCT:  str += "("
        str += self.factors[0].str(C_PRODUCT)
        for term in self.factors[1:]:
            str += " * " + term.str(C_PRODUCT)
        if str == "": str = "1"
        
        for term in self.divisors:
            str += " / "
            str +=  term.str(C_DIVISOR)

        if context > C_PRODUCT:  str += ")"
        return str
    
    def latex(self, context=C_PARENTH):
        
        fraction = (len(self.divisors) > 0)       
        if fraction:
            chieldContext = C_PARENTH
        else:
            chieldContext = C_PRODUCT
        
        numerator = ""
        for term in self.factors:
            numerator += " " + term.latex(chieldContext)
        if numerator == "": numerator = "1"
        
        denominator = ""
        for term in self.divisors:
            denominator += " " + term.latex(chieldContext)
 
        str = ""
        if context>C_DIVISOR: str = "\\left("
        
        if not fraction:
            str += numerator
        else:
            str += "\\frac{" + numerator + "}{" + denominator + "}"
        if context>C_DIVISOR: str += "\\right)"
        
        return str    

class Minus(MathObject):
    def __init__(self, funct):
        self.inner = funct
    def eval(self, **vars):
        return -self.inner.eval(**vars)
    def str(self, context=C_PARENTH):
        if context > C_PARENTH:
            return "(-" + self.inner.str(C_MINUS) + ")"
        else:
            return "-" + self.inner.str(C_MINUS) 
    def latex(self, context=C_PARENTH):
        if context > C_PARENTH:
            return "\\left(-" + self.inner.latex(C_MINUS) + "\\right)"
        else:
            return "-" + self.latex.str(C_MINUS) 

class OneOver(MathObject):
    def __init__(self, funct):
        self.inner = funct
    def eval(self, **vars):
        return 1/self.inner.eval(**vars)
    def str(self, context=C_PARENTH):
        if context > C_DIVISOR:
            return "(1/" + self.inner.str(C_DIVISOR) + ")"
        else:
            return "1/" + self.inner.str(C_DIVISOR) 
    def latex(self, context=C_PARENTH):
        if context > C_DIVISOR:
            return "\\left(\\frac{1}{" + self.inner.latex(C_DIVISOR) + "}\\right)"
        else:
            return "(\\frac{1}{" + self.inner.latex(C_DIVISOR) + "})"
   
class Sqrt(MathObject):
    def __init__(self, funct):
        self.inner = funct
    def eval(self, **vars):
        return math.sqrt(self.inner.eval(**vars))
    def str(self, context=C_PARENTH):
        return "sqrt(" + self.inner.str(C_PARENTH) + ")"
    def latex(self):
        return "\\sqrt{" + self.inner.latex(C_PARENTH) + "}"
     
     
class Log(MathObject):
    def __init__(self, funct, base=Number(10)):
        self.inner = funct
        self.base  = base
    def eval(self, **vars):
        return math.log(self.inner.eval(**vars), self.base.eval(**vars))
    def str(self, contex=C_PARENTH):
         if self.base == Number(10):
             return "log(" + self.inner.str(C_PARENTH) + ")"
         else:
             return "log(" + self.inner.str(C_PARENTH) + ", " + self.base.str() + ")"
    def latex(self, context=C_PARENTH):
         if self.base == Number(10):
             return "\\log \left(" + self.inner.latex(C_PARENTH) + "\\right)"
         else:
             return "\\log_{" + self.base.latex(C_PARENTH) + "} \left(" + self.inner.latex(C_PARENTH) +  "\\right)" 
                 
class Ln(MathObject):
    def __init__(self, funct):
        self.inner = funct
    def eval(self, **vars):
        return math.log(self.inner.eval(**vars))
    def str(self, context=C_PARENTH):
         return "ln(" + self.inner.str(C_PARENTH) + ")"
    def latex(self, context=C_PARENTH):
         return "\\ln \left(" + self.inner.latex(C_PARENTH) + "\\right)"
    
class Root(MathObject):
    def __init__(self, n, funct):
        self.inner  = funct
        self.n      = n
    def eval(self, **vars):
        return math.pow(self.inner.eval(**vars), OneOver(self.n).eval(**vars))
    def str(self, context=C_PARENTH):
         return "root(" + self.n.str(C_PARENTH) + ", " + self.inner.str(C_PARENTH) + ")"
    def latex(self, context=C_PARENTH):
         return "\\sqrt[" +  self.n.latex(C_PARENTH) + "]{" + self.inner.latex(C_PARENTH) + "}"
        
class Pow(MathObject):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def eval(self, **vars):
        return math.pow(self.x.eval(**vars), self.y.eval(**vars))
    def str(self, context=C_PARENTH):
        if context>C_DIVISOR:
            return "(" + self.x.str(C_POWER) + "^" +  self.y.str(C_POWER) + ")"
        else:
            return self.x.str(C_POWER) + "^" +  self.y.str(C_POWER)
    def latex(self, context=C_PARENTH):
        if context>C_DIVISOR:
            return "\\left(" + self.x.latex(C_POWER) + "^{" + self.y.latex(C_PARENTH) + "}\\right)"
        else:
            return  self.x.latex(C_POWER) + "^{" + self.y.latex(C_PARENTH) + "}"
     
class Square(MathObject):
    def __init__(self, x):
        self.x = x
    def eval(self, **vars):
        return math.pow(self.x.eval(**vars), 2)
    def str(self, context=C_PARENTH):
        if context>C_DIVISOR:
            return "(" + self.x.str(C_POWER) + "^2)"
        else:
            return self.x.str(C_POWER) + "^2"
        
    def latex(self, context=C_PARENTH):
        if context > C_DIVISOR:
            return "\\left(" + self.x.latex(C_POWER) + "^2\\right)"
        else:
            return "" + self.x.latex(C_POWER) + "^2"
        

class Exp(MathObject):
    def __init__(self, funct):
        self.inner = funct
    def eval(self, **vars):
        return math.exp(self.inner.eval(**vars))
    def str(self, context=C_PARENTH):
         return "exp(" + self.inner.str(C_PARENTH) + ")"  
    
    def latex(self, context=C_PARENTH):
         return "e^{" + self.inner.latex(C_PARENTH) + "}"    

