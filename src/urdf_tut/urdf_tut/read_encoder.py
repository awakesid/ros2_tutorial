#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import serial
import math

class EncoderReader(Node):
    def __init__(self):
        super().__init__('encoder_reader')
        
        # Parameters with correct default baud rate
        self.declare_parameter('serial_port', '/dev/ttyACM0')
        self.declare_parameter('baud_rate', 115200)  # Fixed to 115200
        self.declare_parameter('encoder_ppr', 2000)
        
        # Get parameters
        port = self.get_parameter('serial_port').value
        baud = self.get_parameter('baud_rate').value
        self.ppr = self.get_parameter('encoder_ppr').value
        
        # Debug connection info
        self.get_logger().info(f"Connecting to {port} at {baud} baud")
        
        # Serial connection
        try:
            self.ser = serial.Serial(port, baud, timeout=1)
            self.get_logger().info(f"Connected successfully! Port info: {self.ser}")
        except serial.SerialException as e:
            self.get_logger().error(f"Serial connection failed: {e}")
            raise
        
        # Publisher and message setup
        self.joint_pub = self.create_publisher(JointState, 'joint_states', 10)
        self.joint_msg = JointState()
        self.joint_msg.name = ['base_to_right_leg']
        
        # Timer
        self.timer = self.create_timer(0.01, self.read_serial)

    def read_serial(self):
        if self.ser.in_waiting:
            try:
                # Read with error handling
                raw_data = self.ser.readline()
                line = raw_data.decode('utf-8', errors='replace').strip()
                
                if line:
                    pos = int(line)
                    rad_pos = (pos / self.ppr) * 2 * math.pi
                    
                    self.joint_msg.header.stamp = self.get_clock().now().to_msg()
                    self.joint_msg.position = [rad_pos]
                    self.joint_pub.publish(self.joint_msg)
                    
            except ValueError:
                self.get_logger().warn(f"Invalid data: {line}")
            except UnicodeDecodeError:
                self.get_logger().warn(f"Decoding error in: {raw_data}")
            except Exception as e:
                self.get_logger().error(f"Unexpected error: {e}")

    def __del__(self):
        if hasattr(self, 'ser') and self.ser.is_open:
            self.ser.close()

# ... (rest of main function remains same)