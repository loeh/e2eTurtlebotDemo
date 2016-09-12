FROM ros:indigo

# install python dependencies
RUN apt-get update && apt-get install -y python-pip git ros-indigo-move-base-msgs

# install bridge dependencies
RUN pip install pika defer kombu eventlet

# Initialize rosdep & create a catkin workspace
RUN rosdep update \
	&& mkdir -p /home/root/catkin_ws/src && cd /home/root/catkin_ws/src \
	&& /bin/bash -c "source /opt/ros/indigo/setup.bash && catkin_init_workspace"

# clone the bridge and the bride demo node
RUN git clone https://furbaz:%40zuri2long@bitbucket.org/rapyutians/rr_cloud_bridge.git /home/root/catkin_ws/src/rr_cloud_bridge
RUN cd /home/root/catkin_ws/src/rr_cloud_bridge; git checkout kombu;

# copy the bride_node with the config in it
COPY bridge_config.yaml /home/root/catkin_ws/src/rr_cloud_bridge/launch/

# build the bridge
RUN /bin/bash -c '. /opt/ros/indigo/setup.bash; cd /home/root/catkin_ws/; catkin_make'
# RUN /bin/bash -c '. /opt/ros/indigo/setup.bash; cd /home/root/catkin_ws/; catkin_make install'

# source setup bash
RUN echo "source /home/root/catkin_ws/devel/setup.bash" >> /home/root/.bashrc

# run the bridge
CMD ["/bin/bash", "-c", "source /home/root/catkin_ws/devel/setup.bash && roslaunch rr_cloud_bridge rr_cloud_bridge.launch"]
