FROM ros:indigo

# install python dependencies
RUN apt-get update && apt-get install -y ros-indigo-map-server

RUN mkdir -p /home/mapdata/

COPY icclab_latest_map.pgm /home/mapdata/icclab_latest_map.pgm
COPY icclab_latest_map.yaml /home/mapdata/icclab_latest_map.yaml

# run it
CMD ["/bin/bash", "-c", "source /opt/ros/indigo/setup.bash && rosrun map_server map_server /home/mapdata/icclab_latest_map.yaml"]
