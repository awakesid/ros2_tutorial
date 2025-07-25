import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/awakesid/Desktop/second_ros2_ws/install/tutorial_node'
