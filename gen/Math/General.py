# Contexts
C_LINE      = -2
C_PARENTH     = 0
C_SUM       = 1
C_MINUS     = 1.5
C_PRODUCT   = 2
C_DIVISOR   = 2.5
C_POWER     = 3

class MathException():
    def __init__(self, data):
        self.data = data
       

        
class NoNumericalValueFound(MathException):
    def repr(self):
        return "No numerical value for variable " + self.data + " found."
    
class MathObject:
    def __init__(self):
        self.space = ParameterSpace()
    def eval(vars):
        pass
    def str(self, context=0):
        pass
    def latex(self, context=0):
        pass
    def simplify(self):
        pass
    def dependsOn(self, var):
        pass
    def derivate(self, var):
     	raise NotImplementedError() 
    """
	plug in some values, no ness. all, so the resulting term depends on less vars
    """

    def reduce(self, vars):
	pass
      
      
class Number(MathObject):
    def e():
        return Number(math.e)
    def pi():
        return Number(math.pi)
    
    def __init__(self, number):
        self.number = number
    def eval(self, **vars):
        return self.number
    def str(self, context=C_PARENTH):
        return str(self.number).replace(".", ",")
    def latex(self, context=C_PARENTH):
        return str(self.number).replace(".", ",")
    
class Function(MathObject):

    def __init__(self, name, argumentSet, inner):
        self.name  = name
        self.inner = inner
        self.argumentSet = argumentSet
    
    def eval(self, vars):
        self.inner = vars
    
    def call(self, *arguments):
        vars = dict(zip(self.argumentSet, arguments))
        return self.inner.eval(**vars)
        
    def derivate():
        pass
    def str(self, context=C_LINE):
        args = ""
        if len(self.argumentSet) > 0:
            args = self.argumentSet[0]
            for arg in self.argumentSet[1:]:
                args += ", " + arg
        if context == C_LINE:
            return self.name  + "(" + args + ") = " + self.inner.str()
        else:
            return self.name  + "(" + args + ") "
        
    def latex(self, context= C_LINE):
        args = ""
        if len(self.argumentSet) > 0:
            args = self.argumentSet[0]
            for arg in self.argumentSet[1:]:
                args += ", " + arg
        if context == C_LINE:
            return "\\textrm{" + self.name + "}" + "(" + args + ") = " + self.inner.latex()      
        else:
            return "\\textrm{" + self.name + "}" + "(" + args + ")" 
      
      
    def derivate(self, var):
        return self.inner.derivate(var)

class Variable(MathObject):
    def __init__(self, name):
        self.name = name
    def eval(self, **vars):
        if self.name in vars.keys():
            return vars[self.name]
        else:
            raise NoNumericalValueFound(self.name)
    def str(self, context=C_PARENTH):
        return self.name
    def latex(self, context=C_PARENTH):
        return self.name
    
    def dependsOn(self, var):
        return  var == self.name
