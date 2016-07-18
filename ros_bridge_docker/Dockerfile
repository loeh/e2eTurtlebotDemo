FROM ros:indigo

# install python dependencies
RUN apt-get update && apt-get install -y python-pip && apt-get install -y git

# install bridge dependencies
RUN pip install pika defer

# Create a new user 'dev' and add it to sudoers
RUN groupadd --gid 1000 dev \
	&& useradd --gid 1000 --uid 1000 --create-home --shell /bin/bash dev \
	&& echo "dev:dev" | chpasswd \
	&& adduser dev sudo

# switch user
USER dev:dev

# Initialize rosdep & create a catkin workspace
RUN rosdep update \
	&& mkdir -p ~/catkin_ws/src && cd ~/catkin_ws/src \
	&& /bin/bash -c "source /opt/ros/indigo/setup.bash && catkin_init_workspace"

# clone the bridge and the bride demo node
RUN git clone https://furbaz:%40zuri2long@bitbucket.org/rapyutians/rr_cloud_bridge.git ~/catkin_ws/src/rr_cloud_bridge
RUN cd ~/catkin_ws/src/rr_cloud_bridge; git checkout review_async;
RUN git clone https://furbaz:%40zuri2long@bitbucket.org/rapyutians/rr_cloud_demo.git ~/catkin_ws/src/rr_cloud_demo

# copy the bride_node with the config in it
COPY ./bridge_node.py ~/catkin_ws/src/rr_cloud_demo/src/rr_cloud_demo/bridge_node.py

# build the bridge
RUN /bin/bash -c '. /opt/ros/indigo/setup.bash; cd ~/catkin_ws/; catkin_make'
# RUN /bin/bash -c '. /opt/ros/indigo/setup.bash; cd ~/catkin_ws/; catkin_make install'

# source setup bash
RUN echo "source ~/catking_ws/devel/setup.bash" >> /home/dev/.bashrc

# run the bridge
CMD ["/bin/bash", "-c", "source ~/catking_ws/devel/setup.bash && roscore"]
