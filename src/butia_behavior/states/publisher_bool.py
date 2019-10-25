import smach
import rospy

from std_msgs.msg import Bool

class PublisherBoolState(smach.State):
  def __init__(self, topic, state):
    smach.State.__init__(self, outcomes=['succeeded', 'error'])
    self.topic = topic
    self.state = state

  def execute(self, userdata):
    publisher = rospy.Publisher(self.topic, Bool, queue_size=10)
    rospy.sleep(1)
    result = publisher.publish(Bool(self.state))
    if result == None:
        return 'succeeded'
    else:
        return 'error'
