myfile = open("demofile.txt", "a")
myfile.write("Now the file has more content!")
myfile.close()

#open and read the file after the appending:
myfile = open("demofile.txt", "r")
print(myfile.read())