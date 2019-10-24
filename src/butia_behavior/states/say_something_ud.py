import smach
import rospy
from butia_speech.srv import SynthesizeSpeech

class SaySomethingUDState(smach.State):
  def __init__(self):
    smach.State.__init__(self, outcomes=['succeeded', 'error'], input_keys=['text'])

  def execute(self, userdata):
    rospy.wait_for_service('butia/synthesize_speech')
    synthesize_speech = rospy.ServiceProxy('butia/synthesize_speech', SynthesizeSpeech)
    resp = synthesize_speech(userdata.text, 'en-us')
    if resp:
      return 'succeeded'
    return 'error'