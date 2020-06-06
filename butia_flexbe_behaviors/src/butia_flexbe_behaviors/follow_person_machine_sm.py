#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from butia_flexbe_states.track_person import TrackPersonState
from butia_flexbe_states.set_fixed_query import SetFixedQueryState
from butia_flexbe_states.get_key import GetKeyState
from butia_flexbe_behaviors.go_to_machine_sm import go_to_machineSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri Jun 05 2020
@author: Cris Lima Froes
'''
class follow_person_machineSM(Behavior):
	'''
	Follows person.
	'''


	def __init__(self):
		super(follow_person_machineSM, self).__init__()
		self.name = 'follow_person_machine'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(go_to_machineSM, 'go_to_machine')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365, x:130 y:365, x:230 y:365, x:330 y:365
		_state_machine = OperatableStateMachine(outcomes=['succeeded', 'aborted', 'preempted', 'arrived'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('track',
										TrackPersonState(service='/butia_vision/pt/start'),
										transitions={'succeeded': 'set_query', 'error': 'aborted'},
										autonomy={'succeeded': Autonomy.Off, 'error': Autonomy.Off})

			# x:267 y:38
			OperatableStateMachine.add('set_query',
										SetFixedQueryState(query='*tracked_person*'),
										transitions={'succeeded': 'get_key', 'error': 'aborted'},
										autonomy={'succeeded': Autonomy.Off, 'error': Autonomy.Off},
										remapping={'query': 'query'})

			# x:484 y:32
			OperatableStateMachine.add('get_key',
										GetKeyState(method='closest'),
										transitions={'succeeded': 'go_to_machine', 'error': 'aborted'},
										autonomy={'succeeded': Autonomy.Off, 'error': Autonomy.Off},
										remapping={'query': 'query', 'key': 'key'})

			# x:543 y:240
			OperatableStateMachine.add('go_to_machine',
										self.use_behavior(go_to_machineSM, 'go_to_machine'),
										transitions={'succeeded': 'set_query', 'aborted': 'set_query', 'preempted': 'preempted', 'arrived': 'arrived'},
										autonomy={'succeeded': Autonomy.Inherit, 'aborted': Autonomy.Inherit, 'preempted': Autonomy.Inherit, 'arrived': Autonomy.Inherit},
										remapping={'key': 'key'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
