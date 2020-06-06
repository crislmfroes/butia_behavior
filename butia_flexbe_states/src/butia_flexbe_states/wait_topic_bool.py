from flexbe_core import EventState
from flexbe_core.proxy import ProxySubscriberCached
import rospy
from std_msgs.msg import Bool
import threading

class WaitTopicBoolState(EventState):
  def __init__(self, topic):
    super(WaitTopicBoolState, self).__init__(outcomes=['succeeded', 'error'])
    self.topic = topic
    self.result = False
    self.event = threading.Event()
    self.subscriber = ProxySubscriberCached({self.topic: Bool})
    self.subscriber.set_callback(self.topic, self.callback)

  def execute(self, userdata):
    self.event.clear()
    self.event.wait()
    if self.event.is_set() and self.result:
        return 'succeeded'
    return 'error'

  def callback(self, data):
    self.result = data.data
    self.event.set()
