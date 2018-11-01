## Project: Kinematics Pick & Place
### Ishmael Rogers
### Robotics Engineer, Infinitely Deep Robotics Group



---
### Writeup / README
### Kinematic Analysis
### Kuka KR210 model

https://github.com/IshmaelRogers/Kuka-Arm/issues/2

### Explanation of DH Parameters
---
<a href="https://www.codecogs.com/eqnedit.php?latex=\alpha&space;_{i-1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\alpha&space;_{i-1}" title="\alpha _{i-1}" /></a>

The twist angle is defined as the angle between <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{Z}_{i-1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{Z}_{i-1}" title="\hat{Z}_{i-1}" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{Z}_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{Z}_{i}" title="\hat{Z}_{i}" /></a> measured along <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{X}_{i-1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{X}_{i-1}" title="\hat{X}_{i-1}" /></a>


<a href="https://www.codecogs.com/eqnedit.php?latex=a_{i-1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a_{i-1}" title="a_{i-1}" /></a>

The link length is the distance between <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{Z}_{i-1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{Z}_{i-1}" title="\hat{Z}_{i-1}" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{Z}_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{Z}_{i}" title="\hat{Z}_{i}" /></a> measured along <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{X}_{i-1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{X}_{i-1}" title="\hat{X}_{i-1}" /></a>, where <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{X}_{i-1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{X}_{i-1}" title="\hat{X}_{i-1}" /></a> is perpendicular to both <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{Z}_{i-1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{Z}_{i-1}" title="\hat{Z}_{i-1}" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{Z}_{i-1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{Z}_{i-1}" title="\hat{Z}_{i-1}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=d_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?d_{i}" title="d_{i}" /></a>

The link offset is the signed distance from <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{X}_{i-1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{X}_{i-1}" title="\hat{X}_{i-1}" /></a> to <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{X}_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{X}_{i}" title="\hat{X}_{i}" /></a> measured along <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{Z}_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{Z}_{i}" title="\hat{Z}_{i}" /></a> for prismatic joints. 

<a href="https://www.codecogs.com/eqnedit.php?latex=\theta_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\theta_{i}" title="\theta_{i}" /></a>

The joint angle is the angle between <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{X}_{i-1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{X}_{i-1}" title="\hat{X}_{i-1}" /></a> to <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{X}_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{X}_{i}" title="\hat{X}_{i}" /></a> measured along <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{Z}_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{Z}_{i}" title="\hat{Z}_{i}" /></a> in a right hand sense for revolute joints.



###
### DH Parameter Table 

<table>
  <tr>
    <th>Link i</th>
    <th>Twist angle</th>
    <th>Link length</th>
    <th>Offset</th>
    <th>Joint angle </th>
  </tr>
  <tr>
    <td>Link 0</td>
    <td>0</td>
    <td>0</td>
    <td>0.75</td>
    <td>q1</td>
  </tr>
  <tr>
    <td>Link 1</td>
    <td>-pi/2</td>
    <td>0.35</td>
    <td>0</td>
    <td>q2 = q2 - pi/2</td>
  </tr>
  <tr>
    <td>Link 2</td>
    <td>0</td>
    <td>1.25</td>
    <td>0</td>
    <td>q3</td>
  </tr>
  <tr>
    <td>Link 3</td>
    <td>-pi/2</td>
    <td>-0.054</td>
    <td>1.50</td>
    <td>q4</td>
  </tr>
  <tr>
    <td>Link 4</td>
    <td>pi/2</td>
    <td>0</td>
    <td>0</td>
    <td>q5</td>
  </tr>
  <tr>
    <td>Link 5</td>
    <td>-pi/2</td>
    <td>0</td>
    <td>0</td>
    <td>q6</td>
  </tr>
  <tr>
    <td>Link 6 </td>
    <td>0</td>
    <td>0</td>
    <td>0.303</td>
    <td>q7</td>
  </tr>
</table>

### Finding the Homogenous Matrix is a composition of homogeneous transforms

<a href="https://www.codecogs.com/eqnedit.php?latex=_{i}^{i-1}\textrm{T}=&space;R_{x}(\alpha_{i-1}&space;)&space;\times&space;D_{x}(a_{i-1})&space;\times&space;R_{z}(\theta{i})&space;\times&space;D_{z}(d_{i})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?_{i}^{i-1}\textrm{T}=&space;R_{x}(\alpha_{i-1}&space;)&space;\times&space;D_{x}(a_{i-1})&space;\times&space;R_{z}(\theta{i})&space;\times&space;D_{z}(d_{i})" title="_{i}^{i-1}\textrm{T}= R_{x}(\alpha_{i-1} ) \times D_{x}(a_{i-1}) \times R_{z}(\theta{i}) \times D_{z}(d_{i})" /></a>

#### Create individual transformation matrices about each joint. 

Link 0-1

<a href="https://www.codecogs.com/eqnedit.php?latex=_{1}^{0}\textrm{T}=\begin{bmatrix}&space;\cos(\theta_{1})&space;&\sin(\theta_{1})&space;&0&space;&a_{0}&space;\\&space;\sin(\theta_{1})\times&space;\cos(\alpha_{0})&&space;\cos(\theta_{1})\times&space;\cos(\alpha_{0})&space;&-\sin(\alpha_0)&space;&-\sin(\alpha_{0}\times&space;d_{i})\\&space;\sin(\theta_1)\times&space;\sin(\alpha_{0})&space;&\cos(\theta_{1})\times\sin(\alpha_{0})&space;&\cos(\alpha_{0})&space;&\cos(\alpha_1\)\times&space;d_i&space;\\&space;0&space;&0&space;&0&space;&1&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?_{1}^{0}\textrm{T}=\begin{bmatrix}&space;\cos(\theta_{1})&space;&\sin(\theta_{1})&space;&0&space;&a_{0}&space;\\&space;\sin(\theta_{1})\times&space;\cos(\alpha_{0})&&space;\cos(\theta_{1})\times&space;\cos(\alpha_{0})&space;&-\sin(\alpha_0)&space;&-\sin(\alpha_{0}\times&space;d_{i})\\&space;\sin(\theta_1)\times&space;\sin(\alpha_{0})&space;&\cos(\theta_{1})\times\sin(\alpha_{0})&space;&\cos(\alpha_{0})&space;&\cos(\alpha_1\)\times&space;d_i&space;\\&space;0&space;&0&space;&0&space;&1&space;\end{bmatrix}" title="_{1}^{0}\textrm{T}=\begin{bmatrix} \cos(\theta_{1}) &\sin(\theta_{1}) &0 &a_{0} \\ \sin(\theta_{1})\times \cos(\alpha_{0})& \cos(\theta_{1})\times \cos(\alpha_{0}) &-\sin(\alpha_0) &-\sin(\alpha_{0}\times d_{i})\\ \sin(\theta_1)\times \sin(\alpha_{0}) &\cos(\theta_{1})\times\sin(\alpha_{0}) &\cos(\alpha_{0}) &\cos(\alpha_1\)\times d_i \\ 0 &0 &0 &1 \end{bmatrix}" /></a>

Link 1-2

<a href="https://www.codecogs.com/eqnedit.php?latex=_{2}^{1}\textrm{T}=\begin{bmatrix}&space;\cos(\theta_{2})&space;&\sin(\theta_{2})&space;&0&space;&a_{1}&space;\\&space;\sin(\theta_{2})\times&space;\cos(\alpha_{1})&&space;\cos(\theta_{2})\times&space;\cos(\alpha_{1})&space;&-\sin(\alpha_1)&space;&-\sin(\alpha_{1}\times&space;d_{2})\\&space;\sin(\theta_2)\times&space;\sin(\alpha_{1})&space;&\cos(\theta_{2})\times\sin(\alpha_{1})&space;&\cos(\alpha_{1})&space;&\cos(\alpha_2\)\times&space;d_i&space;\\&space;0&space;&0&space;&0&space;&1&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?_{1}^{0}\textrm{T}=\begin{bmatrix}&space;\cos(\theta_{2})&space;&\sin(\theta_{2})&space;&0&space;&a_{1}&space;\\&space;\sin(\theta_{2})\times&space;\cos(\alpha_{1})&&space;\cos(\theta_{2})\times&space;\cos(\alpha_{1})&space;&-\sin(\alpha_1)&space;&-\sin(\alpha_{1}\times&space;d_{2})\\&space;\sin(\theta_2)\times&space;\sin(\alpha_{1})&space;&\cos(\theta_{2})\times\sin(\alpha_{1})&space;&\cos(\alpha_{1})&space;&\cos(\alpha_2\)\times&space;d_i&space;\\&space;0&space;&0&space;&0&space;&1&space;\end{bmatrix}" title="_{1}^{0}\textrm{T}=\begin{bmatrix} \cos(\theta_{2}) &\sin(\theta_{2}) &0 &a_{1} \\ \sin(\theta_{2})\times \cos(\alpha_{1})& \cos(\theta_{2})\times \cos(\alpha_{1}) &-\sin(\alpha_1) &-\sin(\alpha_{1}\times d_{2})\\ \sin(\theta_2)\times \sin(\alpha_{1}) &\cos(\theta_{2})\times\sin(\alpha_{1}) &\cos(\alpha_{1}) &\cos(\alpha_2\)\times d_i \\ 0 &0 &0 &1 \end{bmatrix}" /></a>












### a generalized homogeneous transform between base_link and gripper_link using only end-effector(gripper) pose.



#### 3. Decouple Inverse Kinematics problem into Inverse Position Kinematics and inverse Orientation Kinematics; doing so derive the equations to calculate all individual joint angles.

Used the modified DH Conditions to locate the parameters
Used he law of cosines to locate the wrist center 

![alt text][image2]

### Project Implementation

#### 1. Fill in the `IK_server.py` file with properly commented python code for calculating Inverse Kinematics based on previously performed Kinematic Analysis. Your code must guide the robot to successfully complete 8/10 pick and place cycles. Briefly discuss the code you implemented and your results. 

The code follows calculates the FK model and then uses poses to estimate joint angles using the IKserver.py


And just for fun, another example image:
![alt text][image3]


