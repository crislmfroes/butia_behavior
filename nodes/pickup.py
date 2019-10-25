#!/usr/bin/env python
import rospy
import smach

from butia_behavior.machines import getPickUpMachine

if __name__ == '__main__':
  rospy.init_node('pickup')
  sm = smach.StateMachine(outcomes=['succeeded', 'error'])
  with sm:
    sm1 = getPickUpMachine()
    smach.StateMachine.add('PICKUP', sm1, transitions={
      'succeeded': 'succeeded',
      'error': 'error'
    })

  outcome = sm.execute()