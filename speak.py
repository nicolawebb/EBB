#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

data = {}

keygaze = "gaze"
data.setdefault(keygaze, [])
keycamb = "camera_botom"
data.setdefault(keycamb, [])
keycamt = "camera_top"
data.setdefault(keycamt, [])
keylg = "left_gripper"
data.setdefault(keylg, [])
keyrg = "right_griper"
data.setdefault(keyrg, [])

def talker():
    pub = rospy.Publisher('robotdata', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        data["gaze"] = "1"
        data["camera_botom"] = "23"
        data["camera_top"] = "234"
        data["left_gripper"] = "9560"
        data["right_griper"] = "546985406"
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass