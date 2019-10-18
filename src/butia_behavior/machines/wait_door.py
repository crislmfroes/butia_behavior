import smach
import rospy
from std_msgs.msg import Empty
import threading

wait_door_sm = smach.StateMachine(outcomes=['succeeded', 'error'])
with wait_door_sm:
    smach.StateMachine.add(
        'WAIT_DOOR',
        WaitTopicState('butia_speech/wait_door'),
        transitions={
        'succeeded': 'succeeded',
        'error': 'error'
        }
    )