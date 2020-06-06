from flexbe_core import EventState
from flexbe_core.proxy import ProxySubscriberCached
import rospy
from std_msgs.msg import Empty
import threading

class WaitTopicState(EventState):
  def __init__(self, topic):
    super(WaitTopicState, self).__init__(outcomes=['succeeded', 'error'])
    self.subscriber = ProxySubscriberCached({topic: Empty})
    self.subscriber.set_callback(topic, self.callback)
    self.event = threading.Event()

  def execute(self, userdata):
    self.event.clear()
    self.event.wait()
    if self.event.is_set():
        return 'succeeded'
    return 'error'

  def callback(self, data):
    self.event.set()