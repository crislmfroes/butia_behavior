import smach
import rospy

class SetFixedTargetState(smach.State):
  def __init__(self, target):
    smach.State.__init__(self, outcomes=['succeeded', 'error'], 
                               output_keys=['target'])
    self.target = target

  def execute(self, userdata):
    rospy.loginfo("Set Fixed Target State.")
    userdata.target = self.target
    return 'succeeded'
    