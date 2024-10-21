import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    hardware_interface = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("bumperbot_firmware"),
            "launch",
            "hardware_interface.launch.py"
        ),
    )

    controller = IncludeLaunchDescription(
    os.path.join(
        get_package_share_directory("bumperbot_controller"),
        "launch",
        "controller.launch.py"
    ),
    launch_arguments={
        "use_simple_controller": "False",
        "use_python": "False"
    }.items(),
    )

    joystick = IncludeLaunchDescription(
    os.path.join(
        get_package_share_directory("bumperbot_controller"),
        "launch",
        "joystick_teleop.launch.py"
    ),
    launch_arguments={
        "use_sim_time": "False"
    }.items()
    )

    safety_stop = Node(
        package="bumperbot_utils",
        executable="safety_stop",
        output="screen",
    )

    return LaunchDescription([    
    hardware_interface,
    controller,
    joystick,
    #safety_stop,
    ])



