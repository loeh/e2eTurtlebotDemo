#!/usr/bin/env python

import roslib
import rospy
import requests

# import std messages 
from std_msgs.msg import String

baseUrl = 'http://acf7984ae549511e69b640206bb85836-1252824845.eu-central-1.elb.amazonaws.com:5000/orchestrate/api/v1.0/'

def callback(data):
    rospy.loginfo("data: %s", data.data)
    message = data.data.split('/')
    if message[0] == 'closeToBase' and message[1] == 'success':
        rospy.loginfo("successfully reached goal!")
        r = requests.post(baseUrl + 'dock')
    elif message[0] == 'docked' and message[1] == 'success':
        rospy.loginfo("successfully reached docked!")
        r = requests.post(baseUrl + 'docked')
    else:
        rospy.loginfo("not a known event string!")


def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("event", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
