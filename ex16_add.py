from sys import argv

script, source = argv

txt = open(source)

print "File %s is:" % script
print txt.read()
