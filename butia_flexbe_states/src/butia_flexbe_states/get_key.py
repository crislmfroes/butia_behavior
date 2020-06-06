#!/usr/bin/env python

from flexbe_core import EventState
from flexbe_core.proxy import ProxyServiceCaller
import rospy
from butia_world_msgs.srv import GetKey

class GetKeyState(EventState):
  def __init__(self, method='closest'):
    super(GetKeyState, self).__init__(outcomes=['succeeded', 'error'], 
                               input_keys=['query'],
                               output_keys=['key'])
    self.service = '/butia_world/get_' + method +'_key'
    self.client = ProxyServiceCaller({self.service: GetKey})

  def execute(self, userdata):
    rospy.wait_for_service(self.service)
    try:
      response = self.client.call(self.service, userdata.query)
      userdata.key = response.key
      return 'succeeded'
    except rospy.ServiceException, e:
      print "Service call failed: %s"%e
      return 'error'
