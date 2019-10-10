import smach
import rospy
from std_msgs.msg import Empty
import threading

class WaitHotwordState(smach.State):
  def __init__(self):
    smach.State.__init__(self, outcomes=['succeeded', 'error'])
    self.subscriber = rospy.Subscriber('butia/wakeup', Empty, self.callback)
    self.event = threading.Event()

  def execute(self, userdata):
    self.event.clear()
    self.event.wait()
    if self.event.is_set():
        return 'succeeded'
    return 'error'

  def callback(self, data):
    self.event.set()