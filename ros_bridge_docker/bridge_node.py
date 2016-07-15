#!/usr/bin/env python

import os
from rr_cloud_bridge import Bridge
import rospy

if __name__ == '__main__':
	config = {
		'host': os.environ['CLOUD_BROKER_HOST'], 
		'broker_user': 'rapyuta_robotics',
		'broker_passwd': 'ECRP_KTI_project',
		'topics': ['/move_base_simple/goal'],
		'services': []
	}
	bridge = Bridge(config)
	print "Bridge is up ..."
	bridge.run()
