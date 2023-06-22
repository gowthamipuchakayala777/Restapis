#  write a python program which will accept list of values and find their sum and avg using function

def readvalues():
    lst=[]
    n=int(input("Enter how many values you want to enter:"))
    if(n<=0):
        return lst
    else:
        for i in range(1,n+1):
            val=float(input("Enter{} value:".format(i)))
            lst.append(val)
        return lst

def findsumavg(gvrlst):
    if(len(gvrlst)==0):
        print("list is empty and cannot find sum and avg:")
    else:
        s=0
        for val in gvrlst:
            s=s+val
        else:
            print("Given list of elements:{}".format(gvrlst))
            print("sum:{}".format(s))
            print("average:{}".format(s/len(gvrlst)))
# main program
lst=readvalues()
findsumavg(lst)