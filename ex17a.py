from sys import argv

script, from_file, to_file = argv
#this copies the from_file to the to_file
open(to_file, 'w').write(open(from_file).read())
