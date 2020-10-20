import numpy
import matplotlib
import pandas
#import scikit-learn
from dask.array import learn
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

n=70809
p=46090
if p>2*n:
        print("0")
else:
    if p==1:
        print("0")
    elif p%2==0:
        print(p//2)
    else:
        print((p-1)//2)