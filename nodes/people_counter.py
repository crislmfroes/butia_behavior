#!/usr/bin/env python
import rospy
import smach
import operator

from butia_behavior.machines.classes_count import getClassesCountMachine
from butia_behavior.states import SaySomethingUDState, PrepareSpeechState

def average(counts):
  return reduce(operator.add, counts) / len(counts)

if __name__ == '__main__':
  rospy.init_node('object_counter')
  sm = smach.StateMachine(outcomes=['succeeded', 'error'])
  with sm:
    sm1 = getClassesCountMachine('butia_vision/or/people_detection', 20, max)
    smach.StateMachine.add(
      'COUNT_OBJECTS',
      sm1,
      transitions={
        'succeeded': 'PREPARE_SPEECH',
        'error': 'error'
      }
    )
    smach.StateMachine.add(
      'PREPARE_SPEECH',
      PrepareSpeechState('I identified','{y} {x}', 'in the room'),
      transitions={
        'succeeded': 'SAY_SOMETHING',
        'error': 'error'
      },
      remapping={
        'registers': 'registers'
      }
    )
    smach.StateMachine.add(
      'SAY_SOMETHING',
      SaySomethingUDState(),
      transitions={
        'succeeded': 'succeeded',
        'error': 'error'
      }
    )
  outcome = sm.execute()
