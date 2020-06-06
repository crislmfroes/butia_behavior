#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from butia_flexbe_behaviors.go_to_fixed_machine_sm import go_to_fixed_machineSM
from butia_flexbe_states.wait_topic import WaitTopicState
from butia_flexbe_states.say_something import SaySomethingState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri Jun 05 2020
@author: Cris Lima Froes
'''
class good_morning_rsSM(Behavior):
	'''
	Apresenta o Bom Dia Rio Grande.
	'''


	def __init__(self):
		super(good_morning_rsSM, self).__init__()
		self.name = 'good_morning_rs'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(go_to_fixed_machineSM, 'go_to_fixed_machine')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365, x:130 y:365, x:230 y:365, x:330 y:365, x:430 y:365
		_state_machine = OperatableStateMachine(outcomes=['succeeded', 'error', 'aborted', 'preempted', 'arrived'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:134 y:51
			OperatableStateMachine.add('go_to_fixed_machine',
										self.use_behavior(go_to_fixed_machineSM, 'go_to_fixed_machine',
											parameters={'target': "interview"}),
										transitions={'succeeded': 'wait_hello', 'aborted': 'aborted', 'preempted': 'preempted', 'arrived': 'arrived'},
										autonomy={'succeeded': Autonomy.Inherit, 'aborted': Autonomy.Inherit, 'preempted': Autonomy.Inherit, 'arrived': Autonomy.Inherit})

			# x:418 y:150
			OperatableStateMachine.add('wait_hello',
										WaitTopicState(topic='butia_speech/bhd/detected'),
										transitions={'succeeded': 'good_morning', 'error': 'error'},
										autonomy={'succeeded': Autonomy.Off, 'error': Autonomy.Off})

			# x:272 y:435
			OperatableStateMachine.add('good_morning',
										SaySomethingState(text='Olá pessoal do Bom Dia Rio Grande, venham para o Robótica 2019.'),
										transitions={'succeeded': 'succeeded', 'error': 'error'},
										autonomy={'succeeded': Autonomy.Off, 'error': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
