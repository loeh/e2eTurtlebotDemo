## start the navigation on a web map
 
-> on the turtlebot:
	- start minimal
	- start amcl with the map and the starting position


-> on the laptop:
	- rosrun robot_pose_publisher robot_pose_publisher
	- roslaunch rosbridge_server rosbridge_websocket.launch
	- e.g. rviz to see what is going on
	- open up nav.html to view
	- double click to navigate the robot


## published data on /move_base/goal

header: 
  seq: 10
  stamp: 
    secs: 0
    nsecs:         0
  frame_id: ''
goal_id: 
  stamp: 
    secs: 0
    nsecs:         0
  id: goal_0.7165642235833299_1469115779284
goal: 
  target_pose: 
    header: 
      seq: 0
      stamp: 
        secs: 1469115779
        nsecs: 285305023
      frame_id: /map
    pose: 
      position: 
        x: -5.89422206865
        y: 1.8372151191
        z: 0.0
      orientation: 
        x: 0.0
        y: 0.0
        z: 0.0
        w: 1.0

