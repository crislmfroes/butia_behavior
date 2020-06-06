from flexbe_core import EventState, Logger
from flexbe_core.proxy import ProxyPublisher
from std_msgs.msg import String

class PublishStringState(EventState):

  def __init__(self, string):
    super(PublishStringState, self).__init__(outcomes=['succeeded', 'error'])
    self.publisher = ProxyPublisher({'butia_speech/bhd/hot_word': String})
    self.string = string

  def execute(self, userdata):
    try:
      self.publisher.publish('butia_speech/bhd/hot_word', String(self.string))
      return 'succeeded'
    except:
      return 'error'
