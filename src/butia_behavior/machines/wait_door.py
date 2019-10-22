import smach
import rospy

from butia_behavior.states import WaitTopicState, PublisherState

def getWaitDoorMachine():
  sm = smach.StateMachine(outcomes=['succeeded', 'error'])
  with sm:
    smach.StateMachine.add(
          'ANALIZE_DOOR',
          PublisherState('butia_navigation/analize_door'),
          transitions={
          'succeeded': 'WAIT_DOOR',
          'error': 'error'
          }
    )
    smach.StateMachine.add(
          'WAIT_DOOR',
          WaitTopicState('butia_navigation/wait_door'),
          transitions={
          'succeeded': 'succeeded',
          'error': 'error'
          }
    )
  return sm