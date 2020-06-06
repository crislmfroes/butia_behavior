#!/usr/bin/env python
from flexbe_core import EventState
from flexbe_core.proxy import ProxyActionClient

import rospy

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseActionResult, MoveBaseResult
from actionlib.simple_action_client import GoalStatus

class GoToState(EventState):
  def __init__(self, frame='map'):
    super(GoToState, self).__init__(input_keys=['pose'], outcomes=['succeeded','aborted','preempted'])
    self.action_client = ProxyActionClient({'move_base': MoveBaseAction})
    self.frame = frame

  def execute(self, userdata):
    if self.action_client.has_result('move_base'):
      if self.action_client.get_result('move_base') == GoalStatus.SUCCEEDED:
        return 'suceeded'
      elif self.action_client.get_result('move_base') == GoalStatus.ABORTED:
        return 'aborted'
      elif self.action_client.get_result('move_base') == GoalStatus.PREEMPTED:
        return 'preempted'

  def on_enter(self, userdata):
    self.action_client.send_goal('move_base', self.__goal_cb(userdata))

  def __goal_cb(self, userdata):
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = self.frame
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose = userdata.pose
    return goal
