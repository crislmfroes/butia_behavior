import smach

import rospy

from butia_behavior.states import SetFixedQueryState, GetTargetPoseState, GoToState
from goto import getGoToMachine

def getGoToFixedMachine(target):
  sm = smach.StateMachine(outcomes=['succeeded', 'aborted', 'preempted', 'arrived'])
  with sm:
    smach.StateMachine.add(
        'SET_KEY',
        SetFixedQueryState(target),
        transitions={
        'succeeded': 'GOTO',
        'error': 'aborted'
        },
        remapping={
          'query':'key'
        }
    )
    smach.StateMachine.add(
      'GOTO',
      getGoToMachine(),
      transitions={
        'succeeded': 'succeeded',
        'aborted': 'aborted',
        'preempted': 'preempted',
        'arrived': 'arrived'
      },
      remapping={
        'key': 'key'
      }
    )
  return sm
