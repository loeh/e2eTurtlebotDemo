FROM ros:indigo

# install rosbridge server
RUN apt-get update && apt-get install -y ros-indigo-rosbridge-server ros-indigo-move-base-msgs

# run the bridge
CMD ["/bin/bash", "-c", "source /opt/ros/indigo/setup.bash && roslaunch rosbridge_server rosbridge_websocket.launch"]
