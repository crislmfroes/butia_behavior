import smach
import rospy

from std_msgs.msg import Float64

class PublisherFloat64State(smach.State):
  def __init__(self, topic, state):
    smach.State.__init__(self, outcomes=['succeeded', 'error'])
    self.publisher = rospy.Publisher(topic, Float64, queue_size=10)
    self.state = state

  def execute(self, userdata):
    self.publisher.publish(self.state)
    return 'succeeded'