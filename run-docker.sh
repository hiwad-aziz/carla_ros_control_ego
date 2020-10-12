#! /bin/sh

IMAGE=carla_ros_control:local

SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
SHARED_DOCKER_DIR=/home/carla/shared
SHARED_HOST_DIR=$SCRIPTPATH

docker run -it -P -v ~/carla:/data --rm \
       --name carla \
       --gpus all \
       -e DISPLAY=${DISPLAY} \
       --volume=$SHARED_HOST_DIR:$SHARED_DOCKER_DIR:rw \
       --privileged \
       --network=host \
       --group-add audio \
       $IMAGE


