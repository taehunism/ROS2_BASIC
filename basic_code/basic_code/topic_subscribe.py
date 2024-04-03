#!/usr/bin/env python3 
import rclpy
from rclpy.node import Node 
from rclpy.qos import QoSProfile
from std_msgs.msg import String 

class Topic_Subscriber(Node):
    def __init__(self):
        super().__init__('topic_sub')
        qos_profile = QoSProfile(depth=10)
        self.topic_subscriber = self.create_subscription(String, 'topic_count', self.sub_callback,qos_profile)

    def sub_callback(self, msg):
        self.get_logger().info(f'Sub msg : {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = Topic_Subscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info(f'Keyboard Interrupt')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()