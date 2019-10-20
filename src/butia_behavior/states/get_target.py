import smach
import rospy
from butia_world_msgs.srv import GetPoses

class GetTargetState(smach.State):
  def __init__(self, service='/butia_world/get_poses'):
    smach.State.__init__(self, outcomes=['succeeded', 'error'], 
                               input_keys=['target'],
                               output_keys=['pose'])
    self.service = service
    self.client = rospy.ServiceProxy(self.service, GetPoses)

  def execute(self, userdata):
    rospy.wait_for_service(self.service)
    try:
      response = self.client('target/' + userdata.target + '/pose')
      userdata.pose = response.poses[0]
      return 'succeeded'
    except rospy.ServiceException, e:
      print "Service call failed: %s"%e
      return 'error'
    