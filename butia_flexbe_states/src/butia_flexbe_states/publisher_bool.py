from flexbe_core import EventState
from flexbe_core.proxy import ProxyPublisher
import rospy

from std_msgs.msg import Bool

class PublisherBoolState(EventState):
  def __init__(self, topic, state):
    super(PublisherBoolState, self).__init__(outcomes=['succeeded', 'error'])
    self.topic = topic
    self.state = state

  def execute(self, userdata):
    publisher = ProxyPublisher({self.topic: Bool}, _queue_size=10)
    rospy.sleep(1)
    result = publisher.publish(self.topic, Bool(self.state))
    if result == None:
        return 'succeeded'
    else:
        return 'error'
