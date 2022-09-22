from pymycobot.mycobot import MyCobot
import time


mc = MyCobot('/dev/ttyAMA0',1000000)
mc.power_on()

print(mc.get_angles())
print(mc.get_coords())

#pick init pose
#mc.send_angles([88.68,0,44.91,46.75,84.37,42],50) 
mc.send_angles([(-73.65),(-36.65),(-40.86),(-10.54),3.25,(-104.23)],50)
time.sleep(.5)
# pick pose
#mc.send_angles([88.68,64,44.91,46.75,84.37,42],50) 
mc.send_angles([(-73.65),(-80.33),(-40.34),24.16,(-2.02),(-114.69)],50)
print('object picked !')
time.sleep(1)
# joint 6: 39 is to make the gripper aligned vertically

# mid pose
#mc.send_angles([(-76.28),0.79,(-1.58),(-1.14),81.03,35.5],50)
mc.send_angles([(-73.65),(-5.36),(-55.54),(-5.53),(-3.25),-122],50)
time.sleep(1)
# mid place pose
#mc.send_angles([(-82.96),35.33,104.85,20.12,90.17,35.5],50)
mc.send_angles([105,(-37.96),(-55.54),(-9.93),1.66,-122],50)
time.sleep(1.4)
# place pose
#mc.send_angles([(-88.5),66.7,45.35,46.31,84.11,42],50)
mc.send_angles([105,(-80),(-41),24,0.96,(-122)],50)
print('object placed !')

# gripper opens
mc.set_gripper_value(0,70)
print('gripper set value 0 | gripper opening')
time.sleep(1.4)
# mid place pose back
mc.send_angles([105,(-37.96),(-55.54),(-9.93),1.66,-122],50)
time.sleep(1)

#pick init pose back
mc.send_angles([(-73.65),(-36.65),(-40.86),(-10.54),3.25,(-104.23)],50)

#mc.release_all_servos()