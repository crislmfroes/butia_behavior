#!/usr/bin/env python
# coding: utf-8
import rospy
import smach
from butia_behavior.states import SaySomethingState
from butia_behavior.states import WaitTopicState

if __name__ == '__main__':
  rospy.init_node('good_morning_rs')
  sm = smach.StateMachine(outcomes=['succeeded', 'error'])
  with sm:
    sm1 = getGoToFixedMachine('interview')
    smach.StateMachine.add('GOTO_1', sm1, transitions={
      'succeeded': 'WAIT_HELLO',
      'aborted': 'aborted',
      'preempted': 'preempted'
    })
    smach.StateMachine.add(
      'WAIT_HELLO',
      WaitTopicState('butia_speech/bhd/detected'),
      transitions={
        'succeeded': 'GOOD_MORNING',
        'error': 'error'
      }
    )
    smach.StateMachine.add(
      'GOOD_MORNING',
      SaySomethingState('Olá pessoal do Bom Dia Rio Grande, venham para o Robótica 2019.'),
      transitions={
        'succeeded': 'succeeded',
        'error': 'error'
      }
    )
  outcome = sm.execute()