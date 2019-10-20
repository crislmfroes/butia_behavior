import smach

import rospy

from butia_behavior.states import SetFixedTargetState, GetTargetState, GoToState

class GoToFixedMachine(smach.StateMachine):
  def __init__(self, target):
    smach.StateMachine.__init__(self, outcomes=['succeeded','aborted','preempted'])
    smach.StateMachine.add(
        'SET_TARGET',
        SetFixedTargetState(target),
        transitions={
        'succeeded': 'succeeded',
        'error': 'aborted'
        }
    )
    smach.StateMachine.add(
        'GET_TARGET',
        GetTargetState(),
        transitions={
        'succeeded': 'GOTO',
        'error': 'aborted'
        }
    )
    smach.StateMachine.add(
        'GOTO',
        GoToState(),
        transitions={
        'succeeded': 'GOTO',
        'aborted': 'aborted',
        'preempted': 'preempted'
        }
    )

  def execute(self):
    return smach.StateMachine.execute()