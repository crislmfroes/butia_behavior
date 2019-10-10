#!/usr/bin/env python3
import rospy
import smach

from butia_behavior.states import WaitTopicState

if __name__ == '__main__':
  rospy.init_node('boiler_plate_machine')
  sm = smach.StateMachine(outcomes=['succeeded', 'error'])
  with sm:
    smach.StateMachine.add(
      'WAIT_HOTWORD',
      WaitTopicState('butia_speech/hotword'),
      transitions={
        'succeeded': 'succeeded',
        'error': 'error'
      }
    )
  outcome = sm.execute()
