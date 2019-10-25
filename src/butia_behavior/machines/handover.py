import smach

import rospy

from goto_gripper import getGoToGripperMachine
from open_gripper import getOpenGripperMachine
from close_gripper import getCloseGripperMachine

def getHandOverMachine():
  sm = smach.StateMachine(outcomes=['succeeded', 'error'])
  with sm:
    smach.StateMachine.add(
        'OPEN_GRIPPER',
        getOpenGripperMachine(),
        transitions={
        'succeeded': 'GOTO_GRIPPER_FIRST2',
        'error': 'error'
        }
    )
    smach.StateMachine.add(
        'GOTO_GRIPPER_FIRST2',
        getGoToGripperMachine(1),
        transitions={
        'succeeded': 'GOTO_GRIPPER_INITIAL2',
        'error': 'error'
        }
    )
    smach.StateMachine.add(
        'GOTO_GRIPPER_INITIAL2',
        getGoToGripperMachine(0),
        transitions={
        'succeeded': 'succeeded',
        'error': 'error'
        }
    )
    
  return sm
