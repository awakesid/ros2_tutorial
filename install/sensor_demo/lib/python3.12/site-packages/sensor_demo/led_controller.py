#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Bool

class LEDController(Node):
    def __init__(self):
        super().__init__('led_controller')
        self.subscription = self.create_subscription(
            Float32,
            '/distance',
            self.distance_callback,
            10)
        self.publisher = self.create_publisher(Bool, '/led_command', 10)
        self.threshold = 0.2  # 20 cm (customize this)
        self.get_logger().info("LED controller ready!")

    def distance_callback(self, msg):
        command = Bool()
        command.data = msg.data < self.threshold
        self.publisher.publish(command)

def main(args=None):
    rclpy.init(args=args)
    node = LEDController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()