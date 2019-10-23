#!/usr/bin/env python
import rospy
import smach
import operator

from butia_behavior.machines.classes_count import getClassesCountMachine

def average(counts):
  return reduce(operator.add, counts) / len(counts)

if __name__ == '__main__':
  rospy.init_node('object_counter')
  sm = smach.StateMachine(outcomes=['succeeded', 'error'])
  with sm:
    sm1 = getClassesCountMachine('butia_vision/or/people_detection', 2, average)
    smach.StateMachine.add(
      'COUNT_OBJECTS',
      sm1,
      transitions={
        'succeeded': 'succeeded',
        'error': 'error'
      }
    )
  outcome = sm.execute()
