import smach
import rospy

from butia_behavior.states import PublisherFloat64State, WaitTopicBoolState

def getTurnGripperMachine(state):
  sm = smach.StateMachine(outcomes=['succeeded', 'error'])
  with sm:
    smach.StateMachine.add(
        'TURN_GRIPPER',
        PublisherFloat64State('/butia_manipulation_arm_gripper/turn', state),
        transitions={
        'succeeded': 'WAIT_TURN_GRIPPER',
        'error': 'error'
        }
    )
    smach.StateMachine.add(
        'WAIT_TURN_GRIPPER',
        WaitTopicBoolState('/butia_manipulation_arm_gripper/turn'),
        transitions={
        'succeeded': 'succeeded',
        'error': 'error'
        }
    )
  return sm