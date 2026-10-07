from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='simulador_tortuga',
            output='screen',
        ),
        Node(
            package='g05_prii3_turtlesim',
            executable='dibujar_0',
            name='dibujar_0',
            output='screen',
        ),
    ])
