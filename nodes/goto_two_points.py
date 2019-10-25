#!/usr/bin/env python
import rospy
import smach

from butia_behavior.machines import getGoToFixedMachine

if __name__ == '__main__':
  rospy.init_node('goto_two_points')
  sm = smach.StateMachine(outcomes=['succeeded', 'aborted', 'preempted'])
  with sm:
    ###
    sm1 = getGoToFixedMachine('nautec')
    smach.StateMachine.add('GOTO_1', sm1, transitions={
      'succeeded': 'GOTO_2',
      'aborted': 'aborted',
      'preempted': 'preempted'
    })
    ###
    sm2 = getGoToFixedMachine('fbot')
    smach.StateMachine.add('GOTO_2', sm2, transitions={
      'succeeded': 'GOTO_1',
      'aborted': 'aborted',
      'preempted': 'preempted'
    })
  outcome = sm.execute()