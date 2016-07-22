#!/usr/bin/env python

import roslib;
import rospy
import actionlib
import sys

#move_base_msgs
from move_base_msgs.msg import *

def simple_move(move_position):

    rospy.init_node('simple_move')

    #Simple Action Client
    sac = actionlib.SimpleActionClient('move_base', MoveBaseAction )

    #create goal
    goal = MoveBaseGoal()

    #set goal
    goal.target_pose.pose.position.x = move_position[0]
    goal.target_pose.pose.position.y = move_position[1]
    goal.target_pose.pose.orientation.z = move_position[2]
    goal.target_pose.pose.orientation.w = move_position[3]
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.header.stamp = rospy.Time.now()

    #start listner
    sac.wait_for_server()

    #send goal
    sac.send_goal(goal)

    #finish
    sac.wait_for_result()

    #print result
    print sac.get_result()


if __name__ == '__main__':
    try:
	away_pos = [-0.536414086819, 0.492057323456, 0.992841611677, 0.119438411419]
	home_pos = [-5.86358213425, 2.0202703476, 0.999910191108, -0.0134018550249]
	if sys.argv[1] == 'home':	
        	simple_move(home_pos)
	elif sys.argv[1] == 'away':
		simple_move(away_pos)
	else:
		print 'use home or away'
	
    except rospy.ROSInterruptException:
        print "Keyboard Interrupt"
