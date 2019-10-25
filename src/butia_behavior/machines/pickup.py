import smach

import rospy

from goto_gripper import getGoToGripperMachine
from open_gripper import getOpenGripperMachine
from close_gripper import getCloseGripperMachine

def getPickUpMachine():
  sm = smach.StateMachine(outcomes=['succeeded', 'error'])
  with sm:
    smach.StateMachine.add(
        'GOTO_GRIPPER_INITIAL',
        getGoToGripperMachine(0),
        transitions={
        'succeeded': 'OPEN_GRIPPER',
        'error': 'error'
        }
    )
    smach.StateMachine.add(
        'OPEN_GRIPPER',
        getOpenGripperMachine(),
        transitions={
        'succeeded': 'GOTO_GRIPPER_FIRST',
        'error': 'error'
        }
    )
    smach.StateMachine.add(
        'GOTO_GRIPPER_FIRST',
        getGoToGripperMachine(1),
        transitions={
        'succeeded': 'GOTO_GRIPPER_SECOND',
        'error': 'error'
        }
    )
    smach.StateMachine.add(
        'GOTO_GRIPPER_SECOND',
        getGoToGripperMachine(2),
        transitions={
        'succeeded': 'CLOSE_GRIPPER',
        'error': 'error'
        }
    )
    smach.StateMachine.add(
        'CLOSE_GRIPPER',
        getCloseGripperMachine(),
        transitions={
        'succeeded': 'succeeded',
        'error': 'error'
        },
    )
    
  return sm
