import time,os
_faa='a'+'.json'
fo = open(_faa, "w")
_time=str(time.time())
fo.write(_time)
fo.close() 
os.system('notify-send '+_time) 

