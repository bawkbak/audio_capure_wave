#!/usr/bin/env python

import rospy
import os
class system_record(object):
    def __init__(self):
        self.node_name = rospy.get_name()
        self.index = 0
    def record(self):
        command = "arecord -D plughw:1 -f S32_LE -c 3 -d 1 record_3channels_{value:d}.wav"
        #print(command.format(value = self.index))
        #rospy.sleep(1)
        now = rospy.get_rostime()
        rospy.loginfo("Current time %i %i", now.secs, now.nsecs)
        os.system(command.format(value = self.index))
        self.index += 1


if __name__ == '__main__':
    rospy.init_node("system_record_wave",anonymous=False)
    audio = system_record()
    while True:
        audio.record()
        if rospy.is_shutdown():
            rospy.sleep(1.5)
            print('finish')
            os.system("pkill arecord")
            rospy.sleep(5)
            break
    
    