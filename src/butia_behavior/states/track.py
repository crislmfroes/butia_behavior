import smach
import rospy
from butia_world_msgs.srv import StartTracking, StartTrackingResponse

class TrackState(smach.State):
  def __init__(self, service='/butia_vision/pt/start'):
    smach.State.__init__(self, outcomes=['succeeded', 'error'], 
                               input_keys=['query'],
                               output_keys=['poses'])
    self.service = service
    self.client = rospy.ServiceProxy(self.service, StartTracking)

  def execute(self, userdata):
    rospy.loginfo("Track State.")
    rospy.wait_for_service(self.service)
    try:
      response = self.client(userdata.query)
      
      return 'succeeded'
    except rospy.ServiceException, e:
      print "Service call failed: %s"%e
      return 'error'
    