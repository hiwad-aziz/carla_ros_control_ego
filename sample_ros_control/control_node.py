import argparse
import rospy
from ackermann_msgs.msg import AckermannDrive

def control_vehicle(speed, steering_angle):
    publisher = rospy.Publisher('/carla/ego_vehicle/ackermann_cmd', AckermannDrive, queue_size=5)
    rospy.init_node('vehicle_controller', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        ackermann_cmd = AckermannDrive()
        ackermann_cmd.steering_angle = steering_angle
        ackermann_cmd.speed = speed
        publisher.publish(ackermann_cmd)
        rate.sleep()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--steering_angle", default = 0.0, help="steering angle input (rad)")
    parser.add_argument("--speed", default = 5.0, help="speed input (m/s)")
    args = parser.parse_args()
    try:
		control_vehicle(args.speed, args.steering_angle)
    except rospy.ROSInterruptException:
		pass