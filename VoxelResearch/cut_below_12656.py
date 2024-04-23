# data starts from index 10
# in python, if you have a range, it goes from [0: to 10] (0 to "not including" 10)
# it's okay to leave the \n inside each cell, just check for Z axis and delete the data
# thislist.pop(1) - method removes the specified index

# NOTE: how to itterate over a list that is SHRINKING
#   try and except: worked like a charm to break it before it breaks me

class MinMaxBoundaries():
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

        self.min_x = float(x)
        self.min_y = float(y)
        self.min_z = float(z)

        self.max_x = float(x)
        self.max_y = float(y)
        self.max_z = float(z)


    def updateMinMaxValues(self, sentence):
        self.updateX(sentence[0])
        self.updateY(sentence[1])
        self.updateZ(sentence[2])

    def updateX(self, value):
        if self.min_x < float(value):self.min_x = float(value)
        if self.max_x > float(value):self.max_x = float(value)

    def updateY(self, value):
        if self.min_y < float(value):self.min_y = float(value)
        if self.max_y > float(value):self.max_y = float(value)

    def updateZ(self, value):
        if self.min_z < float(value):self.min_z = float(value)
        if self.max_z > float(value):self.max_z = float(value)


    def print_results(self):
        print("Min_X: " + str(self.min_x))
        print("Max_X: " + str(self.max_x))

        print("Min_X: " + str(self.min_y))
        print("Max_X: " + str(self.max_y))

        print("Min_X: " + str(self.min_z))
        print("Max_X: " + str(self.max_z))

class MutableInteger:
    def __init__(self, value):
        self.value = value

    def increment(self):
        self.value +=1





# WARNING: it has minmax variable to track min and max values across X,Y,Z
def data_cleanup(read_data, data_length, index, minmax):
    while index.value < data_length:
        try:
            sentence = read_data[index.value]
        except:
            print("index value is :" + str(index.value))
            break
        #-------------------
        # ['-0.8613202263119941', '-0.5589853724099351', '0.9024654115388514', '201', '178', '164\n']
        z_value = sentence.split(" ")[2]

        coords = sentence.split(" ")[:3]
        minmax.updateMinMaxValues(coords)

        # If below this Z-value then it's trash data
        if float(z_value) > 1.265624:
            read_data.pop(index.value)

        index.increment()








with open('colorized.ply', 'r') as f:
    read_data = f.readlines()
    
data_length = len(read_data)
# Skipping through headers at the beginning
index = MutableInteger(10)
print(*read_data[10].split(" ")[:3])
minmax = MinMaxBoundaries(*read_data[10].split(" ")[:3])



data_cleanup(read_data, data_length, index, minmax)

print("total length is :" + str(data_length))
print("current length is:" + str(index.value+1))

# This is the length mentioned in .ply
element_vertex_totalLength = read_data[2].split(" ") 
element_vertex_totalLength[2] = str(index.value-10)+"\n"
read_data[2] = " ".join(element_vertex_totalLength)


minmax.print_results()

with open("filtered.ply", "w") as fout:
    fout.writelines(read_data)

# ===========================
