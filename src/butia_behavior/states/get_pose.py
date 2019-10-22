import smach
import rospy
from butia_world_msgs.srv import GetPose

class GetPoseState(smach.State):
  def __init__(self, service='/butia_world/get_pose'):
    smach.State.__init__(self, outcomes=['succeeded', 'error'], 
                               input_keys=['key'],
                               output_keys=['pose'])
    self.service = service
    self.client = rospy.ServiceProxy(self.service, GetPose)

  def execute(self, userdata):
    rospy.wait_for_service(self.service)
    try:
      print(userdata.key)
      response = self.client(userdata.key + '/pose')
      userdata.pose = response.pose
      return 'succeeded'
    except rospy.ServiceException, e:
      print "Service call failed: %s"%e
      return 'error'
    