# Dynamic-Movement-Premitives:DMP
## >>This repo is based on Imitation Learning using Learning from Demonstration(LfD)<<

### Refer to [Setup Mycobot](https://github.com/ayan-kundu/Mycobot-280-pi) to set up the robot 
### Step by Step guidance to work with LfD, in this case it's DMP:
  1. Get the catkinworkspace ready. Focus on 'dmp' dir here for that
  2. launch dmp.launch. Make sure there remains no same name file.
  3. open terminal run the python file: dmp_test.py If you name it dmp.py it will make confusion in the ROS so it's better you name it other than dmp.py for sure
  4. when launch file is running, then only this python file will work as it will call required services when launch is ready.
  5. Feed Demonstation trajectoy to the model when you run it. It also requires to take a new pick and place pose you want the robot to follow.
  6. It will learn from the demo and will give you a suitable trajectory starting from your given pick and ending with the given place pose.
  
  The learning model is Dynamic Premitive Movement model.It takes a single trajetory and tries to learn from that.That is the drawback in case of perturbation. Having a look at the learning graphs attached, you can figure out that the model is working well. 
### Insight of the Imitation learning: ###

1. **Learning from Demonstration(LfD):-**

***Application1:-*** **Pick and place**

The graphs I attached is made using pic and place operation. These graphs shows a good amount of imitation learning, the robot is capable of.
Attach pic

- [x] In Pick and place I got an idea of Food unloading to a dish from a microwave where pick pose would be the food inside the microwave and the place pose would be the plate position.

**_Demonstration_:-**
![demo]()

**_Learning curves_:-**
![curves]()

***Application2:-*** **Wave gesture**

It is able to imitate hand wave trajectory. So if I put a palm structure on it gripper it can wave from any position and it will carry on waving for a certain time irrespective if its initial body pose. 

  **_Demonstration_:-**
  ![demo]()





2. **Dmp visualisation:-**

![Show outputs]()

![Show plots]()

![Attach pic]()

3. **Wellknown Gripper Issue**
:+1:_Gripper not working issue solved!_ 
```
is_gripper_moving
0
```
:+1:Burn ATOM to its latest version 4.2**
```
is_gripper_moving
1

OTHERWISE, try change gripper
```
> What's Coming next: putting vision in it 

With computer vision(Employing a camera on ATOM) it would automatically pick (no need to give pick position anymore) and place to the given place position. 
