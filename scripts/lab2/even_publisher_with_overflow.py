cat > even_publisher_with_overflow.py << 'EOF'
#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node('even_publisher')
pub_even = rospy.Publisher('even_numbers', Int32, queue_size=10)
pub_overflow = rospy.Publisher('overflow_topic', Int32, queue_size=10)
rate = rospy.Rate(10)
count = 0

while not rospy.is_shutdown():
    if count <= 100:
        pub_even.publish(count)
        rospy.loginfo("Published even: %d", count)
        count += 2
    else:
        pub_overflow.publish(count)
        rospy.loginfo("Overflow! Published: %d", count)
        count = 0
    rate.sleep()
EOF