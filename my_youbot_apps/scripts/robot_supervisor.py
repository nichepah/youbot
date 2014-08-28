#!/usr/bin/env python

'''
@author: Rick Candell
@organization: NIST
@contact: rick.candell@nist.gov
@license: MIT
'''

import sys
import copy
import rospy
import math
from abc import ABCMeta, abstractmethod
from brics_actuator.msg import JointPositions, JointValue
from my_youbot_msgs.srv import JointTrajectoryRequest

class LegacyJointPositions(object):
  # Robot 1 is the LEFT HAND one close to computer.
  # Robot 2 is the RIGHT HAND one far from computer.
  prepick_rob2 = [2.945,1.5,-1.62,3.13,2.94]  
  pick_rob2 = [2.945,1.89,-1.62,3.13,4.5]  
  cand = [2.94,1.0,-2.1,1.8,2.94] # candle
  trans1 = [1.4,0.71,-2.0,3.3,2.9489] # Rob1 prepares for giving it to Rob2
  pretrans2 = [4.0,1.35,-1.94,2.4,1.39] # Rob2 gets ready to receive the ball
  trans2 = [4.5,1.35,-1.94,2.41,1.39] # Rob2 takes ball from Rob1 
  posttrans2 = [4.5,0.9,-1.94,2.4,1.39] # Rob2 moves out the way
  premach2 = [1.93, 0.55, -1.3, 2.5, 2.95] # Machine 2 pre spot, it is right after loading point Rob2 uses it
  mach2 = [1.93, 1.05, -1.3, 3.16, 2.95] # Machine 2 spot, it is right after loading point. Rob2 uses it
  preload = [1.37, 1.15, -1.7, 2.83, 2.95] # Loading pre point. Rob 2 uses it
  load = [1.37, 1.55, -1.7, 2.83, 2.95] # Loading point. Rob 2 uses it
  premach1 = [2.22, 0.35, -2.34, 0.92, 2.95] # Machine 1 pre spot. Rob1 uses it
  mach1 = [2.22, 0.05, -2.34, 0.92, 2.95] # Machine 1 spot. Rob1 uses it
  prepick_rob1 = [2.96, 1.36, -1.62, 3.07, 2.94] # Robot 1 is the left hand one. This is the pre pickup spot 
  pick_rob1 = [2.96, 1.96, -1.62, 3.07, 2.94] # Robot 1 is the left hand one. This is the pickup spot 
  ready_tight_spot = [3.8, 1.2, -0.02, 0.8, 2.93] # PRE-PRE tight spot, gets ready for *ANY* operation involving the tight spot.
  # IMPORTANT: ready_tight_spot should also be done AFTER operation as well as getting ready before it.
  pretight_spot_place = [3.8, 1.75, -0.7, 0.85, 2.929] # Pre tight spot for placing. Note identical to post-tight-spot-place.
  # IMPORTANT: picking up from the tight spot doesn't require a pretight_spot!!
  tight_spot = [3.8, 1.85, -0.9, 0.96, 2.929] # tight spot
  posttight_spot_pickA = [3.8, 1.85, -0.9, 0.90, 2.929] # First post tight spot after picking (lifts it a bit)
  posttight_spot_pickB = [4.5, 1.85, -0.9, 0.90, 2.929] # Second post tight spot after picking (clears the spot)
  posttight_spot_place = [3.8, 1.75, -0.7, 0.85, 2.929] # Post tight spot for placing. Note identical to pre-tight-spot-place
  opening = 22 # opening gap in mm
  closing = 9 # closing gap in mm. DO NOT REDUCE BELOW 8 mm! Gripper finger(s) may become out of place from biting too hard.
  SPECIAL = [3.8, 1.75, -0.7, 0.85, 2.929] # USE FOR TESTING

class Command(object):
  def __init__(self, robot_id):

class CommandSequence(object):
  def __init__(self):
    self._database = []
    self._database.append(Command())

class YoubotGazeboSupervisor(object):
  __node_name = "youbot_supervisor"
  def __init__(self):
    
    self._command_sequence = CommandSequence()
    
    # initialize this ROS node
    rospy.init_node(self._node_name, anonymous=False)    
    rospy.loginfo("proxy node initialized: " + rospy.get_name())
    
  def load_command_db(self):
    

# This is the main subroutine
if __name__=='__main__':
  try:  
    sup = YoubotGazeboSupervisor()
  except Exception as e:
    rospy.logerr(e)
    pass   
  
  
  