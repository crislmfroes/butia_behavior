import smach

import rospy

from butia_behavior.states import SetFixedQueryState, GetPoseState, GoToState, GetKeyState, TrackPersonState

def getFollowPersonMachine():
  sm = smach.StateMachine(outcomes=['succeeded', 'aborted', 'preempted'])
  with sm:
    smach.StateMachine.add(
        'TRACK',
        TrackPersonState(),
        transitions={
        'succeeded': 'SET_QUERY',
        'error': 'aborted'
        }
    )
    smach.StateMachine.add(
        'SET_QUERY',
        SetFixedQueryState('*tracked_person*'),
        transitions={
        'succeeded': 'GET_KEY',
        'error': 'aborted'
        },
        remapping={
        'query': 'query'
        }
    )
    smach.StateMachine.add(
        'GET_KEY',
        GetKeyState(),
        transitions={
        'succeeded': 'GET_POSE',
        'error': 'aborted'
        },
        remapping={
        'query':'query',
        'key': 'key'
        }
    )
    smach.StateMachine.add(
        'GET_POSE',
        GetPoseState(),
        transitions={
        'succeeded': 'GOTO',
        'error': 'aborted'
        },
        remapping={
        'key': 'key',
        'pose': 'pose'
        }
    )
    smach.StateMachine.add(
        'GOTO',
        GoToState(),
        transitions={
        'succeeded': 'SET_QUERY',
        'aborted': 'SET_QUERY',
        'preempted': 'preempted'
        },
        remapping={
        'pose': 'pose'
        }
    )
  return sm