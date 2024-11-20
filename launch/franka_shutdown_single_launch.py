from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
import os
from launch.substitutions import TextSubstitution, LaunchConfiguration

def generate_launch_description():
    hostname = LaunchConfiguration('hostname')
    name = LaunchConfiguration('name')
    username = LaunchConfiguration('username')
    password = LaunchConfiguration('password')
    shutdown = LaunchConfiguration('run_shutdown')

    hostname_arg = DeclareLaunchArgument(
        'hostname', default_value='0.0.0.0',
        description='The hostname of the robot')
    name_arg = DeclareLaunchArgument(
        'name', default_value='unlock_arm0',
        description='The name of the robot (used for the namespace)')
    username_arg = DeclareLaunchArgument(
        'username', default_value="moonshot",
        description='The username for the robot')
    password_arg = DeclareLaunchArgument(
        'password', default_value='moonshotfranka',
        description='The password for the robot')

    shutdown_arg = DeclareLaunchArgument(
        'run_shutdown', default_value='false',
        description='Run the shutdown command instead of the unlock command')

    run_node = Node(
            package='franka_lock_unlock',
            executable='run',
            name=name,
            arguments=[hostname, username, password, "-u", "-w",
                       "-r", "-p", "-c", "-i", "-l"],
            parameters=[{
                "shutdown_request": shutdown,
            }],
            output="screen",
        )

    return LaunchDescription([
        hostname_arg,
        name_arg,
        username_arg,
        password_arg,
        shutdown_arg,
        run_node,
    ])
