### Project: Kinematics Pick & Place
### Ishmael Rogers
### Robotics Engineer, Infinitely Deep Robotics Group
### 2018 
### Writeup / README
---
### Kinematic Analysis
---

### Kuka KR210 annotated model

https://github.com/IshmaelRogers/Kuka-Arm/issues/2

### Explanation of DH Parameters

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

### Link 0-1

<a href="https://www.codecogs.com/eqnedit.php?latex=_{1}^{0}\textrm{T}=\begin{bmatrix}&space;\cos(\theta_{1})&space;&\sin(\theta_{1})&space;&0&space;&a_{0}&space;\\&space;\sin(\theta_{1})\times&space;\cos(\alpha_{0})&&space;\cos(\theta_{1})\times&space;\cos(\alpha_{0})&space;&-\sin(\alpha_0)&space;&-\sin(\alpha_{0}\times&space;d_{i})\\&space;\sin(\theta_1)\times&space;\sin(\alpha_{0})&space;&\cos(\theta_{1})\times\sin(\alpha_{0})&space;&\cos(\alpha_{0})&space;&\cos(\alpha_1\)\times&space;d_i&space;\\&space;0&space;&0&space;&0&space;&1&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?_{1}^{0}\textrm{T}=\begin{bmatrix}&space;\cos(\theta_{1})&space;&\sin(\theta_{1})&space;&0&space;&a_{0}&space;\\&space;\sin(\theta_{1})\times&space;\cos(\alpha_{0})&&space;\cos(\theta_{1})\times&space;\cos(\alpha_{0})&space;&-\sin(\alpha_0)&space;&-\sin(\alpha_{0}\times&space;d_{i})\\&space;\sin(\theta_1)\times&space;\sin(\alpha_{0})&space;&\cos(\theta_{1})\times\sin(\alpha_{0})&space;&\cos(\alpha_{0})&space;&\cos(\alpha_1\)\times&space;d_i&space;\\&space;0&space;&0&space;&0&space;&1&space;\end{bmatrix}" title="_{1}^{0}\textrm{T}=\begin{bmatrix} \cos(\theta_{1}) &\sin(\theta_{1}) &0 &a_{0} \\ \sin(\theta_{1})\times \cos(\alpha_{0})& \cos(\theta_{1})\times \cos(\alpha_{0}) &-\sin(\alpha_0) &-\sin(\alpha_{0}\times d_{i})\\ \sin(\theta_1)\times \sin(\alpha_{0}) &\cos(\theta_{1})\times\sin(\alpha_{0}) &\cos(\alpha_{0}) &\cos(\alpha_1\)\times d_i \\ 0 &0 &0 &1 \end{bmatrix}" /></a>

### Link 1-2

<a href="https://www.codecogs.com/eqnedit.php?latex=_{2}^{1}\textrm{T}=\begin{bmatrix}&space;\cos(\theta_{2})&space;&\sin(\theta_{2})&space;&0&space;&a_{1}&space;\\&space;\sin(\theta_{2})\times&space;\cos(\alpha_{1})&&space;\cos(\theta_{2})\times&space;\cos(\alpha_{1})&space;&-\sin(\alpha_1)&space;&-\sin(\alpha_{1}\times&space;d_{2})\\&space;\sin(\theta_2)\times&space;\sin(\alpha_{1})&space;&\cos(\theta_{2})\times\sin(\alpha_{1})&space;&\cos(\alpha_{1})&space;&\cos(\alpha_2\)\times&space;d_i&space;\\&space;0&space;&0&space;&0&space;&1&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?_{2}^{1}\textrm{T}=\begin{bmatrix}&space;\cos(\theta_{2})&space;&\sin(\theta_{2})&space;&0&space;&a_{1}&space;\\&space;\sin(\theta_{2})\times&space;\cos(\alpha_{1})&&space;\cos(\theta_{2})\times&space;\cos(\alpha_{1})&space;&-\sin(\alpha_1)&space;&-\sin(\alpha_{1}\times&space;d_{2})\\&space;\sin(\theta_2)\times&space;\sin(\alpha_{1})&space;&\cos(\theta_{2})\times\sin(\alpha_{1})&space;&\cos(\alpha_{1})&space;&\cos(\alpha_2\)\times&space;d_i&space;\\&space;0&space;&0&space;&0&space;&1&space;\end{bmatrix}" title="_{2}^{1}\textrm{T}=\begin{bmatrix} \cos(\theta_{2}) &\sin(\theta_{2}) &0 &a_{1} \\ \sin(\theta_{2})\times \cos(\alpha_{1})& \cos(\theta_{2})\times \cos(\alpha_{1}) &-\sin(\alpha_1) &-\sin(\alpha_{1}\times d_{2})\\ \sin(\theta_2)\times \sin(\alpha_{1}) &\cos(\theta_{2})\times\sin(\alpha_{1}) &\cos(\alpha_{1}) &\cos(\alpha_2\)\times d_i \\ 0 &0 &0 &1 \end{bmatrix}" /></a>

