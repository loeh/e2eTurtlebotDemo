FROM ros:indigo

# install rosbridge server
RUN apt-get update && apt-get install -y ros-indigo-robot-pose-publisher

# run the pose publisher
CMD ["/bin/bash", "-c", "source /opt/ros/indigo/setup.bash && rosrun robot_pose_publisher robot_pose_publisher"]
