from flexbe_core import EventState
from flexbe_core.proxy import ProxyPublisher
import rospy

from std_msgs.msg import Int16

class PublisherIdState(EventState):
  def __init__(self, topic):
    super(PublisherIdState, self).__init__(outcomes=['succeeded', 'error'], input_keys=['id'])
    self.topic = topic
    self.publisher = ProxyPublisher({self.topic: Int16})

  def execute(self, userdata):
    self.publisher.publish(self.topic, Int16(userdata.id))
    return 'succeeded'