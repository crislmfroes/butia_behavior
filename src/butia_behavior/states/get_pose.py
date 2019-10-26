import smach
import rospy
from butia_world_msgs.srv import GetPose
import math

def euclid_dist(p1, p2):
  return math.sqrt(math.pow(p1.x - p2.x, 2)+math.pow(p1.y - p2.y, 2)+math.pow(p1.z - p2.z))

class GetPoseState(smach.State):
  def __init__(self, service='/butia_world/get_pose'):
    smach.State.__init__(self, outcomes=['succeeded', 'error', 'arrived'], 
                               input_keys=['key'],
                               output_keys=['pose'])
    self.service = service
    self.client = rospy.ServiceProxy(self.service, GetPose)

  def execute(self, userdata):
    rospy.wait_for_service(self.service)
    try:
      print(userdata.key)
      response = self.client(userdata.key + '/pose')
      exit_p = self.client('exit')
      if euclid_dist(response.pose.position, exit_pose.pose.position):
        return 'arrived'
      userdata.pose = response.pose
      return 'succeeded'
    except rospy.ServiceException, e:
      print "Service call failed: %s"%e
      return 'error'
    
