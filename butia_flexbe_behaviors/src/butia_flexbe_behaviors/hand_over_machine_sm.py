#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from butia_flexbe_behaviors.open_gripper_machine_sm import open_gripper_machineSM
from butia_flexbe_behaviors.go_to_gripper_machine_sm import go_to_gripper_machineSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri Jun 05 2020
@author: Cris Lima Froes
'''
class hand_over_machineSM(Behavior):
	'''
	TODO: add description.
	'''


	def __init__(self):
		super(hand_over_machineSM, self).__init__()
		self.name = 'hand_over_machine'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(open_gripper_machineSM, 'open_gripper_machine')
		self.add_behavior(go_to_gripper_machineSM, 'go_to_gripper_machine')
		self.add_behavior(go_to_gripper_machineSM, 'go_to_gripper_machine_2')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365, x:130 y:365
		_state_machine = OperatableStateMachine(outcomes=['succeeded', 'error'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:126 y:70
			OperatableStateMachine.add('open_gripper_machine',
										self.use_behavior(open_gripper_machineSM, 'open_gripper_machine'),
										transitions={'succeeded': 'go_to_gripper_machine', 'error': 'error'},
										autonomy={'succeeded': Autonomy.Inherit, 'error': Autonomy.Inherit})

			# x:308 y:169
			OperatableStateMachine.add('go_to_gripper_machine',
										self.use_behavior(go_to_gripper_machineSM, 'go_to_gripper_machine',
											parameters={'gripper_state': 1}),
										transitions={'succeeded': 'go_to_gripper_machine_2', 'error': 'error'},
										autonomy={'succeeded': Autonomy.Inherit, 'error': Autonomy.Inherit})

			# x:443 y:490
			OperatableStateMachine.add('go_to_gripper_machine_2',
										self.use_behavior(go_to_gripper_machineSM, 'go_to_gripper_machine_2',
											parameters={'gripper_state': 0}),
										transitions={'succeeded': 'succeeded', 'error': 'error'},
										autonomy={'succeeded': Autonomy.Inherit, 'error': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
