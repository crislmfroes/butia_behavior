#!/usr/bin/env python
import rospy
import smach

from butia_behavior.machines import GoToFixedMachine

if __name__ == '__main__':
  rospy.init_node('goto_two_points')
  sm = smach.StateMachine(outcomes=['succeeded', 'aborted', 'preempted'])
  with sm:
    smach.StateMachine.add(
      'GOTO_1',
      GoToFixedMachine('nautec'),
      transitions={
        'succeeded': 'succeeded',
        'aborted': 'aborted',
        'preempted': 'preempted'
      }
    )
    # smach.StateMachine.add(
    #   'GOTO_2',
    #   GoToFixedMachine('fbot'),
    #   transitions={
    #     'succeeded': 'succeeded',
    #     'abroted': 'aborted',
    #     'preempted': 'preempted'
    #   }
    # )
  outcome = sm.execute()
