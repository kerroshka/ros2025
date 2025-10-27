#!/usr/bin/env python3


import rospy
from std_msgs.msg import Time
import time

def time_node():
    rospy.init_node('time_node', anonymous=True)
    rate = rospy.Rate(0.2)  # 0.2 Hz = каждые 5 секунд
    
    rospy.loginfo("Time node started. Publishing every 5 seconds.")
    
    while not rospy.is_shutdown():
        # Получаем текущее ROS время
        current_time = rospy.Time.now()
        
        # Выводим время
        rospy.loginfo("Current ROS time: %s", current_time)
        
        rate.sleep()


if __name__ == '__main__':
    try:
        time_node()
    except rospy.ROSInterruptException:
        pass