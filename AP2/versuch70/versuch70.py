import ocd
import sympy as sy
ex1=ocd.open_csv("ex1.csv")
ex2=ocd.open_csv("ex2.csv")
ex3=ocd.open_csv("ex3.csv")
ex4=ocd.open_csv("ex4.csv")
ex5=ocd.open_csv("ex5.csv")
offsets=ocd.open_csv("offsets.csv")

e_=sy.Symbol("e_")
g_=sy.Symbol("g_")

xb=sy.Symbol("xb")
xs=sy.Symbol("xs")
xa=sy.Symbol("xa")
xl=sy.Symbol("xl")

var=[e_,g_,xb,xs,xa,xl]

e = e_ + xa + xs
g = g_ + xa + xb
b = e - g
beta = b / g
f = g*b/ (g+b)
inner=ur"Experiment I \\ "
inner+=ocd.table_groesse(g,var,ex1+offsets,"g")
inner+=ocd.table_groesse(b,var,ex1+offsets,"b")
inner+=ocd.table_groesse(f,var,ex1+offsets,"f")
inner+=ocd.table_groesse(beta,var,ex1+offsets,ur"beta")
inner+=ur"Experiment II 1. \\ "
inner+=ocd.table_groesse(g,var,ex2+offsets,"g")
inner+=ocd.table_groesse(b,var,ex2+offsets,"b")
inner+=ocd.table_groesse(f,var,ex2+offsets,"f")
inner+=ocd.table_groesse(beta,var,ex2+offsets,ur"beta")
inner+=ur"Experiment II 2. \\ "
inner+=ocd.table_groesse(g,var,ex3+offsets,"g")
inner+=ocd.table_groesse(b,var,ex3+offsets,"b")
inner+=ocd.table_groesse(f,var,ex3+offsets,"f")
inner+=ocd.table_groesse(beta,var,ex3+offsets,ur"beta")
ocd.write_tex(inner)
