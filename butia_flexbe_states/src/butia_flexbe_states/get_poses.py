from flexbe_core import EventState
from flexbe_core.proxy import ProxyServiceCaller
import rospy
from butia_world_msgs.srv import GetPoses


class GetPosesState(EventState):
  def __init__(self, prefix, service='/butia_world/get_poses'):
    self.prefix = prefix
    super(GetPosesState, self).__init__(outcomes=[self.prefix + 'succeeded', self.prefix + 'error'], 
                               input_keys=['query'],
                               output_keys=['poses'])
    self.service = service
    self.client = ProxyServiceCaller({self.service: GetPoses})

  def execute(self, userdata):
    rospy.loginfo("Get Poses State.")
    rospy.wait_for_service(self.service)
    try:
      response = self.client.call(userdata.query)
      userdata.poses = response.poses
      return self.prefix + 'succeeded'
    except rospy.ServiceException, e:
      print "Service call failed: %s"%e
      return self.prefix + 'error'
    