import fileinput
import pickle

fh = open("./mydata/saveFile.pickle", "wb")

pickle.dump("Hello Pickle!!!", fh)
fh.close()

fileObj = open("./mydata/saveFile.pickle", "rb")
data = pickle.load(fileObj)
print(data)
fileObj.close()