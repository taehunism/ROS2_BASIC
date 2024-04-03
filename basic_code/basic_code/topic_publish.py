#!/usr/bin/env python3 
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String

class Topic_Publisher(Node):
    def __init__(self):
        super().__init__('topic_pub')
        qos_profile = QoSProfile(depth=10)
        self.topic_publisher = self.create_publisher(String, 'topic_count', qos_profile)
        self.timer = self.create_timer(1, self.pub_callback)
        self.count = 0

    def pub_callback(self):
        msg = String()
        msg.data = f'Hi this is Topic publish code : {self.count}'
        self.topic_publisher.publish(msg)
        self.get_logger().info(f'Published msg : {self.count}')
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = Topic_Publisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger.info(f'Keyboard Interrupt')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()