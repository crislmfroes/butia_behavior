import smach
import rospy
from butia_world_msgs.srv import GetPoses

class GetPosesState(smach.State):
  def __init__(self, service='/butia_world/get_poses'):
    smach.State.__init__(self, outcomes=['succeeded', 'error'], 
                               input_keys=['query'],
                               output_keys=['poses'])
    self.service = service
    self.client = rospy.ServiceProxy(self.service, GetPoses)

  def execute(self, userdata):
    rospy.wait_for_service(self.service)
    try:
      response = self.client(userdata.query)
      userdata.poses = response.poses
      return 'succeeded'
    except rospy.ServiceException, e:
      print "Service call failed: %s"%e
      return 'error'
    