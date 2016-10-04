FROM ros:indigo

# install ros web video server
RUN apt-get update && apt-get install -y ros-indigo-web-video-server

# run the bridge
CMD ["/bin/bash", "-c", "source /opt/ros/indigo/setup.bash && rosrun web_video_server web_video_server"]
