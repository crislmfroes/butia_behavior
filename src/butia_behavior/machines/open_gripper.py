import smach
import rospy

from butia_behavior.states import PublisherBoolState, WaitTopicBoolState

def getOpenGripperMachine():
  sm = smach.StateMachine(outcomes=['succeeded', 'error'])
  with sm:
    smach.StateMachine.add(
        'OPEN_GRIPPER',
        PublisherBoolState('/butia_manipulation_arm_gripper/open', True),
        transitions={
        'succeeded': 'WAIT_OPEN_GRIPPER',
        'error': 'error'
        }
    )
    smach.StateMachine.add(
        'WAIT_OPEN_GRIPPER',
        WaitTopicBoolState('butia_manipulation_arm_gripper/open/finished'),
        transitions={
        'succeeded': 'succeeded',
        'error': 'error'
        }
    )
  return sm