import time
import os

list = os.listdir("/home/skb/Downloads/Walls")
for i in list:
	print i
	time.sleep(1)
	os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:/home/skb/Downloads/Walls/"+i)

##print list[3], time.clock()
