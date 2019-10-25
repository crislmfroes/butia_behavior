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
        'succeeded': 'WAIT_TIME',
        'error': 'WAIT_TIME'
      }
    )
    smach.StateMachine.add(
        'WAIT_TIME',
        WaitTimeState(10),
        transitions={
          'succeeded': 'GOTO_1',
          'error': 'aborted'
        }
    )
    sm1 = getGoToFixedMachine('exit')
    smach.StateMachine.add('GOTO_1', sm1, transitions={
      'succeeded': 'WAIT_HELLO2',
      'aborted': 'aborted',
      'preempted': 'preempted'
    })
    smach.StateMachine.add(
      'WAIT_HELLO2',
      WaitTopicState('butia_speech/bhd/detected'),
      transitions={
        'succeeded': 'GOTO_2',
        'error': 'GOTO_2'
      }
    )
    sm2 = getGoToFixedMachine('living_room')
    smach.StateMachine.add('GOTO_2', sm2, transitions={
      'succeeded': 'succeeded',
      'aborted': 'aborted',
      'preempted': 'preempted'
    })

  outcome = sm.execute()