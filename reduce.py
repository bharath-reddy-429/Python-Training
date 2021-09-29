#add all the elements in list using reduce
from functools import *
l=[10,20,30,40,50]
print(reduce(lambda x,y:x+y,l))
