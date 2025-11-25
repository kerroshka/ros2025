cat > even_publisher.py << 'EOF'
#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node('even_publisher')
pub = rospy.Publisher('even_numbers', Int32, queue_size=10)
rate = rospy.Rate(10)  # 10 Гц
count = 0

while not rospy.is_shutdown():
    pub.publish(count)
    rospy.loginfo("Published: %d", count)
    count += 2
    rate.sleep()
EOF