### Link 2-3

<a href="https://www.codecogs.com/eqnedit.php?latex=_{3}^{2}\textrm{T}=\begin{bmatrix}&space;\cos(\theta_{3})&space;&\sin(\theta_{3})&space;&0&space;&a_{2}&space;\\&space;\sin(\theta_{3})\times&space;\cos(\alpha_{2})&&space;\cos(\theta_{3})\times&space;\cos(\alpha_{2})&space;&-\sin(\alpha_2)&space;&-\sin(\alpha_{2}\times&space;d_{3})\\&space;\sin(\theta_3)\times&space;\sin(\alpha_{2})&space;&\cos(\theta_{3})\times\sin(\alpha_{2})&space;&\cos(\alpha_{2})&space;&\cos(\alpha_3\)\times&space;d_3&space;\\&space;0&space;&0&space;&0&space;&1&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?_{3}^{2}\textrm{T}=\begin{bmatrix}&space;\cos(\theta_{3})&space;&\sin(\theta_{3})&space;&0&space;&a_{2}&space;\\&space;\sin(\theta_{3})\times&space;\cos(\alpha_{2})&&space;\cos(\theta_{3})\times&space;\cos(\alpha_{2})&space;&-\sin(\alpha_2)&space;&-\sin(\alpha_{2}\times&space;d_{3})\\&space;\sin(\theta_3)\times&space;\sin(\alpha_{2})&space;&\cos(\theta_{3})\times\sin(\alpha_{2})&space;&\cos(\alpha_{2})&space;&\cos(\alpha_3\)\times&space;d_3&space;\\&space;0&space;&0&space;&0&space;&1&space;\end{bmatrix}" title="_{3}^{2}\textrm{T}=\begin{bmatrix} \cos(\theta_{3}) &\sin(\theta_{3}) &0 &a_{2} \\ \sin(\theta_{3})\times \cos(\alpha_{2})& \cos(\theta_{3})\times \cos(\alpha_{2}) &-\sin(\alpha_2) &-\sin(\alpha_{2}\times d_{3})\\ \sin(\theta_3)\times \sin(\alpha_{2}) &\cos(\theta_{3})\times\sin(\alpha_{2}) &\cos(\alpha_{2}) &\cos(\alpha_3\)\times d_3 \\ 0 &0 &0 &1 \end{bmatrix}" /></a>

### Link 3-4

<a href="https://www.codecogs.com/eqnedit.php?latex=_{4}^{3}\textrm{T}=\begin{bmatrix}&space;\cos(\theta_{4})&space;&\sin(\theta_{4})&space;&0&space;&a_{3}&space;\\&space;\sin(\theta_{4})\times&space;\cos(\alpha_{3})&&space;\cos(\theta_{4})\times&space;\cos(\alpha_{3})&space;&-\sin(\alpha_3)&space;&-\sin(\alpha_{3}\times&space;d_{4})\\&space;\sin(\theta_4)\times&space;\sin(\alpha_{3})&space;&\cos(\theta_{4})\times\sin(\alpha_{3})&space;&\cos(\alpha_{3})&space;&\cos(\alpha_4\)\times&space;d_4&space;\\&space;0&space;&0&space;&0&space;&1&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?_{4}^{3}\textrm{T}=\begin{bmatrix}&space;\cos(\theta_{4})&space;&\sin(\theta_{4})&space;&0&space;&a_{3}&space;\\&space;\sin(\theta_{4})\times&space;\cos(\alpha_{3})&&space;\cos(\theta_{4})\times&space;\cos(\alpha_{3})&space;&-\sin(\alpha_3)&space;&-\sin(\alpha_{3}\times&space;d_{4})\\&space;\sin(\theta_4)\times&space;\sin(\alpha_{3})&space;&\cos(\theta_{4})\times\sin(\alpha_{3})&space;&\cos(\alpha_{3})&space;&\cos(\alpha_4\)\times&space;d_4&space;\\&space;0&space;&0&space;&0&space;&1&space;\end{bmatrix}" title="_{4}^{3}\textrm{T}=\begin{bmatrix} \cos(\theta_{4}) &\sin(\theta_{4}) &0 &a_{3} \\ \sin(\theta_{4})\times \cos(\alpha_{3})& \cos(\theta_{4})\times \cos(\alpha_{3}) &-\sin(\alpha_3) &-\sin(\alpha_{3}\times d_{4})\\ \sin(\theta_4)\times \sin(\alpha_{3}) &\cos(\theta_{4})\times\sin(\alpha_{3}) &\cos(\alpha_{3}) &\cos(\alpha_4\)\times d_4 \\ 0 &0 &0 &1 \end{bmatrix}" /></a>

