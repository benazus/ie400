import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

prompt = ""
write = ""
file = open("bpp_instances.txt", "a")

while prompt not in ["n", "N", "No", "no", "NO"]:
    w = np.random.randint(75, 150, size = 30)
    c = np.random.randint(50, 74, size = 1)
    data = np.hstack((c, w))
    dataToStr = np.array2string(data, separator=', ')
    print(dataToStr)
    write = input("Save? ")

    if write in ["y", "Y", "Yes", "yes", "YES"]:
        file.write((dataToStr + "\n").replace("[", "").replace("]", "").replace(" ", ""))

    prompt = input("Continue? ")
file.close()