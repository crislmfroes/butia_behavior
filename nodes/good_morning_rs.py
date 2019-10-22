#!/usr/bin/env python3
import rospy
import smach
from butia_behavior.states import SaySomethingState

if __name__ == '__main__':
  rospy.init_node('presentation_1')
  sm = smach.StateMachine(outcomes=['succeeded', 'error'])
  with sm:
    smach.StateMachine.add(
      'INTRODUCE',
      SaySomethingState('Olá pessoal do Bom Dia Rio Grande, venham para o Robótica 2019.'),
      transitions={
        'succeeded': 'succeeded',
        'error': 'error'
      }
    )
  outcome = sm.execute()