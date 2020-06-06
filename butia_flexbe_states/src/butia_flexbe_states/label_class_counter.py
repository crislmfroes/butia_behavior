#!/usr/bin/env python

from flexbe_core import EventState
from flexbe_core.proxy import ProxySubscriberCached
import rospy
import threading
from collections import defaultdict

from butia_vision_msgs.msg import Recognitions, Description

#/butia_vision/or/object_recognition3d

class ClassesCountHistoryState(EventState):

  def __init__(self, topic, window_size):
    super(ClassesCountHistoryState, self).__init__(
      outcomes=['succeeded', 'error'],
      output_keys=['counts_history']
    )
    self.topic = topic
    self.window_size = window_size
    self.event = threading.Event()
    self.counts_history = defaultdict(list)
    self.frame_counter = 0
  
  def execute(self, userdata):
    self.subscriber = ProxySubscriberCached({self.topic: Recognitions})
    self.subscriber.set_callback(self.topic, self._on_recognitions)
    self.event.clear()
    self.event.wait()
    if self.event.is_set():
      userdata.counts_history = self.counts_history
      return 'succeeded'
    return 'error'
  
  def _on_recognitions(self, recognitions):
    print('frame ' + str(self.frame_counter))
    print(recognitions)
    frame_counts = defaultdict(int)
    for description in recognitions.descriptions:
      frame_counts[description.label_class] += 1
    for label, count in frame_counts.items():
      self.counts_history[label].append(count)
    self.frame_counter += 1
    if self.frame_counter >= self.window_size:
      print(self.counts_history)
      self.subscriber.unregister()
      self.event.set()
