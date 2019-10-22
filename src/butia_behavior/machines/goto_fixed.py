import smach

import rospy

from butia_behavior.states import SetFixedTargetKeyState, GetPoseState, GoToState

def getGoToFixedMachine(target):
  sm = smach.StateMachine(outcomes=['succeeded', 'aborted', 'preempted'])
  with sm:
    smach.StateMachine.add(
        'SET_KEY',
        SetFixedTargetKeyState(target),
        transitions={
        'succeeded': 'GET_POSE',
        'error': 'aborted'
        }
    )
    smach.StateMachine.add(
        'GET_POSE',
        GetPoseState(),
        transitions={
        'succeeded': 'GOTO',
        'error': 'aborted'
        }
    )
    smach.StateMachine.add(
        'GOTO',
        GoToState(),
        transitions={
        'succeeded': 'succeeded',
        'aborted': 'aborted',
        'preempted': 'preempted'
        }
    )
  return sm

# class GoToFixedMachine(smach.StateMachine):
#   def __init__(self, node_name, target):
#       smach.StateMachine.__init__(self, outcomes=['succeeded','aborted','preempted'])
#       smach.StateMachine.add(
#           node_name + '_' +'SET_TARGET',
#           SetFixedTargetState(target),
#           transitions={
#           'succeeded': node_name + '_' +'GET_TARGET',
#           'error': 'aborted'
#           }
#       )
#       smach.StateMachine.add(
#           node_name + '_' +'GET_TARGET',
#           GetTargetState(),
#           transitions={
#           'succeeded': node_name + '_' +'GOTO',
#           'error': 'aborted'
#           }
#       )
#       smach.StateMachine.add(
#           node_name + '_' +'GOTO',
#           GoToState(),
#           transitions={
#           'succeeded': 'succeeded',
#           'aborted': 'aborted',
#           'preempted': 'preempted'
#           }
#       )

#   def execute(self):
#     return smach.StateMachine.execute()