import smach
import rospy

from std_msgs.msg import Int16

class PublisherIdState(smach.State):
  def __init__(self, topic):
    smach.State.__init__(self, outcomes=['succeeded', 'error'], input_keys=['id'])
    self.publisher = rospy.Publisher(topic, Int16)

  def execute(self, userdata):
    self.publisher.publish(Int16(userdata.id))
    return 'succeeded'