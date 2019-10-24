import smach
import rospy

class PrepareSpeechState(smach.State):
  def __init__(self, prefix, string_format, sufix):
    smach.State.__init__(self, outcomes=['succeeded', 'error'], input_keys=['registers'], output_keys=['text'])
    self.prefix = prefix
    self.string_format = string_format
    self.sufix = sufix

  def execute(self, userdata):
    text = self.prefix + ' '
    micro_sentences = [self.string_format.format(x=' '.join(key.split('/')), y=value) for key, value in userdata.registers.items()]
    text += ', '.join(micro_sentences)
    text += ' ' + self.sufix
    userdata.text = text
    print(text)
    return 'succeeded'
    