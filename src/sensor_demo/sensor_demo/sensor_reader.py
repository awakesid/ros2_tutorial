#!/usr/bin/env python3
import rclpy
# ros2 run sensor_demo sensor_readerfrom rclpy.node import Node
from std_msgs.msg import Float32, Bool
import serial

class SensorReader(Node):
    def __init__(self):
        super().__init__('sensor_reader')
        self.publisher = self.create_publisher(Float32, '/distance', 10)
        self.subscription = self.create_subscription(
            Bool,
            '/led_command',
            self.led_callback,
            10)
        self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
        self.timer = self.create_timer(0.1, self.read_sensor)
        self.get_logger().info("Sensor reader started!")

    def read_sensor(self):
        line = self.ser.readline().decode('utf-8').strip()
        try:
            distance = float(line)
            msg = Float32()
            msg.data = distance
            self.publisher.publish(msg)
        except ValueError:
            pass

    def led_callback(self, msg):
        self.ser.write(b'1' if msg.data else b'0')

def main(args=None):
    rclpy.init(args=args)
    node = SensorReader()
    rclpy.spin(node)
    node.ser.close()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()