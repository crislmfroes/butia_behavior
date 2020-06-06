#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from butia_flexbe_states.publisher_float64 import PublisherFloat64State
from butia_flexbe_states.wait_topic_bool import WaitTopicBoolState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri Jun 05 2020
@author: Cris Lima Froes
'''
class go_to_gripper_machineSM(Behavior):
	'''
	Moves gripper torwards position.
	'''


	def __init__(self):
		super(go_to_gripper_machineSM, self).__init__()
		self.name = 'go_to_gripper_machine'

		# parameters of this behavior
		self.add_parameter('gripper_state', '0')

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		topics = ['butia_manipulation_arm_gripper/initial_position/finished','butia_manipulation_arm_gripper/first_position/finished','butia_manipulation_arm_gripper/second_position/finished']
		# x:30 y:365, x:130 y:365
		_state_machine = OperatableStateMachine(outcomes=['succeeded', 'error'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:181 y:25
			OperatableStateMachine.add('goto_gripper',
										PublisherFloat64State(topic='butia_manipulation_arm_gripper/goto', state=int(self.gripper_state)),
										transitions={'succeeded': 'wait_goto_gripper', 'error': 'error'},
										autonomy={'succeeded': Autonomy.Off, 'error': Autonomy.Off})

			# x:356 y:78
			OperatableStateMachine.add('wait_goto_gripper',
										WaitTopicBoolState(topic=topics[int(self.gripper_state)]),
										transitions={'succeeded': 'succeeded', 'error': 'error'},
										autonomy={'succeeded': Autonomy.Off, 'error': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
