import smach
import rospy

class GoToMachine(smach.StateMachine):
  def __init__(self, target):
    smach.StateMachine.__init__(self, outcomes=['succeeded','aborted','preempted'], input_keys=['target'])
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

  def execute(self):
    return smach.StateMachine.execute()