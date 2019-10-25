#!/usr/bin/env python
import rospy
import smach

from butia_behavior.machines import getPickUpMachine, getHandOverMachine

if __name__ == '__main__':
  rospy.init_node('pickup')
  sm = smach.StateMachine(outcomes=['succeeded', 'error'])
  with sm:
    sm1 = getPickUpMachine()
    smach.StateMachine.add('PICKUP', sm1, transitions={
      'succeeded': 'HANDOVER',
      'error': 'error'
    })
    sm2 = getHandOverMachine()
    smach.StateMachine.add('HANDOVER', sm2, transitions={
      'succeeded': 'succeeded',
      'error': 'error'
    })

  outcome = sm.execute()
