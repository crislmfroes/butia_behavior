import smach
import rospy

from butia_behavior.states import GetPoseState, GoToState

def getGoToMachine():
  sm = smach.StateMachine(outcomes=['succeeded', 'aborted', 'preempted'])
  with sm:
    smach.StateMachine.add(
        'GET_POSE',
        GetPoseState(),
        transitions={
        'succeeded': 'GOTO',
        'error': 'aborted'
        },
        remapping={
        'key':'key',
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