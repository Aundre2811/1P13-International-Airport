ip_address =  "localhost"
project_identifier = 'P3A'
#--------------------------------------------------------------------------------
import sys
sys.path.append('../')
from Common.hardware_project_library import *
from Common.barcode_checker import *

hardware = True
arm = qarm(project_identifier,ip_address,hardware)
table = servo_table(ip_address,None,hardware)
scanner = barcode_checker()



for _ in range (4):

    x = scanner.barcode_check()
    time.sleep(2)

    if(x == "Platform"):

        arm.rotate_base(-90)
        time.sleep(1)
        arm.rotate_shoulder(-8)
        time.sleep(1)
        arm.rotate_elbow(49)
        time.sleep(1)
        arm.control_gripper(45)
        time.sleep(1)

        arm.rotate_elbow(-30)
        time.sleep(1)
        arm.move_arm(0.193, 0.0, 0.086)
        time.sleep(1)
        arm.control_gripper(-45)
        time.sleep(1)
        arm.move_arm(0.406, 0.0, 0.483)

        table.rotate_table_angle(90)
        time.sleep(1)
        table.stop()

    else:
        arm.rotate_base(-90)
        time.sleep(1)
        arm.rotate_shoulder(-8)
        time.sleep(1)
        arm.rotate_elbow(49)
        time.sleep(1)
        arm.control_gripper(45)
        time.sleep(1)

        arm.rotate_elbow(-30)
        time.sleep(1)
        arm.move_arm(0.0, 0.406, 0.483)
        time.sleep(1)
        arm.control_gripper(-45)
        time.sleep(1)
        arm.move_arm(0.406, 0.0, 0.483)

        table.rotate_table_angle(90)
        time.sleep(1)
        table.stop()
    




bot.activate_stepper_motor() #Activating rotary actuator

for _ in range (4): #Loops through 4 times

    x = scanner.barcode_check() #Checks for when barcode of luggage is scanned
    time.sleep(2) #stops for 2 seconds

    if(x == "Platform"): #Checks if the luggage is supposed to go to the platform
        arm.move_arm(-0.03, -0.44, 0.23) #Moves Q-arm to coordinate
        time.sleep(1)
        arm.control_gripper(45) #Grabs luggage using Q-arm gripper
        arm.move_arm(0.52, -0.15, 0.39)
        time.sleep(1)
        arm.control_gripper(-45) #Releases luggage
        
        time.sleep(2)
        bot.rotate_stepper_ccw(5) #Counter clockwise rotation for 5 seconds to unravel the section of ramp
        time.sleep(4)
        bot.rotate_stepper_ccw(5)
        time.sleep(4)
        bot.rotate_stepper_ccw(5)
        time.sleep(4)
        bot.rotate_stepper_cw(5) #Clockwise rotation for 5 seconds, returning ramps to initial position
        time.sleep(2)
        bot.rotate_stepper_cw(5)
        time.sleep(2)
        bot.rotate_stepper_cw(5)
        time.sleep(2)
        
        table.rotate_table_angle(90)
        time.sleep(1)
        table.stop()
        
        
        
    else: #If luggage is supposed to go to the rejection bin
        arm.move_arm(-0.03, -0.44, 0.23)
        time.sleep(1)
        arm.control_gripper(45)
        arm.move_arm(0.0, 0.47, 0.15)
        time.sleep(1)
        arm.control_gripper(-45)
        
        table.rotate_table_angle(90)
        time.sleep(1)
        table.stop()











    

