# CARLA - control ego vehicle using ROS
A simple docker environment and python ROS node to control the ego vehicle in the CARLA simulator. The repository is intended to give an overview of how it works and to get familiar with CARLA and controlling it with ROS messages.

## Usage

 - Build the docker environment with following command:
	  `docker build --tag carla_ros_control:local`
 - Run the docker image:
	  `bash /home/carla/shared/run-docker.sh`
 - Launch the CARLA simulator.
 - Launch all the dependencies (CARLA ROS bridge, ego vehicle, manual control) using the provided launch script:
	  `roslaunch /home/carla/shared/sample_ros_control/carla_ros_dep.launch`
	  
 - Run the provided Python script to control the ego vehicle's speed and steering angle.
	  `python /home/carla/shared/sample_ros_control/control_node.py`
	  This will create a ROS node that uses Ackermann control messages to set the speed and steering angle of the 			ego vehicle. Default values are:
	  
	 - speed: 5.0 m/s
	 - steering angle: 0.0 rad
	 
	 You can pass in your own desired values using the `--speed` and `--steering_angle` arguments of the provided Python script.

