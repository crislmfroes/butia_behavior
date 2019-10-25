#!/usr/bin/env python
# coding: utf-8
import rospy
import smach
from butia_behavior.machines import getGoToFixedMachine, getGoToGripperMachine, getOpenGripperMachine, getCloseGripperMachine
from butia_behavior.states import WaitTopicState, WaitTimeState

if __name__ == '__main__':
  rospy.init_node('help_me_carry_node')
  sm = smach.StateMachine(outcomes=['succeeded', 'aborted', 'preempted'])
  with sm:
    smach.StateMachine.add(
      'WAIT_HELLO',
      WaitTopicState('butia_speech/bhd/detected'),
      transitions={
        'succeeded': 'GOTO_GRIPPER_INITIAL',
        'error': 'GOTO_GRIPPER_INITIAL'
      }
    )
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
        'succeeded': 'WAIT_TIME',
        'error': 'aborted'
        }
    )
    smach.StateMachine.add(
        'WAIT_TIME',
        WaitTimeState(10),
        transitions={
          'succeeded': 'CLOSE_GRIPPER',
          'error': 'aborted'
        }
    )
    smach.StateMachine.add(
        'CLOSE_GRIPPER',
        getCloseGripperMachine(),
        transitions={
        'succeeded': 'GOTO_1',
        'error': 'aborted'
        }
    )
    sm1 = getGoToFixedMachine('exit')
    smach.StateMachine.add('GOTO_1', sm1, transitions={
      'succeeded': 'GOTO_GRIPPER_FIRST',
      'aborted': 'aborted',
      'preempted': 'preempted'
    })
    smach.StateMachine.add(
        'GOTO_GRIPPER_FIRST',
        getGoToGripperMachine(1),
        transitions={
        'succeeded': 'OPEN_GRIPPER2',
        'error': 'aborted'
        }
    )
    smach.StateMachine.add(
        'OPEN_GRIPPER2',
        getOpenGripperMachine(),
        transitions={
        'succeeded': 'GOTO_2',
        'error': 'aborted'
        }
    )
    sm2 = getGoToFixedMachine('living_room')
    smach.StateMachine.add('GOTO_2', sm2, transitions={
      'succeeded': 'succeeded',
      'aborted': 'aborted',
      'preempted': 'preempted'
    })

  outcome = sm.execute()