from sys import platform
from random import randint
from numpy import binary_repr
_a_=platform
 

print(_a_)
print(" Your system supports ipv4,ipv6")
print(" \n Seosh now has 1GB or ipv1048576 ")
print(" \n Seosh is launching 2GB ,4Gb and 8GB simultaneously which this software can handle")
print(" \n Enter the mode you want 1 for ipv4 to ipv1048576,2 for ipv4 to ipv2097152,3 for ipv4 to ipv4194304,4 for ipv4 to ipv8388608 (testing) ")
#_option_=input("\n  : ")
_option=4

#4,6,8,16,32,64,128,256,512,1024,2048
#131072    262144
#1048576 is  1024 MB
#2097152 is  2048 MB
#4194304 is  4096 MB
#8388608 is  8192 MB
if _option_==1:
    print("\n Creating a virtual ipv1Gb which may take time")
    _faa='ipv1048576.bin'
    fo = open(_faa, "w")
    print(" Dumping ipv1048576 to ipv1048576.bin,dont delete this file ")
    for num in range(0,1048577):
   
        fo.write(binary_repr(randint(0, 254), width=8))
        fo.write('.')
    
    print("ipv1048576 or ipv1GB  created,written to file ipv1048576.bin")    
    print(" opening ipv4 ")   
    print(" DHCP enabled") 
    print(" Server found,getting ipv4")
    print(" Bridging ipv4 to ipv1048576")
    print(" ipv4  <=====> ipv1048576  (active,up)")
    print(" Enjoy ")
    fo.close()
elif _option_==2: 
    print("\n Creating a virtual ipv2Gb which may take time")
    _faa='ipv2097152.bin'
    fo = open(_faa, "w")
    print(" Dumping ipv2097152 to ipv2097152.bin,dont delete this file ")
    for num in range(0,2097153):
   
        fo.write(binary_repr(randint(0, 254), width=8))
        fo.write('.')
    
    print("ipv2097152 or ipv2GB  created,written to file ipv2097152.bin")    
    print(" opening ipv4 ")   
    print(" DHCP enabled") 
    print(" Server found,getting ipv4")
    print(" Bridging ipv4 to ipv2097152")
    print(" ipv4  <=====> ipv12097152  (active,up)")
    print(" Enjoy ")
    fo.close() 
elif _option_==3: 
    print("\n Creating a virtual ipv4Gb which may take time")
    _faa='ipv4194304.bin'
    fo = open(_faa, "w")
    print(" Dumping ipv4194304 to ipv4194304.bin,dont delete this file ")
    for num in range(0,4194305):
   
        fo.write(binary_repr(randint(0, 254), width=8))
        fo.write('.')
    
    print("ipv4194304 or ipv4GB  created,written to file ipv4194304.bin")    
    print(" opening ipv4 ")   
    print(" DHCP enabled") 
    print(" Server found,getting ipv4")
    print(" Bridging ipv4 to ipv4194304")
    print(" ipv4  <=====> ipv4194304  (active,up)")
    print(" Enjoy ")
    fo.close() 
elif _option_==4: 
    print("\n Creating a virtual ipv8Gb which may take time")
    _faa='ipv8388608.bin'
    fo = open(_faa, "w")

    _fab='ipv8388608.txt'
    fe= open(_fab, "w")
    print(" Dumping ipv8388608 to ipv8388608.bin,dont delete this file, ip can be seen in ipv8388608.txt")
    for num in range(0,8388609):
        _ab_=randint(0, 254)
        fo.write(binary_repr(_ab_, width=8))
        fo.write('.')
        fe.write(str(_ab_))
        fe.write('.')

    
    print("ipv8388608 or ipv8GB  created,written to file ipv8388608.bin")    
    print(" opening ipv4 ")   
    print(" DHCP enabled") 
    print(" Server found,getting ipv4")
    print(" Bridging ipv4 to ipv8388608")
    print(" ipv4  <=====> ipv8388608  (active,up)")
    print(" Enjoy ")
    fo.close() 
    fe.close()
else :
      print(" \n Wrong mode selected ...")  
      print(" \n Exiting")         