### Link 4-5

<a href="https://www.codecogs.com/eqnedit.php?latex=_{5}^{4}\textrm{T}=\begin{bmatrix}&space;\cos(\theta_{5})&space;&\sin(\theta_{5})&space;&0&space;&a_{4}&space;\\&space;\sin(\theta_{5})\times&space;\cos(\alpha_{4})&&space;\cos(\theta_{5})\times&space;\cos(\alpha_{4})&space;&-\sin(\alpha_4)&space;&-\sin(\alpha_{4}\times&space;d_{5})\\&space;\sin(\theta_5)\times&space;\sin(\alpha_{4})&space;&\cos(\theta_{5})\times\sin(\alpha_{4})&space;&\cos(\alpha_{4})&space;&\cos(\alpha_5\)\times&space;d_5&space;\\&space;0&space;&0&space;&0&space;&1&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?_{5}^{4}\textrm{T}=\begin{bmatrix}&space;\cos(\theta_{5})&space;&\sin(\theta_{5})&space;&0&space;&a_{4}&space;\\&space;\sin(\theta_{5})\times&space;\cos(\alpha_{4})&&space;\cos(\theta_{5})\times&space;\cos(\alpha_{4})&space;&-\sin(\alpha_4)&space;&-\sin(\alpha_{4}\times&space;d_{5})\\&space;\sin(\theta_5)\times&space;\sin(\alpha_{4})&space;&\cos(\theta_{5})\times\sin(\alpha_{4})&space;&\cos(\alpha_{4})&space;&\cos(\alpha_5\)\times&space;d_5&space;\\&space;0&space;&0&space;&0&space;&1&space;\end{bmatrix}" title="_{5}^{4}\textrm{T}=\begin{bmatrix} \cos(\theta_{5}) &\sin(\theta_{5}) &0 &a_{4} \\ \sin(\theta_{5})\times \cos(\alpha_{4})& \cos(\theta_{5})\times \cos(\alpha_{4}) &-\sin(\alpha_4) &-\sin(\alpha_{4}\times d_{5})\\ \sin(\theta_5)\times \sin(\alpha_{4}) &\cos(\theta_{5})\times\sin(\alpha_{4}) &\cos(\alpha_{4}) &\cos(\alpha_5\)\times d_5 \\ 0 &0 &0 &1 \end{bmatrix}" /></a>

### Link 5-6

