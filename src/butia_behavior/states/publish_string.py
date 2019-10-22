import smach
import rospy
from std_msgs.msg import String

class PublishStringState(smach.State):

  def __init__(self, string):
    smach.State.__init__(self, outcomes=['succeeded', 'error'])
    self.publisher = rospy.Publisher('butia_speech/bhd/hot_word', String)
    self.string = string

  def execute(self, userdata):
    self.publisher.publish(String(self.string))
    return 'succeeded'
