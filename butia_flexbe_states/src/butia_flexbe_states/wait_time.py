from flexbe_core import EventState
import rospy
import time
from std_msgs.msg import Empty

class WaitTimeState(EventState):
  def __init__(self, time):
    super(WaitTimeState, self).__init__(outcomes=['succeeded', 'error'])
    self.time = time

  def execute(self, userdata):
    time.sleep(self.time)
    return 'succeeded'