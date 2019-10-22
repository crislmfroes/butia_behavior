#!/usr/bin/env python
import smach
import smach_ros

import rospy

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

class GoToState(smach_ros.SimpleActionState):
  def __init__(self, frame='map'):
    smach_ros.SimpleActionState.__init__(self, 'move_base', MoveBaseAction, input_keys=['pose'], goal_cb=self.__goal_cb)
    self.frame = frame

  def __goal_cb(self, userdata, old_goal):
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = self.frame
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose = userdata.pose
    return goal
