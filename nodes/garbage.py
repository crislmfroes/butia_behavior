#!/usr/bin/env python
# coding: utf-8
import rospy
import smach
from butia_behavior.machines import getWaitDoorMachine, getGoToFixedMachine, getGoToGripperMachine, getOpenGripperMachine, getCloseGripperMachine
from butia_behavior.states import WaitTopicState, WaitTimeState, SaySomethingState

if __name__ == '__main__':
  rospy.init_node('garbage_node')
  sm = smach.StateMachine(outcomes=['succeeded', 'aborted', 'preempted'])
  with sm:
    smach.StateMachine.add(
      'WAIT_DOOR',
      getWaitDoorMachine(),
      transitions={
        'succeeded': 'GOTO_1',
        'error': 'aborted'
      }
    )
    sm1 = getGoToFixedMachine('garbage1')
    smach.StateMachine.add('GOTO_1', sm1, transitions={
      'succeeded': 'GOTO_GRIPPER_INITIAL',
      'aborted': 'aborted',
      'preempted': 'preempted'
    })
    smach.StateMachine.add(
        'GOTO_GRIPPER_INITIAL',
        getGoToGripperMachine(0),
        transitions={
        'succeeded': 'OPEN_GRIPPER',
        'error': 'aborted'
        }
    )
    smach.StateMachine.add(
        'OPEN_GRIPPER',
        getOpenGripperMachine(),
        transitions={
          'succeeded': 'CLOSE_GRIPPER',
          'error': 'aborted'
        }
    )
    smach.StateMachine.add(
      'CLOSE_GRIPPER',
      getCloseGripperMachine(),
      transitions={
        'succeeded': 'GOTO_2',
        'error': 'aborted'
      }
    )
    sm2 = getGoToFixedMachine('exit')
    smach.StateMachine.add('GOTO_2', sm2, transitions={
      'succeeded': 'OPEN_GRIPPER2',
      'aborted': 'aborted',
      'preempted': 'preempted'
    })
    smach.StateMachine.add(
        'OPEN_GRIPPER2',
        getOpenGripperMachine(),
        transitions={
          'succeeded': 'GOTO_3',
          'error': 'aborted'
        }
    )
    sm3 = getGoToFixedMachine('garbage2')
    smach.StateMachine.add('GOTO_3', sm3, transitions={
      'succeeded': 'CLOSE_GRIPPER2',
      'aborted': 'aborted',
      'preempted': 'preempted'
    })
    smach.StateMachine.add(
      'CLOSE_GRIPPER2',
      getCloseGripperMachine(),
      transitions={
        'succeeded': 'GOTO_4',
        'error': 'aborted'
      }
    )
    sm4 = getGoToFixedMachine('exit')
    smach.StateMachine.add('GOTO_4', sm4, transitions={
      'succeeded': 'OPEN_GRIPPER3',
      'aborted': 'aborted',
      'preempted': 'preempted'
    })
    smach.StateMachine.add(
        'OPEN_GRIPPER3',
        getOpenGripperMachine(),
        transitions={
          'succeeded': 'GOTO_5',
          'error': 'aborted'
        }
    )
    sm5 = getGoToFixedMachine('living_room')
    smach.StateMachine.add('GOTO_5', sm5, transitions={
      'succeeded': 'succeeded',
      'aborted': 'aborted',
      'preempted': 'preempted'
    })

  outcome = sm.execute()
