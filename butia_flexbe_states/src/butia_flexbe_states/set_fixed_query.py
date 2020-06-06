from flexbe_core import EventState
import rospy

class SetFixedQueryState(EventState):
  def __init__(self, query):
    super(SetFixedQueryState, self).__init__(outcomes=['succeeded', 'error'], 
                               output_keys=['query'])
    self.query = query

  def execute(self, userdata):
    userdata.query = self.query
    return 'succeeded'
    