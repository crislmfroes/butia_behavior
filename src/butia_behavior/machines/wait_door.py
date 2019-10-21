import smach
import rospy
from std_msgs.msg import Empty

def getWaitDoorMachine():
  sm = smach.StateMachine.__init__(self, outcomes=['succeeded', 'error'])
  with sm:
    smach.StateMachine.add(
          'WAIT_DOOR',
          WaitTopicState('butia_speech/wait_door'),
          transitions={
          'succeeded': 'succeeded',
          'error': 'error'
          }
    )
  return sm