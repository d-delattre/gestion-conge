import numpy as np

class File_modifier:
    def __init__(self):
        self.filename = "./.congé.txt"

    def add_data(self, name, day, month, year, status, length):
        f = open(self.filename, "a")
        f.write(str(name)+";"+str(day)+"/"+str(month)+"/"+str(year)+";"+str(status)+";"+str(length)+"\n")
        f.close()

    def remove_data(self, name, day, month, year, status, length):
        with open(self.filename, "r") as f:
            lines = f.readlines()
        with open(self.filename, "w") as f:
            for line in lines:
                if line.strip("\n") != str(name)+";"+str(day)+"/"+str(month)+"/"+str(year)+";"+str(status)+";"+str(length):
                    f.write(line)

if __name__ == "__main__":
    mod = File_modifier()
    #mod.add_data("DELATTRE","11","01","2023","congé")
    #mod.remove_data("DELATTRE","11","01","2023","congé")
