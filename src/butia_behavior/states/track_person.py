import smach
import rospy
from butia_vision_msgs.srv import StartTracking, StartTrackingResponse

class TrackPersonState(smach.State):
  def __init__(self, service='/butia_vision/pt/start'):
    smach.State.__init__(self, outcomes=['succeeded', 'error'])
    self.service = service
    self.client = rospy.ServiceProxy(self.service, StartTracking)

  def execute(self, userdata):
    rospy.wait_for_service(self.service)
    try:
      response = self.client(True)
      if response.started:
        return 'succeeded'
      else:
        return 'error'
    except rospy.ServiceException, e:
      print "Service call failed: %s"%e
      return 'error'
    