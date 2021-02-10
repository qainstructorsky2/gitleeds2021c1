#!/usr/local/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

items = Belgium.split(',')
print('-' * len(Belgium))			    # a)

print(':' . join(items))			    # b)

print(int(items[1]) + int(items[3]))	# c)

print('-' * len(Belgium))			    # d)
