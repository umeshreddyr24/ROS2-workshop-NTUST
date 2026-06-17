import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import math

class TrajectoryGenerator(Node):

    def __init__(self):
        super().__init__('trajectory_generator')

        # Publisher for joint states
        self.publisher_ = self.create_publisher(JointState, '/joint_states', 10)

        # Timer to run at 20Hz (every 50 milliseconds)
        self.timer_period = 0.05
        self.timer = self.create_timer(self.timer_period, self.timer_callback)

        # Define joint names matching your assignment 3 URDF exactly
        self.joint_names = [
            'arm_0_joint', 'arm_1_joint', 'arm_2_joint',
            'gripper_1_joint', 'gripper_2_joint'
        ]

        # 5 Defined target points (waypoints) in joint space [arm0, arm1, arm2, grip1, grip2]
        self.waypoints = [
            [0.0,   0.0,   0.0,  0.0,  0.0],   # Home Position
            [1.57,  0.5,  -0.5,  0.03, 0.03],  # Reach Forward & Open Gripper
            [3.14,  0.8,  -0.8,  0.0,  0.0],   # Rotate & Close Gripper
            [-1.57, -0.5,  0.5,  0.03, 0.03],  # Swing Reverse
            [0.0,   0.0,   0.0,  0.0,  0.0]    # Return Home
        ]

        # Interpolation control variables
        self.current_waypoint_idx = 0
        self.next_waypoint_idx = 1
        self.interpolation_step = 0.0
        self.step_increment = 0.02  # Controls speed of transition between waypoints

        # Start at the first waypoint configuration
        self.current_positions = list(self.waypoints[0])
        self.get_logger().info('Robo Nemotron Kinematic Motion Simulation Initialized.')

    def timer_callback(self):
        # Obtain target endpoints
        start_pt = self.waypoints[self.current_waypoint_idx]
        end_pt = self.waypoints[self.next_waypoint_idx]

        # Perform Linear Interpolation (LERP) for smooth movement
        for i in range(len(self.joint_names)):
            self.current_positions[i] = start_pt[i] + (end_pt[i] - start_pt[i]) * self.interpolation_step

        # Construct and publish the message
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = self.joint_names
        msg.position = self.current_positions

        self.publisher_.publish(msg)

        # Increment step
        self.interpolation_step += self.step_increment

        # Check if the next waypoint target configuration is reached
        if self.interpolation_step >= 1.0:
            self.interpolation_step = 0.0
            self.current_waypoint_idx = self.next_waypoint_idx
            self.next_waypoint_idx = (self.next_waypoint_idx + 1) % len(self.waypoints)

def main(args=None):
    rclpy.init(args=args)
    node = TrajectoryGenerator()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
