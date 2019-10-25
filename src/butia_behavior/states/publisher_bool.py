import smach
import rospy

from std_msgs.msg import Bool

class PublisherBoolState(smach.State):
  def __init__(self, topic, state):
    smach.State.__init__(self, outcomes=['succeeded', 'error'])
    self.publisher = rospy.Publisher(topic, Bool, queue_size=10)
    self.state = state

  def execute(self, userdata):
    self.publisher.publish(Bool(self.state))
    return 'succeeded'