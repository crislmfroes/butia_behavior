from flexbe_core import EventState
from flexbe_core.proxy import ProxyPublisher
import rospy

from std_msgs.msg import Float64

class PublisherFloat64State(EventState):
  def __init__(self, topic, state):
    super(PublisherFloat64State, self).__init__(outcomes=['succeeded', 'error'])
    self.topic = topic
    self.state = state

  def execute(self, userdata):
    publisher = ProxyPublisher({self.topic: Float64}, _queue_size=10)
    rospy.sleep(1)
    result = publisher.publish(self.topic, Float64(self.state))
    if result == None:
      return 'succeeded'
    else:
      return 'error'
