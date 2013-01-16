#usage: 
# x = open_csv("table1.csv")
# now all the variables are stored in x
import numpy as np
import csv 
from errorclass import *
def open_csv(name):
        class Bunch(object):
          def __init__(self, adict):
            self.__dict__.update(adict)
        data_={}
        with open(name,"rb") as csvfile:
                data= csv.reader(csvfile, delimiter=",", quotechar="|")
                names=data.next()
                for k in names:
                        data_[k]=[]
                for row in data:
                        for k in xrange(len(row)):
                                data_[names[k]]+=[row[k]]
        return Bunch(data_)
def open_csv_errors(name):
	pass

                                
