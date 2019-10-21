import smach
import rospy

from butia_behavior.states import SetFixedTargetState, GetTargetState, GoToState

def getGoToMachine():
  sm = smach.StateMachine(outcomes=['succeeded', 'aborted', 'preempted'])
  with sm:
    smach.StateMachine.add(
        'GET_TARGET',
        GetTargetState(),
        transitions={
        'succeeded': 'GOTO',
        'error': 'aborted'
        },
        remapping={
        'target':'target',
        'pose':'pose'
        }
    )
    smach.StateMachine.add(
        'GOTO',
        GoToState(),
        transitions={
        'succeeded': 'GOTO',
        'aborted': 'aborted',
        'preempted': 'preempted'
        },
        remapping={
        'pose':'pose'
        }
    )
  return sm