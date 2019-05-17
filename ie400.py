import csv
import numpy as np
from first_fit import first_fit

inputFile = open("bpp_instances.txt", "r")
for line in inputFile:
    data = np.array(line.split(","), dtype = np.int32) 
    print(first_fit(data[1:], data[0]))
inputFile.close()