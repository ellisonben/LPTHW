from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third varable is:", third
raw_data = raw_input("say something: ")
print "You said %r" % raw_data
