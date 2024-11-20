from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from launch.substitutions import TextSubstitution, LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    hostname_list = [
        "172.16.0.2",
        "172.16.0.3",
        "172.16.0.4",
        "172.16.0.5",
    ]
    name_list = [
        "shutdown_arm0",
        "shutdown_arm1",
        "shutdown_arm2",
        "shutdown_arm3",
    ]
    username = "moonshot"
    password = "moonshotfranka"
    launch_srcs = []
    for hostname, name in zip(hostname_list, name_list):
        launch_srcs.append(
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    PathJoinSubstitution([
                        FindPackageShare('franka_lock_unlock'),
                        'launch',
                        'franka_shutdown_single_launch.py'
                    ])
                ),
                launch_arguments={
                    'hostname': hostname,
                    'name': name,
                    'username': username,
                    'password': password,
                    'run_shutdown': 'true'
                }.items(),
            )
        )


    return LaunchDescription([
        *launch_srcs
    ])


if __name__ == "__main__":
    from launch import LaunchService

    launch_service = LaunchService()
    launch_service.include_launch_description(generate_launch_description())
    launch_service.run()