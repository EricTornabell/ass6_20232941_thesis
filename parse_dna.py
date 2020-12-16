import sys

parameters = sys.argv

with open(parameters[1],'r') as infile:
   sequence = infile.read().strip()

print (sequence[int(parameters[2]):])


