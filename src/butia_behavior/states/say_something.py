import smach
import rospy
from butia_speech.srv import SynthesizeSpeech

class SaySomethingState(smach.State):
  def __init__(self, text):
    smach.State.__init__(self, outcomes=['succeeded', 'error'])
    self.text = text

  def execute(self, userdata):
    rospy.wait_for_service('butia/synthesize_speech')
    synthesize_speech = rospy.ServiceProxy('butia/synthesize_speech', SynthesizeSpeech)
    resp = synthesize_speech(self.text, 'pt-br')
    if resp:
      return 'succeeded'
    return 'error'