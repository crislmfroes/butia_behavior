import smach
import rospy

from butia_behavior.states import GetTargetPoseState, GoToState

def getGoToMachine():
  sm = smach.StateMachine(outcomes=['succeeded', 'aborted', 'preempted'], input_keys=['key'])
  with sm:
    smach.StateMachine.add(
        'GET_TARGET_POSE',
        GetTargetPoseState(),
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
        'succeeded': 'succeeded',
        'aborted': 'aborted',
        'preempted': 'preempted'
        },
        remapping={
        'pose':'pose'
        }
    )
  return sm