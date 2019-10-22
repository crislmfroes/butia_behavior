import smach
import rospy

from std_msgs.msg import Empty

class PublisherState(smach.State):
  def __init__(self, topic):
    smach.State.__init__(self, outcomes=['succeeded', 'error'])
    self.publisher = rospy.Publisher(topic, Empty)

  def execute(self, userdata):
    self.publisher.publish(Empty())
    return 'succeeded'