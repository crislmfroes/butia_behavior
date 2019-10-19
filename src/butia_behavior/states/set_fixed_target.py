import smach
import rospy

class GetPosesState(smach.State):
  def __init__(self, target):
    smach.State.__init__(self, outcomes=['succeeded', 'error'], 
                               output_keys=['query'])
    self.query = '*/' + target + '/pose'

  def execute(self, userdata):
    userdata.query = self.query
    return 'succeeded'
    