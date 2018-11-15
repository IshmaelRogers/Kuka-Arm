#!/usr/bin/env python


# import modules
import rospy
import tf
from kuka_arm.srv import *
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from geometry_msgs.msg import Pose
from mpmath import *
from sympy import *
from IK_helper import get_R_corr, get_WC, inv_pos, get_R0_3 inv_orient, TF_matrix


# Define DH parameter symbols
alpha0, alpha1, alpha2, alpha3, alpha4, alpha5, alpha6 = symbols('alpha0:7') # twist angle
a0, a1, a2, a3, a4, a5, a6 = symbols('a0:7') # link length
d1, d2, d3, d4, d5, d6, d7 = symbols('d1:8') # link offset
q1, q2, q3, q4, q5, q6, q7 = symbols('q1:8') # joint angle

# Modified DH parameters
DH_table = {alpha0:      0, a0:      0, d1:   0.75, q1:        q1,
            alpha1: -pi/2., a1:   0.35, d2:      0, q2: -pi/2.+q2,
            alpha2:      0, a2:   1.25, d3:      0, q3:        q3,
            alpha3: -pi/2., a3: -0.054, d4:    1.5, q4:        q4,
            alpha4:  pi/2., a4:      0, d5:      0, q5:        q5,
            alpha5: -pi/2., a5:      0, d6:      0, q6:        q6,
            alpha6:      0, a6:      0, d7:  0.303, q7:         0}


T0_1 = TF_Matrix(alpha0, a0, d1, q1).subs(DH_Table)
T1_2 = TF_Matrix(alpha1, a1, d2, q2).subs(DH_Table)
T2_3 = TF_Matrix(alpha2, a2, d3, q3).subs(DH_Table)
T3_4 = TF_Matrix(alpha3, a3, d4, q4).subs(DH_Table)
T4_5 = TF_Matrix(alpha4, a4, d5, q5).subs(DH_Table)
T5_6 = TF_Matrix(alpha5, a5, d6, q6).subs(DH_Table)
T6_EE = TF_Matrix(alpha6, a6, d7, q7).subs(DH_Table)

T0_EE = simplify(T0_1 * T1_2 * T2_3 * T3_4 * T4_5 * T5_6 * T6_EE)
R0_3 = T0_1[0:3,0:3] * T1_2[0:3,0:3] * T2_3[0:3,0:3]


r, p, y = symbols('r p y') 

ROT_x = Matrix([[1,      0,       0],
                [0, cos(r), -sin(r)],
                [0, sin(r), cos(r)]])

ROT_y = Matrix([[ cos(p), 0, sin(p)],
                [      0, 1,      0],
                [-sin(p), 0, cos(p)]])

ROT_z = Matrix([[cos(y), -sin(y), 0],
                [sin(y),  cos(y), 0],
                [     0,       0, 1]])

ROT_EE = ROT_z * ROT_y * ROT_x

# Account for the URDF file defintion and make the correction.
ROT_correction = ROT_z.subs(y, radians(180)) * ROT_y.subs(p, radians(-90))
ROT_EE = ROT_EE * ROT_correction


def handle_calculate_IK(req):
    rospy.loginfo("Received %s eef-poses from the plan" % len(req.poses))
    if len(req.poses) < 1:
        print "No valid poses received"
        return -1
    else:
        # Initialize service response
        joint_trajectory_list = []
        for x in xrange(0, len(req.poses)):
            # IK code starts here
            joint_trajectory_point = JointTrajectoryPoint()

            # Extract end-effector position and orientation from request
            # px,py,pz = end-effector position
            # roll, pitch, yaw = end-effector orientation
            px = req.poses[x].position.x
            py = req.poses[x].position.y
            pz = req.poses[x].position.z

            (roll, pitch, yaw) = tf.transformations.euler_from_quaternion(
                [req.poses[x].orientation.x, req.poses[x].orientation.y,
                    req.poses[x].orientation.z, req.poses[x].orientation.w])
            Rot_ee = get_R_corr(roll, pitch, yaw)
            WC = get_WC(p_ee, Rot_ee, DH_table)
            theta1, theta2, theta3 = inv_pos(WC, angles):
            R0_3 = get_R0_3(theta1, theta2, theta3)
            theta4, theta5, theta6 = inv_orient(theta1, theta2, theta3, R0_3, Rot_ee):
            
            # Populate response for the IK request
            
            joint_trajectory_point.positions = [theta1, theta2, theta3, theta4, theta5, theta6]
            joint_trajectory_list.append(joint_trajectory_point)
        
        rospy.loginfo("length of Joint Trajectory List: %s" % len(joint_trajectory_list))
        return CalculateIKResponse(joint_trajectory_list)  
            
def IK_server():
    # initialize node and declare calculate_ik service
    rospy.init_node('IK_server')
    s = rospy.Service('calculate_ik', CalculateIK, handle_calculate_IK)
    print "Ready to receive an IK request"
    rospy.spin()

if __name__ == "__main__":
    IK_server()            
        


