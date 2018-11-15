#!/usr/bin/env python

import rospy
import tf
from kuka_arm.srv import *
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from geometry_msgs.msg import Pose
from mpmath import *
from sympy import 

def TF_Matrix(alpha, a, d, q):
		TF = Matrix([
			[cos(q), 		-sin(q), 		0, 		a],
	     		[sin(q)*cos(alpha), 	cos(q)*cos(alpha), 	-sin(alpha), 	-sin(alpha)*d],
	     		[sin(q)* sin(alpha), 	cos(q)*sin(alpha), 	cos(alpha), 	cos(alpha)*d],
	     		[0,			0,			0,		1]
		   ])
  		return TF
      
def get_WC(p_ee, Rot_ee, DH_table);
  
  WC = p_ee - DH_table['d6'] * Rot_ee[:,2] 
  
  return WC

def cosine_law(a_1, d_1, a_2, d_4, WC):
  
  side_a = a_2
  side_b = sqrt(pow(sqrt(WC[0] * WC[0] + WC[1] * WC[1]) - 0.35, 2)+ pow((WC[2] - 0.75), 2))
	side_c = 1.25
  
  angle_a = acos((side_b * side_b + side_c * side_c - side_a * side_a) / (2 * side_b * side_c))
  angle_b = acos((side_a * side_a + side_c * side_c - side_b * side_b) / (2 * side_a * side_c))
  angle_c = acos((side_a * side_a + side_b * side_b - side_c * side_c ) / (2 * side_a * side_b))
  
  angles = [angle_a, angle_b, angle_c]
  
  returrn angles 
 
 
def inv_pos(WC, angles):
  
  theta1 = atan2(WC[1], WC[0], DH_table)
  theta2 = pi/2. - angles[0] - atan2(WC[2] - DH_table['d1'], sqrt(WC[0]**2 + WC[1]**2) - DH_tables['a1'])
  theta3 = pi/2. - angles[1] - atan2(DH_table['a3'], DH_table['d4']
  
  return theta1, theta2, theta3
  
def get_R0_3(theta1, theta2, theta3):

  return R0_3.evalf(subs={q1:theta1, q2:theta2, q3:theta3}0
  
def inv_orient(theta1, theta2, theta3, R0_3, Rot_ee):
  
  R3_6 = R0_3.T * Rot_ee
  
  theta4 = atan2(R3_6[2,2], -R3_6[0,2])
  theta5 = atan2(sqrt(R3_6[0,2]**2 + R3_6[2,2]**2, R3_6[1,2])
  theta6 = atan2(-R3_6[1,1], R3_6[1,0])
  
  return theta4, theta5, theta6
  
def get_R_corr(roll, pitch, yaw):
  return Rot_ee.subs({r: roll, p: pitch, y: yaw})

  
  
