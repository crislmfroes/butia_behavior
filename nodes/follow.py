#!/usr/bin/env python
import rospy
import smach

from butia_behavior.machines import getFollowPersonMachine

if __name__ == '__main__':
  rospy.init_node('follow')
  sm = smach.StateMachine(outcomes=['succeeded', 'aborted', 'preempted'])
  with sm:
    ###
    sm1 = getFollowPersonMachine()
    smach.StateMachine.add('FOLLOW', sm1, transitions={
      'succeeded': 'succeeded',
      'aborted': 'aborted',
      'preempted': 'preempted'
    })
  outcome = sm.execute()
