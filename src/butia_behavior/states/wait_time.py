import smach
import rospy
import time
from std_msgs.msg import Empty

class WaitTimeState(smach.State):
  def __init__(self, time):
    smach.State.__init__(self, outcomes=['succeeded', 'error'])
    self.time = time

  def execute(self, userdata):
    time.sleep(self.time)
    return 'succeeded'