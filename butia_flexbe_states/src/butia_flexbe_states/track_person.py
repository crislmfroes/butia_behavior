from flexbe_core import EventState
from flexbe_core.proxy import ProxyServiceCaller
import rospy
from butia_vision_msgs.srv import StartTracking, StartTrackingResponse

class TrackPersonState(EventState):
  def __init__(self, service='/butia_vision/pt/start'):
    super(TrackPersonState, self).__init__(outcomes=['succeeded', 'error'])
    self.service = service
    self.client = ProxyServiceCaller({self.service: StartTracking})

  def execute(self, userdata):
    rospy.wait_for_service(self.service)
    try:
      response = self.client.call(self.service, True)
      if response.started:
        return 'succeeded'
      else:
        return 'error'
    except rospy.ServiceException, e:
      print "Service call failed: %s"%e
      return 'error'
    