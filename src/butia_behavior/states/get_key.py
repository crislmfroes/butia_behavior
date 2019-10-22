import smach
import rospy
from butia_world_msgs.srv import GetKey

class GetKeyState(smach.State):
  def __init__(self, method='closest'):
    smach.State.__init__(self, outcomes=['succeeded', 'error'], 
                               input_keys=['query'],
                               output_keys=['key'])
    self.service = '/butia_world/get_' + method +'_key'
    self.client = rospy.ServiceProxy(self.service, GetKey)

  def execute(self, userdata):
    rospy.wait_for_service(self.service)
    try:
      response = self.client(userdata.query)
      userdata.key = response.key
      return 'succeeded'
    except rospy.ServiceException, e:
      print "Service call failed: %s"%e
      return 'error'
    
    