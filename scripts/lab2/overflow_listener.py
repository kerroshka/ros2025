cat > overflow_listener.py << 'EOF'
#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(msg):
    rospy.loginfo("Overflow detected! Value: %d", msg.data)

rospy.init_node('overflow_listener')
rospy.Subscriber('overflow_topic', Int32, callback, queue_size=10)
rospy.spin()
EOF