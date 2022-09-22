#!/user/bin/env python

import rospy
from std_msgs.msg import String

print('node ready to subcribe to data ')

def callback(msg):
    print msg.data
subscriber=rospy.Subscriber('topicPublisher',String,callback)

rospy.init_node("Tx_topic_subscriber")
rospy.spin()