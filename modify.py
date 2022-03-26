import sys
fileSpec = sys.argv[1]		# read file name first argument
searchText = sys.argv[2]	# text to search for
replaceText = sys.argv[3]	# text to replace with

outFile = fileSpec + '.new'	# write file = read file with .new appended
outPointer = open(outFile,'w')	# open write file
inPointer = open(fileSpec, 'r')	# open read file
for line in inPointer:
    outPointer.write(line.replace(searchText, replaceText))

inPointer.close()
outPointer.close()