import smach
import rospy

class SelectIdState(smach.State):
  def __init__(self, service):
    smach.State.__init__(self, outcomes=['succeeded', 'error'], 
                               input_keys=['ids'],
                               output_keys=['id'])

  def execute(self, userdata):
    userdata.id = userdata.ids[0]
    return 'succeeded'
    