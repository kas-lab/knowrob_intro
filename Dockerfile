FROM ghcr.io/rezenders/knowrob_docker:main

COPY . /knowrob_ws/src/knowrob_intro
WORKDIR /knowrob_ws
RUN ["/bin/bash", "-c", "source /opt/ros/noetic/setup.bash && catkin_make"]
