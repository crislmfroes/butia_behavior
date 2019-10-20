import smach
import rospy

class SetFixedTargetState(smach.State):
  def __init__(self, target):
    smach.State.__init__(self, outcomes=['succeeded', 'error'], 
                               output_keys=['target'])
    self.query = 'target/' + target + '/pose'

  def execute(self, userdata):
    userdata.target = self.query
    return 'succeeded'
    