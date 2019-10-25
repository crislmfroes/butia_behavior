import smach
import rospy
from std_msgs.msg import Bool
import threading

class WaitTopicBoolState(smach.State):
  def __init__(self, topic):
    smach.State.__init__(self, outcomes=['succeeded', 'error'])
    self.topic = topic
    self.result = False
    self.event = threading.Event()

  def execute(self, userdata):
    self.subscriber = rospy.Subscriber(self.topic, Bool, self.callback)
    self.event.clear()
    self.event.wait()
    if self.event.is_set() and self.result:
        return 'succeeded'
    return 'error'

  def callback(self, data):
    self.result = data.data
    self.event.set()