from flexbe_core import EventState
from flexbe_core.proxy import ProxyPublisher
import rospy

from std_msgs.msg import Empty

class PublisherState(EventState):
  def __init__(self, topic):
    super(PublisherState, self).__init__(outcomes=['succeeded', 'error'])
    self.topic = topic
    self.publisher = ProxyPublisher({self.topic: Empty})

  def execute(self, userdata):
    self.publisher.publish(self.topic, Empty())
    return 'succeeded'