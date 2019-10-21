import smach
import rospy

from std_msgs.msg import Int16

class PublisherState(smach.State):
  def __init__(self, topic):
    smach.State.__init__(self, outcomes=['succeeded', 'error'], input_keys=['id'])
    self.publisher = rospy.Publisher(topic, Int16, self.callback)

  def execute(self, userdata):
    rospy.loginfo("Publisher State.")
    self.publisher.publish(Int16(userdata.id))
    return 'succeeded'