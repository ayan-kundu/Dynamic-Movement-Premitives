#!/usr/bin/env python3

"""
This package need `pymycobot`.
This file for test the API if right.
Just can run in Linux.
"""

from pymycobot.mycobot import MyCobot
import time
# from its orihinal version file
import random, subprocess
from pymycobot.genre import Angle, Coord


mc = MyCobot('/dev/ttyAMA0',1000000)
mc.power_on()


#mc.send_angles([0,0,0,0,0,0],70)
time.sleep (1)

if __name__ == "__main__":
  for turn in range (4):

    #for ele in range (1,7,1):
      #print('joint id --> %s max value --> %s'%(ele,mc.get_joint_max(ele)))

    print('::Joint angles... %s'%(mc.get_angles()))
    print('::Rotational coordinates... %s'%(mc.get_coords()))
  
    print("Start check api")

    print("::get_angles()")
    print("==> degrees: %s"%(mc.get_angles()))
    time.sleep(0.5)

    print("::get_radians()")
    print("==> radians: %s"%(mc.get_radians()))
    time.sleep(0.5)

    print("::send_angles()")
    mc.send_angles([-90, 0, 0, 0, 0, 0], 70)
    print("==> set angles [-90,0,0,0,0,0], speed 80")
    if mc.is_moving()== 1:
      status='YES'
    else:
      status='NO'
    print("Is moving: %s "%(status))
    time.sleep(3)

    print("::send_radians");radian_list=[1, 1, 1, 1, 1, 1]
    mc.send_radians(radian_list, 70)
    print("==> set raidans [1,1,1,1,1,1], speed 70")
    print('==> equivlant degree angles %s'%(mc.get_angles()))
    time.sleep(2)

    print("::send_angle()")
    mc.send_angle(Angle.J2.value, 10, 50)
    print("==> angle: joint2, degree: 10, speed: 50")
    time.sleep(1)

    print("::get_coords()")
    print("==> coords %s"%(mc.get_coords()))
    time.sleep(0.5)

    print("::send_coords()")
    coord_list = [160, 160, 160, 0, 0, 0]
    mc.send_coords(coord_list, 70, 0)
    print("==> send coords [160,160,160,0,0,0], speed 70, mode 0\n")
    time.sleep(3.0)

    print('is in position -->',mc.is_in_position(coord_list, 1))
    time.sleep(1)

    print("::send_coord() ...")
    #mc.send_coord(Coord.X.value, -40, 70)
    print("==> send coord id: X, coord value: -40, speed: 70\n")
    time.sleep(2)

    print("::release_all_servos()")
    #mc.release_all_servos()
    print("==> into free moving mode.")
    print("=== check end <==")
