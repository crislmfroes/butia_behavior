from flexbe_core import EventState
from flexbe_core.proxy import ProxyServiceCaller
import rospy
from butia_speech.srv import SynthesizeSpeech

class SaySomethingState(EventState):
  def __init__(self, text):
    super(SaySomethingState, self).__init__(outcomes=['succeeded', 'error'])
    self.text = text

  def execute(self, userdata):
    rospy.wait_for_service('butia/synthesize_speech')
    synthesize_speech = ProxyServiceCaller({'butia/synthesize_speech': SynthesizeSpeech})
    resp = synthesize_speech.call('butia/synthesize_speech', self.text, 'pt-br')
    if resp:
      return 'succeeded'
    return 'error'