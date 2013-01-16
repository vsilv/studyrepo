#usage: 
# x = open_csv("table1.csv")
# now all the variables are stored in x
import csv 
import errorclass
def open_csv(name,errorfy=False):
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
                                try:
                                        number=float(str(row[k]))
                                        data_[names[k]]+=[number]
                                except:
                                        pass
        if errorfy==False:
                return Bunch(data_)
        else:
                result={}
                variables=[]
                errors=[]
                for k in data_.keys():
                        if k[0]!="S":
                                variables+=[k]
                        else:
                                errors+=[k]
                for k in variables:
                        if "S"+k in errors:
                                result[k]=errorclass.Errorclass(data_[k],data_["S"+k])
                        else:
                                result[k]=data_[k]
                return Bunch(result)





                                



                                
