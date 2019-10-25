import smach
import rospy

from butia_behavior.states import PublisherBoolState, WaitTopicBoolState, WaitTimeState

def getCloseGripperMachine():
  sm = smach.StateMachine(outcomes=['succeeded', 'error'])
  with sm:
    smach.StateMachine.add(
        'CLOSE_GRIPPER',
        PublisherBoolState('/butia_manipulation_arm_gripper/close', True),
        transitions={
        'succeeded': 'WAIT_TIME',
        'error': 'error'
        }
    )
    smach.StateMachine.add(
      'WAIT_TIME',
      WaitTimeState(5),
      transitions={
        'succeeded': 'succeeded',
        'error': 'error'
      }
    )

    # smach.StateMachine.add(
    #     'WAIT_CLOSE_GRIPPER',
    #     WaitTopicBoolState('butia_manipulation_arm_gripper/close/finished'),
    #     transitions={
    #     'succeeded': 'succeeded',
    #     'error': 'error'
    #     }
    # )
  return sm