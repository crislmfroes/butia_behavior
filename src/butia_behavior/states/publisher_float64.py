import smach
import rospy

from std_msgs.msg import Float64

class PublisherFloat64State(smach.State):
  def __init__(self, topic, state):
    smach.State.__init__(self, outcomes=['succeeded', 'error'])
    self.topic = topic
    self.state = state

  def execute(self, userdata):
    publisher = rospy.Publisher(self.topic, Float64, queue_size=10)
    rospy.sleep(1)
    result = publisher.publish(Float64(self.state))
    if result == None:
      return 'succeeded'
    else:
      return 'error'
