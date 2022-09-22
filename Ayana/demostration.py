from pymycobot.mycobot import MyCobot
import time
import json

mc = MyCobot('/dev/ttyAMA0',1000000)
mc.power_on()
trial_set=[];demo_set=[]

current_angle=mc.get_angles()
print('robot current pose %s'%mc.get_angles())

trial_num=input('Enter how many trials needed ');trials=0

# align into ready pose
ready_pose=[(-73.5),(-36.65),(-40.86),(-10.54),3.25,(-104.23)]
mc.send_angles(ready_pose,50)
print('robot in ready pose now !')
time.sleep(2)
mc.release_all_servos()
#trial_set.append(init_pose) # comment out in case of different starting 


trials=0
while trials < trial_num:
    mc.release_all_servos()
    Trajactory='Tajactory'+str(trials+1)
    trial_set.append(Trajactory) # to seperater trajctory sets

    print('go to the pick pose =>');time.sleep(4)
    pick_pose=mc.get_angles()
    print('pick pose recorded',pick_pose)
    trial_set.append(pick_pose)

    for i in range(3):
        # intermidiate and place pose
        print('go to next pose',i+1);
        time.sleep(4)
        trial_set.append(mc.get_angles())
        print('pose recorded',mc.get_angles())
        time.sleep(.5)
        i+=1

    #trial_dict={'trial':trial_set}  
    print('trial set %s ==> %s'%(trials+1,trial_set))
    print('trial set %s length:: %s'%(trials+1,len(trial_set)))
    
    demo_set.append(trial_set)
    trials+=1

    #trial_set.append(init_pose)
    mc.send_angles(ready_pose,50);time.sleep(2)

print('demonstation set length:: %s'%len(demo_set))
print(demo_set)
'''
# store the values in a json file
#Dict={'a':1}
with open('data.json','w') as f:
    json.dump(demo_set,f, indent=4)

'''
# store several trials into a single file
list_demo_set=[]

with open('demo_data.json') as f:
    list_demo_set=json.load(f)  

list_demo_set.append(demo_set)

with open('demo_data.json','w') as f:
    json.dump(list_demo_set,f,indent=4)

