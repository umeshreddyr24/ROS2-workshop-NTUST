# ROS2-workshop-NTUST
Create and build A simple 3 DoF manipulator robot description packages.
1. A simple 3 DoF manipulator - ros2 launch robo_nemotron_description description_test.launch.xml
2. Motion generation in a simple kinematic simulation - ros2 launch robo_nemotron_motion simulation.launch.xml
3. QT_QPA_PLATFORM=xcb ros2 launch moveit_setup_assistant setup_assistant.launch.py
ros2 launch robo_nemotron_gazebo spawn_robot.launch.xml
ros2 launch robo_nemotron_gazebo start_simulator.launch.xml 