<a href="https://www.codecogs.com/eqnedit.php?latex=_{6}^{5}\textrm{T}=\begin{bmatrix}&space;\cos(\theta_{6})&space;&\sin(\theta_{6})&space;&0&space;&a_{5}&space;\\&space;\sin(\theta_{6})\times&space;\cos(\alpha_{5})&&space;\cos(\theta_{6})\times&space;\cos(\alpha_{5})&space;&-\sin(\alpha_5)&space;&-\sin(\alpha_{5}\times&space;d_{6})\\&space;\sin(\theta_6)\times&space;\sin(\alpha_{5})&space;&\cos(\theta_{6})\times\sin(\alpha_{5})&space;&\cos(\alpha_{5})&space;&\cos(\alpha_6\)\times&space;d_6&space;\\&space;0&space;&0&space;&0&space;&1&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?_{6}^{5}\textrm{T}=\begin{bmatrix}&space;\cos(\theta_{6})&space;&\sin(\theta_{6})&space;&0&space;&a_{5}&space;\\&space;\sin(\theta_{6})\times&space;\cos(\alpha_{5})&&space;\cos(\theta_{6})\times&space;\cos(\alpha_{5})&space;&-\sin(\alpha_5)&space;&-\sin(\alpha_{5}\times&space;d_{6})\\&space;\sin(\theta_6)\times&space;\sin(\alpha_{5})&space;&\cos(\theta_{6})\times\sin(\alpha_{5})&space;&\cos(\alpha_{5})&space;&\cos(\alpha_6\)\times&space;d_6&space;\\&space;0&space;&0&space;&0&space;&1&space;\end{bmatrix}" title="_{6}^{5}\textrm{T}=\begin{bmatrix} \cos(\theta_{6}) &\sin(\theta_{6}) &0 &a_{5} \\ \sin(\theta_{6})\times \cos(\alpha_{5})& \cos(\theta_{6})\times \cos(\alpha_{5}) &-\sin(\alpha_5) &-\sin(\alpha_{5}\times d_{6})\\ \sin(\theta_6)\times \sin(\alpha_{5}) &\cos(\theta_{6})\times\sin(\alpha_{5}) &\cos(\alpha_{5}) &\cos(\alpha_6\)\times d_6 \\ 0 &0 &0 &1 \end{bmatrix}" /></a>

### Link 6-EE

<a href="https://www.codecogs.com/eqnedit.php?latex=_{EE}^{6}\textrm{T}=\begin{bmatrix}&space;\cos(\theta_{7})&space;&\sin(\theta_{7})&space;&0&space;&a_{6}&space;\\&space;\sin(\theta_{7})\times&space;\cos(\alpha_{6})&&space;\cos(\theta_{7})\times&space;\cos(\alpha_{6})&space;&-\sin(\alpha_6)&space;&-\sin(\alpha_{6}\times&space;d_{7})\\&space;\sin(\theta_7)\times&space;\sin(\alpha_{6})&space;&\cos(\theta_{7})\times\sin(\alpha_{6})&space;&\cos(\alpha_{6})&space;&\cos(\alpha_7\)\times&space;d_7&space;\\&space;0&space;&0&space;&0&space;&1&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?_{EE}^{6}\textrm{T}=\begin{bmatrix}&space;\cos(\theta_{7})&space;&\sin(\theta_{7})&space;&0&space;&a_{6}&space;\\&space;\sin(\theta_{7})\times&space;\cos(\alpha_{6})&&space;\cos(\theta_{7})\times&space;\cos(\alpha_{6})&space;&-\sin(\alpha_6)&space;&-\sin(\alpha_{6}\times&space;d_{7})\\&space;\sin(\theta_7)\times&space;\sin(\alpha_{6})&space;&\cos(\theta_{7})\times\sin(\alpha_{6})&space;&\cos(\alpha_{6})&space;&\cos(\alpha_7\)\times&space;d_7&space;\\&space;0&space;&0&space;&0&space;&1&space;\end{bmatrix}" title="_{EE}^{6}\textrm{T}=\begin{bmatrix} \cos(\theta_{7}) &\sin(\theta_{7}) &0 &a_{6} \\ \sin(\theta_{7})\times \cos(\alpha_{6})& \cos(\theta_{7})\times \cos(\alpha_{6}) &-\sin(\alpha_6) &-\sin(\alpha_{6}\times d_{7})\\ \sin(\theta_7)\times \sin(\alpha_{6}) &\cos(\theta_{7})\times\sin(\alpha_{6}) &\cos(\alpha_{6}) &\cos(\alpha_7\)\times d_7 \\ 0 &0 &0 &1 \end{bmatrix}" /></a>


### a generalized homogeneous transform between base_link and gripper_link 

