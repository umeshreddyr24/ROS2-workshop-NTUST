"""
A launch file for running the motion planning python api tutorial
"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from moveit_configs_utils import MoveItConfigsBuilder


def generate_launch_description():
    moveit_config = (
        MoveItConfigsBuilder(
            robot_name="TODO_YOUR_ROBOT_NAME", package_name="TODO_YOUR_ROBOT_NAME_moveit_config"
        )
        .robot_description(file_path="config/TODO_YOUR_ROBOT_NAME.urdf.xacro")
        .trajectory_execution(file_path="config/moveit_controllers.yaml")
        .moveit_cpp(
            file_path=get_package_share_directory("TODO_YOUR_ROBOT_NAME_scripts")
            + "/config/moveit_py.yaml"
        )
        .to_moveit_configs()
    )

    script_file = DeclareLaunchArgument(
        "script_file",
        default_value="moveit_py_example_node",
        description="Python API script file name",
    )

    parameters = moveit_config.to_dict()
    parameters['use_sim_time'] = True

    moveit_py_node = Node(
        name="moveit_py",
        package="TODO_YOUR_ROBOT_NAME_scripts",
        executable=LaunchConfiguration("script_file"),
        output="both",
        parameters=[parameters],
    )

    return LaunchDescription(
        [
            script_file,
            moveit_py_node,
        ]
    )
