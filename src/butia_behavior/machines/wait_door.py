import smach
import rospy
from std_msgs.msg import Empty
import threading

class WaitDoorMachine(smach.StateMachine):
  def __init__(self):
    smach.StateMachine.__init__(self, outcomes=['succeeded', 'error'])
    smach.StateMachine.add(
        'WAIT_DOOR',
        WaitTopicState('butia_speech/wait_door'),
        transitions={
        'succeeded': 'succeeded',
        'error': 'error'
        }
    )

  def execute(self):
    return smach.StateMachine.execute()