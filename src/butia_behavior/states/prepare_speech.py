import smach
import random
from collections import defaultdict
import json

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
    clustered_count = defaultdict(list)
    for key, value in userdata.registers.items():
        splitted = key.split('/')
        category = splitted[0]
        label = splitted[1]
        clustered_count[category].append({label: value})
    print(text)
    print(clustered_count)
    print(json.dumps(clustered_count, indent=4))
    return 'succeeded'
    
