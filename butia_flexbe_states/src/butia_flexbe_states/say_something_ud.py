from flexbe_core import EventState
from flexbe_core.proxy import ProxyServiceCaller
import rospy
from butia_speech.srv import SynthesizeSpeech

class SaySomethingUDState(EventState):
  def __init__(self):
    super(SaySomethingUDState, self).__init__(outcomes=['succeeded', 'error'], input_keys=['text'])

  def execute(self, userdata):
    rospy.wait_for_service('butia/synthesize_speech')
    synthesize_speech = ProxyServiceCaller({'butia/synthesize_speech': SynthesizeSpeech})
    resp = synthesize_speech.call('butia/synthesize_speech', userdata.text, 'en-us')
    if resp:
      return 'succeeded'
    return 'error'