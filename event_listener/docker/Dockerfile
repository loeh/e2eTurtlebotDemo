FROM ros:indigo

# install rosbridge server
RUN apt-get update && apt-get install -y python-pip git

RUN pip install requests

# Initialize rosdep & create a catkin workspace
RUN rosdep update \
	&& mkdir -p /home/root/catkin_ws/src && cd /home/root/catkin_ws/src \
	&& /bin/bash -c "source /opt/ros/indigo/setup.bash && catkin_init_workspace"

# clone the bridge and the bride demo node
RUN git clone https://github.com/loeh/e2eTurtlebotDemo.git /home/root/catkin_ws/src/e2eTurtlebotDemo

# copy the eventListener to src
RUN cd /home/root/catkin_ws/src/e2eTurtlebotDemo && mv event_listener/ /home/root/catkin_ws/src/
RUN cd /home/root/catkin_ws/src && rm -r /home/root/catkin_ws/src/e2eTurtlebotDemo

# build it
RUN /bin/bash -c '. /opt/ros/indigo/setup.bash; cd /home/root/catkin_ws/; catkin_make'
RUN /bin/bash -c '. /opt/ros/indigo/setup.bash; cd /home/root/catkin_ws/; catkin_make install'

# source setup bash
RUN echo "source /home/root/catkin_ws/devel/setup.bash" >> /home/root/.bashrc

# run the bridge
CMD ["/bin/bash", "-c", "source /home/root/catkin_ws/devel/setup.bash && rosrun event_listener event_listener.py"]
