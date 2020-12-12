
Brief Guide

		!!Group force is added. Here I declare a 2D matrix when the number of EVAC lines is determined.  Users may initialize or modify the matrix by using EVAC Namelist, and this matrix characterizes the social relationship of agents.  
		     
		!! The total number of groups is NPC_EVAC, then DFACTOR_MATRIX is in dimension of NPC_EVAC*NPC_EVAC.  If agents are grouped, there will be sub-matrix for each group, and the final matrix consists of these sub-matrices for groups.  
		     
		!! The integer variable GROUP_FORCE switches on the group force.  Users can modify this integer variable by using PERS Namelist. 
		!GROUP_FORCE == 0: Traditional Social Force
		!GROUP_FORCE == 1: Desired Distance - Repulsive Force - Max - No Traditional SF
		!GROUP_FORCE == 2: Desired Distance - Repulsive Force - No Max - No Traditional SF
		!GROUP_FORCE == 3: Group Force - Repusion or Cohesion - Traditional SF is Kept in computation


For definition of AFactor, BFactor, DFactor, please refer to our document
Modeling Group Behavior of Pedestrian Crowd

AFactor: Better value is 0.01 in Pre-Evac stage.  