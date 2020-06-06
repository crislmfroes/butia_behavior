#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from butia_flexbe_states.get_target_pose import GetTargetPoseState
from butia_flexbe_states.goto import GoToState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri Jun 05 2020
@author: Cris Lima Froes
'''
class go_to_machineSM(Behavior):
	'''
	Navigates torwards place.
	'''


	def __init__(self):
		super(go_to_machineSM, self).__init__()
		self.name = 'go_to_machine'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365, x:130 y:365, x:222 y:365, x:330 y:365
		_state_machine = OperatableStateMachine(outcomes=['succeeded', 'aborted', 'preempted', 'arrived'], input_keys=['key'])
		_state_machine.userdata.key = key

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:314 y:19
			OperatableStateMachine.add('get_target_pose',
										GetTargetPoseState(service='/butia_world/get_pose'),
										transitions={'succeeded': 'go_to', 'error': 'aborted', 'arrived': 'arrived'},
										autonomy={'succeeded': Autonomy.Off, 'error': Autonomy.Off, 'arrived': Autonomy.Off},
										remapping={'key': 'key', 'pose': 'pose'})

			# x:26 y:96
			OperatableStateMachine.add('go_to',
										GoToState(frame='map'),
										transitions={'succeeded': 'succeeded', 'aborted': 'aborted', 'preempted': 'preempted'},
										autonomy={'succeeded': Autonomy.Off, 'aborted': Autonomy.Off, 'preempted': Autonomy.Off},
										remapping={'pose': 'pose'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
