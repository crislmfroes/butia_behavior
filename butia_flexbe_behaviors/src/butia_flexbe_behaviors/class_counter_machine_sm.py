#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from butia_flexbe_states.label_class_counter import ClassesCountHistoryState
from butia_flexbe_states.label_class_counter_reductor import ClassesHistoryReductorState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri Jun 05 2020
@author: Cris Lima Froes
'''
class class_counter_machineSM(Behavior):
	'''
	Count classes.
	'''


	def __init__(self):
		super(class_counter_machineSM, self).__init__()
		self.name = 'class_counter_machine'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		topic = None
		window_size = None
		reductor = None
		# x:30 y:365, x:130 y:365
		_state_machine = OperatableStateMachine(outcomes=['succeeded', 'error'], output_keys=['registers'])
		_state_machine.userdata.registers = None

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('count_history',
										ClassesCountHistoryState(topic=topic, window_size=window_size),
										transitions={'succeeded': 'history_reductor', 'error': 'error'},
										autonomy={'succeeded': Autonomy.Off, 'error': Autonomy.Off},
										remapping={'counts_history': 'counts_history'})

			# x:184 y:119
			OperatableStateMachine.add('history_reductor',
										ClassesHistoryReductorState(reduction_func=reductor),
										transitions={'succeeded': 'succeeded', 'error': 'error'},
										autonomy={'succeeded': Autonomy.Off, 'error': Autonomy.Off},
										remapping={'counts_history': 'counts_history', 'classes_count': 'registers'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
