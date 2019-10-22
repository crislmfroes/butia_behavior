import smach

import rospy

from butia_behavior.states import GetKeyState, GetPoseState
from . import getGoToMachine

def getApproach2PickUpMachine(query):
  sm = smach.StateMachine.__init__(self, outcomes=['succeeded', 'aborted', 'preempted'], output_keys=['pose'])
  with sm:
    smach.StateMachine.add(
          'GET_KEY',
          GetKeyState(query),
          transitions={
          'succeeded': 'succeeded',
          'error': 'error'
          }
    )
    smach.StateMachine.add(
          'GET_TARGET_POSE',
          GetTargetPose(),
          transitions={
          'succeeded': 'succeeded',
          'error': 'error'
          }
    )
    smach.StateMachine.add(
          'GOTO',
          getGoToMachine(),
          transitions={
          'succeeded': 'succeeded',
          'aborted': 'aborted',
          'preempted': 'preempted'
          }
          remapping={
          'key': 'key'
          }
    )
    smach.StateMachine.add(
          'GET_POSE',
          GetPoseState(),
          transitions={
          'succeeded': 'succeeded',
          'error': 'error'
          }
          remapping={
          'key': 'key',
          'pose': 'pose'
          }
    )
  return sm