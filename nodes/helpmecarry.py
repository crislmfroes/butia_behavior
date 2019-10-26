#!/usr/bin/env python
# coding: utf-8
import rospy
import smach
from butia_behavior.machines import getFollowPersonMachine, getGoToFixedMachine, getGoToGripperMachine, getOpenGripperMachine, getCloseGripperMachine
from butia_behavior.states import WaitTopicState, WaitTimeState

if __name__ == '__main__':
  rospy.init_node('help_me_carry_node')
  sm = smach.StateMachine(outcomes=['succeeded', 'aborted', 'preempted', 'arrived'])
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
        'succeeded': 'WAIT_TIME',
        'error': 'aborted'
        }
    )
    smach.StateMachine.add(
        'WAIT_TIME',
        WaitTimeState(15),
        transitions={
          'succeeded': 'GOTO_1',
          'error': 'aborted'
        }
    )
    sm1 = getFollowPersonMachine()
    smach.StateMachine.add('GOTO_1', sm1, transitions={
      'succeeded': 'GOTO_GRIPPER_FIRST',
      'aborted': 'aborted',
      'preempted': 'preempted',
      'arrived': 'GOTO_GRIPPER_FIRST'
    })
    smach.StateMachine.add(
        'GOTO_GRIPPER_FIRST',
        getGoToGripperMachine(1),
        transitions={
        'succeeded': 'WAIT_HELLO2',
        'error': 'aborted'
        }
    )
    smach.StateMachine.add(
      'WAIT_HELLO2',
      WaitTopicState('butia_speech/bhd/detected'),
      transitions={
        'succeeded': 'GOTO_2',
        'error': 'GOTO_GRIPPER_FIRST'
      }
    )
    sm2 = getGoToFixedMachine('living_room')
    smach.StateMachine.add('GOTO_2', sm2, transitions={
      'succeeded': 'succeeded',
      'aborted': 'aborted',
      'preempted': 'preempted',
      'arrived': 'arrived'
    })

  outcome = sm.execute()
