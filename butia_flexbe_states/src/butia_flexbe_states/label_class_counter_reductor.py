#!/usr/bin/env python

from flexbe_core import EventState
from flexbe_core.proxy import ProxySubscriberCached
import rospy
import threading
from collections import defaultdict

from butia_vision_msgs.msg import Recognitions, Description

#/butia_vision/or/object_recognition3d

class ClassesHistoryReductorState(EventState):
  
  def __init__(self, reduction_func):
    super(ClassesHistoryReductorState, self).__init__(
      self,
      outcomes=['succeeded', 'error'],
      input_keys=['counts_history'],
      output_keys=['classes_count']
    )
    self.reduction_func = reduction_func
  
  def execute(self, userdata):
    classes_count = {}
    for label, counts in userdata.counts_history.items():
      classes_count[label] = self.reduction_func(counts)
    userdata.classes_count = classes_count
    print(classes_count)
    return 'succeeded'
