from pymycobot.mycobot import MyCobot
import time
import json

mc = MyCobot('/dev/ttyAMA0',1000000)
mc.power_on()

trial_set=[]

current_angle=mc.get_angles()
print('robot current pose %s'%mc.get_angles())

num=input('Enter how many poses needed... ');trials=0

while trials < num:
    mc.release_all_servos()

    print('go to the pick pose =>');time.sleep(2);print('wait...');time.sleep(1)
    pose=mc.get_angles()
    print('pose recorded >>>',pose)
    trial_set.append(pose)
    
    trials+=1
print('trial set %s'%trial_set)
# store the values in a json file

with open('demo_data.json','w') as f:
    json.dump(trial_set,f, indent=4)

