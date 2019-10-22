import smach
import rospy

class SetFixedQueryState(smach.State):
  def __init__(self, query):
    smach.State.__init__(self, outcomes=['succeeded', 'error'], 
                               output_keys=['query'])
    self.query = query

  def execute(self, userdata):
    userdata.query = self.query
    return 'succeeded'
    