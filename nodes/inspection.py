#!/usr/bin/env python
# coding: utf-8
import rospy
import smach
from butia_behavior.machines import getWaitDoorMachine, getGoToFixedMachine
from butia_behavior.states import SaySomethingState
from butia_behavior.states import WaitTopicState

if __name__ == '__main__':
  rospy.init_node('inspection')
  sm = smach.StateMachine(outcomes=['succeeded', 'aborted', 'preempted'])
  with sm:
    sm1 = getWaitDoorMachine()
    smach.StateMachine.add('WAIT_DOOR', sm1, transitions={
      'succeeded': 'GOTO_1',
      'error': 'aborted',
    })
    sm2 = getGoToFixedMachine('examination')
    smach.StateMachine.add('GOTO_1', sm2, transitions={
      'succeeded': 'WAIT_HELLO',
      'aborted': 'aborted',
      'preempted': 'preempted'
    })
    smach.StateMachine.add(
      'WAIT_HELLO',
      WaitTopicState('butia_speech/bhd/detected'),
      transitions={
        'succeeded': 'GOTO_2',
        'error': 'aborted'
      }
    )
    sm3 = getGoToFixedMachine('exit')
    smach.StateMachine.add('GOTO_2', sm3, transitions={
      'succeeded': 'succeeded',
      'aborted': 'aborted',
      'preempted': 'preempted'
    })
  outcome = sm.execute()