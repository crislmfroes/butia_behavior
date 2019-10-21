import smach
import rospy

from butia_behavior.states import WaitTopicState, PublisherState

def getSpeechMachine():
  sm = smach.StateMachine.__init__(self, outcomes=['succeeded', 'error'])
  with sm:
    smach.StateMachine.add(
          'PUBLISH',
          PublisherState('butia_speech/speak'),
          transitions={
          'succeeded': 'succeeded',
          'error': 'error'
          }
    )
    smach.StateMachine.add(
          'WAIT_TOPIC',
          WaitTopicState('butia_speech/spoken'),
          transitions={
          'succeeded': 'succeeded',
          'error': 'error'
          }
    )
  return sm