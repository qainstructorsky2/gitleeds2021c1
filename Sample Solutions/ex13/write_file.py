# coding=utf-8
myfile = open("pelican.txt", "a") # 3
myfile.write('A wonderful bird is the pelican,') # 4
myfile.write('His bill holds more than his belican.') # 5

lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I’m damned if I see how the helican.\n"] #6

myfile.writelines(lines) #7
myfile.close()