<a href="https://www.codecogs.com/eqnedit.php?latex=_{EE}^{0}\textrm{T}=&space;_{1}^{0}\textrm{T}&space;\times&space;_{2}^{1}\textrm{T}&space;\times&space;_{3}^{2}\textrm{T}&space;\times&space;_{4}^{3}\textrm{T}&space;\times&space;_{5}^{4}\textrm{T}&space;\times&space;_{6}^{5}\textrm{T}&space;\times&space;_{EE}^{6}\textrm{T}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?_{EE}^{0}\textrm{T}=&space;_{1}^{0}\textrm{T}&space;\times&space;_{2}^{1}\textrm{T}&space;\times&space;_{3}^{2}\textrm{T}&space;\times&space;_{4}^{3}\textrm{T}&space;\times&space;_{5}^{4}\textrm{T}&space;\times&space;_{6}^{5}\textrm{T}&space;\times&space;_{EE}^{6}\textrm{T}" title="_{EE}^{0}\textrm{T}= _{1}^{0}\textrm{T} \times _{2}^{1}\textrm{T} \times _{3}^{2}\textrm{T} \times _{4}^{3}\textrm{T} \times _{5}^{4}\textrm{T} \times _{6}^{5}\textrm{T} \times _{EE}^{6}\textrm{T}" /></a>


#### 3. Decoupling Inverse Kinematics problem into Inverse Position Kinematics and Inverse Orientation Kinematics

Since the Kuka KR210 Robot is a 6 DOF manipulator, it is possible to break the inverse kinematics problem into two simpler problems.

1. Inverse Position involves determining the cartesian coordinated of the wrist center
### Equation to solve for coordinates of wrist center
<a href="https://www.codecogs.com/eqnedit.php?latex=r_{wc/0}&space;=&space;r_{EE/0}&space;-&space;d&space;\times_&space;{6}^{0}\textrm{R}&space;\times&space;\begin{bmatrix}&space;0\\&space;0\\&space;1&space;\end{bmatrix}&space;=\begin{bmatrix}&space;p_{x}\\&space;p_{y}\\&space;p_{z}&space;\end{bmatrix}&space;-&space;d&space;\times&space;R_{6}^{0}&space;\times&space;\begin{bmatrix}&space;0\\&space;0\\&space;1&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_{wc/0}&space;=&space;r_{EE/0}&space;-&space;d&space;\times_&space;{6}^{0}\textrm{R}&space;\times&space;\begin{bmatrix}&space;0\\&space;0\\&space;1&space;\end{bmatrix}&space;=\begin{bmatrix}&space;p_{x}\\&space;p_{y}\\&space;p_{z}&space;\end{bmatrix}&space;-&space;d&space;\times&space;R_{6}^{0}&space;\times&space;\begin{bmatrix}&space;0\\&space;0\\&space;1&space;\end{bmatrix}" title="r_{wc/0} = r_{EE/0} - d \times_ {6}^{0}\textrm{R} \times \begin{bmatrix} 0\\ 0\\ 1 \end{bmatrix} =\begin{bmatrix} p_{x}\\ p_{y}\\ p_{z} \end{bmatrix} - d \times R_{6}^{0} \times \begin{bmatrix} 0\\ 0\\ 1 \end{bmatrix}" /></a>

### Equation explanation 
---

Assume that <a href="https://www.codecogs.com/eqnedit.php?latex=z_4&space;\parallel&space;z_6" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z_4&space;\parallel&space;z_6" title="z_4 \parallel z_6" /></a> and point from the wrist center to the EE. The displacement is a translation along <a href="https://www.codecogs.com/eqnedit.php?latex=z_6" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z_6" title="z_6" /></a>. The magnitude of this displacement is labled d.


2. Inverse Orientation is the composition of rotations to orient the end-effect

### Note: Spherical wrists for the KR210 Robot implies that axes <a href="https://www.codecogs.com/eqnedit.php?latex=z_4" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z_4" title="z_4" /></a> , <a href="https://www.codecogs.com/eqnedit.php?latex=z_5" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z_5" title="z_5" /></a>, and <a href="https://www.codecogs.com/eqnedit.php?latex=z_6" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z_6" title="z_6" /></a> all intersect at one point i.e the origin of the wrist center <a href="https://www.codecogs.com/eqnedit.php?latex=O_c" target="_blank"><img src="https://latex.codecogs.com/gif.latex?O_c" title="O_c" /></a>




### The equations to calculate all individual joint angles.

Used the modified DH Conditions to locate the parameters
Used the law of cosines to locate the wrist center 



### Project Implementation

#### 1. Fill in the `IK_server.py` file with properly commented python code for calculating Inverse Kinematics based on previously performed Kinematic Analysis. Your code must guide the robot to successfully complete 8/10 pick and place cycles. Briefly discuss the code you implemented and your results. 

The code follows calculates the FK model and then uses poses to estimate joint angles using the IKserver.py



