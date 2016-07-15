FROM ros:indigo

RUN apt-get update

# install git
RUN apt-get install git

# install python dependencies
RUN apt-get install -y python-pip

# install bridge dependencies
RUN pip install pika defer

# Now create the ros user
RUN adduser --gecos "ROS User" --disabled-password ros

USER ros

# HOME needs to be set explicitly. Without it, the HOME environment variable is
# set to "/"
RUN HOME=/home/ros rosdep update

# create workspace folder
RUN mkdir -p /home/ros/workspace/src

# create the catkin workspace
RUN /bin/bash -c '. /opt/ros/indigo/setup.bash; catkin_init_workspace /home/ros/workspace/src'

# clone the bridge and the bride demo node
RUN cd /home/ros/workspace/src
USER root
RUN git clone https://furbaz:%40zuri2long@bitbucket.org/rapyutians/rr_cloud_bridge.git
RUN git clone https://furbaz:%40zuri2long@bitbucket.org/rapyutians/rr_cloud_demo.git

# copy the bride_node with the config in it
COPY ./bridge_node.py /home/ros/workspace/src/rr_cloud_demo/src/rr_cloud_demo/bridge_node.py

USER ros
# build the bridge
RUN /bin/bash -c '. /opt/ros/indigo/setup.bash; cd /home/ros/workspace; catkin_make'
RUN /bin/bash -c '. /opt/ros/indigo/setup.bash; cd /home/ros/workspace; catkin_make install'

# source setup bash
RUN echo "source ~/workspace/devel/setup.bash" >> /home/ros/.bashrc
RUN /bin/bash -c 'source /home/ros/workspace/devel/setup.bash'


# run the bridge
CMD ["/bin/bash", "-c", "rosrun rr_cloud_demo bridge_node.py"]
