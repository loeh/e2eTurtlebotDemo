FROM ros:indigo

# install python dependencies
RUN apt-get update --no-install-recommends
RUN apt-get -yq install --no-install-recommends ros-indigo-joy \
    ros-indigo-turtlebot \
    ros-indigo-hector-sensors-description \
    build-essential \
		git


# Create a new user 'dev' and add it to sudoers
RUN groupadd --gid 1000 dev \
	&& useradd --gid 1000 --uid 1000 --create-home --shell /bin/bash dev \
	&& echo "dev:dev" | chpasswd \
	&& adduser dev sudo

# switch user
USER dev:dev

# Initialize rosdep & create a catkin workspace
RUN rosdep update \
	&& mkdir -p /home/dev/catkin_ws/src && cd /home/dev/catkin_ws/src \
	&& /bin/bash -c "source /opt/ros/indigo/setup.bash && catkin_init_workspace"

# clone the bridge and the bride demo node
RUN git clone https://github.com/gtoff/icclab_turtlebot.git /home/dev/catkin_ws/src/icclab_turtlebot
# RUN git clone https://github.com/tu-darmstadt-ros-pkg/hector_models.git /home/dev/catkin_ws/src/hector_models

# build the bridge
RUN /bin/bash -c '. /opt/ros/indigo/setup.bash; cd /home/dev/catkin_ws/; catkin_make'

# run the bridge
# CMD ["/bin/bash", "-c", "source /home/dev/catkin_ws/devel/setup.bash && roslaunch icclab_turtlebot amcl_icclab.launch map_file:=/home/dev/catkin_ws/src/icclab_turtlebot/icclab_latest_map.yaml"]
