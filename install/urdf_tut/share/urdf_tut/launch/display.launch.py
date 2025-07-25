import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_share = get_package_share_directory('urdf_tut')
    
    urdf_path = os.path.join(pkg_share, 'urdf', 'my_robot.urdf')
    rviz_config = os.path.join(pkg_share, 'config', 'robot.rviz')
    
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            arguments=[urdf_path],
            output='screen'
        ),
        Node(
            package='urdf_tut',
            executable='read_encoder',
            name='encoder_reader',
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config],
            output='screen'
        )
    ])