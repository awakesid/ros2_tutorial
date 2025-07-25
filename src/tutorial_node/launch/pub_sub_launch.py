# my_package/launch/pub_sub_launch.py

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tutorial_node',
            executable='publisher_node',
            name='publisher',
            output='screen'
        ),
        Node(
            package='tutorial_node',
            executable='subscriber_node',
            name='subscriber',
            output='screen'
        ),
    ])
