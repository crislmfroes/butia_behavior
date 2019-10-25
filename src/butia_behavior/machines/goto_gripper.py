import smach
import rospy

from butia_behavior.states import PublisherFloat64State, WaitTopicBoolState

topics = ['butia_manipulation_arm_gripper/initial_position/finished',
          'butia_manipulation_arm_gripper/first_position/finished',
          'butia_manipulation_arm_gripper/second_position/finished']

def getGoToGripperMachine(state):
  sm = smach.StateMachine(outcomes=['succeeded', 'error'])
  with sm:
    smach.StateMachine.add(
        'GOTO_GRIPPER',
        PublisherFloat64State('/butia_manipulation_arm_gripper/goto', state),
        transitions={
        'succeeded': 'WAIT_GOTO_GRIPPER',
        'error': 'error'
        }
    )
    smach.StateMachine.add(
        'WAIT_GOTO_GRIPPER',
        WaitTopicBoolState(topics[state]),
        transitions={
        'succeeded': 'succeeded',
        'error': 'error'
        }
    )
  return sm