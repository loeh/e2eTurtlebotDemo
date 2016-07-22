salt turtlebot.robonet cmd.run_bg "source /opt/ros/indigo/setup.bash && source ~/catkin_ws/devel/setup.bash && source ~/turtlebot/devel/setup.bash && export ROS_MASTER_URI=http://turtlebot:11311 && export ROS_HOSTNAME=turtlebot && roslaunch icclab_turtlebot amcl_icclab.launch map_file:=/home/turtlebot/catkin_ws/src/icclab_turtlebot/icclab_latest_map.yaml" runas=turtlebot shell="/bin/bash" cwd="/home/turtlebot"

salt turtlebot.robonet cmd.run_bg "source /opt/ros/indigo/setup.bash && source ~/catkin_ws/devel/setup.bash && source ~/turtlebot/devel/setup.bash && export ROS_MASTER_URI=http://turtlebot:11311 && export ROS_HOSTNAME=turtlebot && roslaunch icclab_turtlebot minimal_with_rplidar.launch" runas=turtlebot shell="/bin/bash" cwd="/home/turtlebot"

### start amcl through API
curl -si http://ab44513583e1711e6b0ef02e4cf15b02-1319127330.eu-central-1.elb.amazonaws.com:8001 -H "Accept: application/json" -H "X-Auth-Token: d295ef89ce7a6a88813781e1680ebc5ffe755d82" -d client=local -d tgt='*' -d fun=cmd.run -d arg='source /opt/ros/indigo/setup.bash && source ~/catkin_ws/devel/setup.bash && source ~/turtlebot/devel/setup.bash && export ROS_MASTER_URI=http://turtlebot:11311 && export ROS_HOSTNAME=turtlebot && roslaunch icclab_turtlebot amcl_icclab.launch map_file:=/home/turtlebot/catkin_ws/src/icclab_turtlebot/icclab_latest_map.yaml'

### start minimal through API
curl -si http://ab44513583e1711e6b0ef02e4cf15b02-1319127330.eu-central-1.elb.amazonaws.com:8001 -H "Accept: application/json" -H "X-Auth-Token: ec9fa66e69a83a6dead3c4d4c0335c040a8adf1a" -d client=local -d tgt='*' -d fun=cmd.run -d shell=/bin/bash  -d arg='source /opt/ros/indigo/setup.bash' -d arg='source ~/catkin_ws/devel/setup.bash' -d arg='source ~/turtlebot/devel/setup.bash' -d arg='roslaunch icclab_turtlebot minimal_with_rplidar.launch'


-d arg='export ROS_MASTER_URI%3Dhttp%3A%2F%2Fturtlebot%3A11311' -d arg='export ROS_HOSTNAME%3Dturtlebot'

curl -si http://ab44513583e1711e6b0ef02e4cf15b02-1319127330.eu-central-1.elb.amazonaws.com:8001 -H "Accept: application/json" -H "X-Auth-Token: ebc7630d592a1ff7f0ac3552631ec079fa4fedd3" -d client=local -d cwd="/home/turtlebot" -d runas=turtlebot -d tgt='*' -d fun=cmd.run -d shell=/bin/bash -d env='ROS_MASTER_URI=http://turtlebot:11311' -d env='export ROS_HOSTNAME=turtlebot' -d arg='source /opt/ros/indigo/setup.bash'  -d arg='source ~/catkin_ws/devel/setup.bash' -d arg='source ~/turtlebot/devel/setup.bash' -d arg='roslaunch icclab_turtlebot minimal_with_rplidar.launch'


### Run meow
salt turtlebot.robonet cmd.run '/opt/ros/indigo/share/rocon_apps/chirp.bash /opt/ros/share/rocon_apps/sounds/meow.wav 90' runas=turtlebot shell="/bin/bash"  cwd="/home/turtlebot"

### Get token
curl -si http://ab44513583e1711e6b0ef02e4cf15b02-1319127330.eu-central-1.elb.amazonaws.com:8001/login -H "Accept: application/json" -d username='roboreg' -d password='splab' -d eauth=pam

### Meow through API
curl -si http://ab44513583e1711e6b0ef02e4cf15b02-1319127330.eu-central-1.elb.amazonaws.com:8001 -H "Accept: application/json" -H "X-Auth-Token: ebc7630d592a1ff7f0ac3552631ec079fa4fedd3" -d client=local -d tgt='*' -d fun=cmd.run -d arg='/opt/ros/indigo/share/rocon_apps/chirp.bash /opt/ros/indigo/share/rocon_apps/sounds/meow.wav 90'
