#!/usr/bin/env python

from flexbe_core import EventState
from flexbe_core.proxy import ProxyServiceCaller
import rospy
from butia_world_msgs.srv import GetPose
import math

def euclid_dist(p1, p2):
  return math.sqrt(math.pow(p1.x - p2.x, 2)+math.pow(p1.y - p2.y, 2)+math.pow(p1.z - p2.z))

class GetTargetPoseState(EventState):
  def __init__(self, service='/butia_world/get_pose'):
    super(GetTargetPoseState, self).__init__(outcomes=['succeeded', 'error', 'arrived'], 
                               input_keys=['key'],
                               output_keys=['pose'])
    self.service = service
    self.client = ProxyServiceCaller({self.service: GetPose})

  def execute(self, userdata):
    rospy.wait_for_service(self.service)
    try:
      response = self.client.call(self.service, 'target/' + userdata.key + '/pose')
      exit_p = self.client.call(self.service, 'exit')
      if euclid_dist(response.pose.position, exit_pose.pose.position):
        return 'arrived'
      userdata.pose = response.pose
      return 'succeeded'
    except rospy.ServiceException, e:
      print "Service call failed: %s"%e
      return 'error'
    
