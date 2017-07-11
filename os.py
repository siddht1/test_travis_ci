from sys import platform

if platform == "linux":
	print "linux"
elif platform == "linux2":
	print "linux"
    # linux
elif platform == "darwin":
	print "mac os"
    # OS X
elif platform == "win32":
	print"windows 32 bits enviroment"
else:
   print "cannot identify"
    # Windows...
print (sys.version)    
