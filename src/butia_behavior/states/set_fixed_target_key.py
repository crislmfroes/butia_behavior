import smach
import rospy

class SetFixedTargetKeyState(smach.State):
  def __init__(self, key):
    smach.State.__init__(self, outcomes=['succeeded', 'error'], 
                               output_keys=['key'])
    self.key = key

  def execute(self, userdata):
    userdata.key = 'target/' + self.key + '/pose'
    return 'succeeded'
    