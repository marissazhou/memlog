import os
import sys 

new_path_lib = sys.path[0]+'/lib'
if new_path_lib not in sys.path:
        sys.path.append(new_path_lib)


#print sys.path
print "**************************************************"

from EventSegmentation import EventSegmentation
	
sensor_path = '/home/marissa/Documents/Autographer_lifelog/marissa_lifelog/2013/12/image_table.txt' 
es = EventSegmentation(1,sensor_path)
