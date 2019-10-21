import smach
import rospy
from std_msgs.msg import Empty
import threading

class WaitTopicState(smach.State):
  def __init__(self, topic):
    smach.State.__init__(self, outcomes=['succeeded', 'error'])
    self.subscriber = rospy.Subscriber(topic, Empty, self.callback)
    self.event = threading.Event()

  def execute(self, userdata):
    rospy.loginfo("Wait Topic State.")
    self.event.clear()
    self.event.wait()
    if self.event.is_set():
        return 'succeeded'
    return 'error'

  def callback(self, data):
    self.event.set()