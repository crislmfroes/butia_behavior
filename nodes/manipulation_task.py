#!/usr/bin/env python
import rospy
import smach
import operator

from butia_behavior.machines import getWaitDoorMachine, getGoToFixedMachine, getPickUpMachine, getHandOverMachine
from butia_behavior.states import SaySomethingState

def average(counts):
  return reduce(operator.add, counts) / len(counts)

if __name__ == '__main__':
  rospy.init_node('manipulation_task')
  sm = smach.StateMachine(outcomes=['succeeded', 'aborted', 'preempted'])
  with sm:
    sm1 = getWaitDoorMachine()
    smach.StateMachine.add('WAIT_DOOR', sm1, transitions={
      'succeeded': 'GOTO_1',
      'error': 'aborted',
    })
    sm2 = getGoToFixedMachine('pickup')
    smach.StateMachine.add('GOTO_1', sm2, transitions={
      'succeeded': 'PICKUP',
      'aborted': 'aborted',
      'preempted': 'preempted'
    })
    sm3 = getPickUpMachine()
    smach.StateMachine.add('PICKUP', sm3, transitions={
      'succeeded': 'GOTO_2',
      'error': 'aborted'
    })
    sm4 = getGoToFixedMachine('handover')
    smach.StateMachine.add('GOTO_2', sm4, transitions={
      'succeeded': 'HANDOVER',
      'aborted': 'aborted',
      'preempted': 'preempted'
    })
    sm5 = getHandOverMachine()
    smach.StateMachine.add('HANDOVER', sm5, transitions={
      'succeeded': 'GOTO_3',
      'error': 'aborted'
    })
    sm6 = getGoToFixedMachine('exit')
    smach.StateMachine.add('GOTO_3', sm6, transitions={
      'succeeded': 'succeeded',
      'aborted': 'aborted',
      'preempted': 'preempted'
    })
  outcome = sm.execute()
