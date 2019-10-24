import smach

import rospy

from butia_behavior.states import ClassesCountHistoryState, ClassesHistoryReductorState

def getClassesCountMachine(topic, window_size, reductor):
  sm = smach.StateMachine(outcomes=['succeeded', 'error'], output_keys=['registers'])
  with sm:
    smach.StateMachine.add(
      'COUNT_HISTORY',
      ClassesCountHistoryState(topic, window_size),
      transitions={
        'succeeded': 'HISTORY_REDUCTOR',
        'error': 'error'
      }
    )
    smach.StateMachine.add(
      'HISTORY_REDUCTOR',
      ClassesHistoryReductorState(reductor),
      transitions={
        'succeeded': 'succeeded',
        'error': 'error'
      },
      remapping={
        'classes_count': 'registers'
      }
    )
  return sm