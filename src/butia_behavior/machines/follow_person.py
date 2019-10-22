import smach

import rospy

from butia_behavior.states import SetFixedQueryState, GetPoseState, GetKeyState, TrackPersonState
from . import getGoToMachine

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
        'succeeded': 'GOTO',
        'error': 'aborted'
        },
        remapping={
        'query':'query',
        'key': 'key'
        }
    )
    smach.StateMachine.add(
        'GOTO',
        getGoToMachine(),
        transitions={
        'succeeded': 'SET_QUERY',
        'aborted': 'SET_QUERY',
        'preempted': 'preempted'
        },
        remapping={
        'key': 'key'
        }
    )
  return sm