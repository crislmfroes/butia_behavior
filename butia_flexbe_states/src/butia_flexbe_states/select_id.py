from flexbe_core import EventState
import rospy

class SelectIdState(EventState):
  def __init__(self, service):
    super(SelectIdState, self).__init__(outcomes=['succeeded', 'error'], 
                               input_keys=['ids'],
                               output_keys=['id'])

  def execute(self, userdata):
    userdata.id = userdata.ids[0]
    return 'succeeded'
    