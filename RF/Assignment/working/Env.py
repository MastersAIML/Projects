import numpy as np
import math
import random
import itertools
from itertools import product

# Defining hyperparameters
m = 5  # number of cities, ranges from 1 ..... m
t = 24  # number of hours, ranges from 0 .... t-1
d = 7  # number of days, ranges from 0 ... d-1
C = 5  # Per hour fuel and other costs
R = 9  # per hour revenue from a passenger

class CabDriver():

    def __init__(self):
        """initialise your state and define your action space and state space"""
        self.locations = np.arange(0,5) # locations assumption of A-0 ... E=4
        self.days = np.arange(0, 7) # 7 days of week encoded as 0..6
        self.hours = np.arange(0, 24,dtype=np.int) # 24 hours encoded as 0..23
        self.interim_commute_time = 0 # placeholder for commute time when pickup & drop locations are not same
        self.pickup_drop_time = 0 # time spent in dropping passenger from pickup to drop location
        self.total_commute = 0 # total commute time for pickup and drop. total_commute=interim_commute_time+pickup_drop_time
        self.state_size=36 #architecture 1 
        # self.state_size=46 #architecture 2

        self.action_space = [a for a in list(product(self.locations, self.locations)) if a[0] != a[1]]  # 20 possible actions
        self.action_size = len(self.action_space)
        # STATE is [location, hours, days]
        self.state_space = [a for a in list(product(self.locations, self.hours, self.days))]
        self.state_init =self.state_space[np.random.randint(len(self.state_space))]
        self.reset()

    # Utility functions
    def day_time_changer(self, hour, week_day):
        """Time and week day calculations, it cares of changing the week day based on time """
        while hour >= 24:
            if hour == 24:
                week_day = week_day+1
                hour = 0
            elif hour > 24:
                week_day = week_day+1
                hour = hour-24
            if week_day > 6:
                week_day = week_day-7
        return (hour, week_day)

    # Encoding state (or state-action) for NN input

    def state_encod_arch1(self, state):
        """convert the state into a vector so that it can be fed to the NN. 
        This method converts a given state into a vector format. Hint: The vector is of size m + t + d."""
        location_vec = np.eye(m, dtype=np.int16)[int(state[0])]
        hour_vec = np.eye(t, dtype=np.int16)[int(state[1])]
        day_vec = np.eye(d, dtype=np.int16)[int(state[2])]
        state_encod = np.concatenate((location_vec, hour_vec, day_vec))
        return state_encod

    # Getting number of requests

    def requests(self, state):
        """Determining the number of requests basis the location.
        Use the table specified in the MDP and complete for rest of the locations"""
        location = state[0]
        if location == 0 :
            requests = np.random.poisson(2)
        elif location == 1 :
            requests = np.random.poisson(12)
        elif location == 2 :
            requests = np.random.poisson(4)
        elif location == 3 :
            requests = np.random.poisson(7)
        elif location == 4 :
            requests = np.random.poisson(8)
        if requests > 15:
            requests = 15

        possible_actions_index = random.sample(range(0, (m-1)*m), requests)
        actions = [self.action_space[i] for i in possible_actions_index]
        actions.append((0, 0))  # (0,0) is not considered as customer request, this is added to each request considering driver going offline
        return possible_actions_index, actions

    def reward_func(self, state, action, Time_matrix):
        """Takes in state, action and Time-matrix and returns the reward"""
        # Reward function returns revenue earned from pickup point p to drop point q) 
        #   # C = 5  # Per hour fuel and other costs, # R = 9  # per hour revenue from a passenger
        # r1=(self.pickup_drop_time*9)-(self.total_commute*5) 
        r2=(self.pickup_drop_time*9)-(self.interim_commute_time*5)-(self.pickup_drop_time*5)
        reward=r2
        return reward

    def next_state_func(self, state, action, Time_matrix):
        """Takes state and action as input and returns next state
            Output: 
                next_state: (location,hour_of_day,day_of_week) 
                action: (p,q) 
                reward: <float> 
                is_terminal: False|True"""
        if not isinstance(action,tuple):
            action=self.action_space[action]
        is_terminal=False
        self.interim_commute_time=0
        self.pickup_drop_time=0
        pickup_location=action[0]
        drop_location=action[1]
        current_location=state[0]
        hour_of_day=state[1]
        day_of_week=state[2]
        if action[0]!=0 and action[1]!=0:    
            if current_location!=pickup_location:
                self.interim_commute_time=Time_matrix[current_location][pickup_location][int(hour_of_day)][day_of_week]
                hour_of_day=self.interim_commute_time+hour_of_day
                hour_of_day,day_of_week= self.day_time_changer(hour_of_day,day_of_week)
                current_location=pickup_location
            
            self.pickup_drop_time=Time_matrix[current_location][drop_location][int(hour_of_day)][day_of_week]
            hour_of_day=hour_of_day+self.pickup_drop_time
            hour_of_day,day_of_week= self.day_time_changer(hour_of_day,day_of_week)
        
            self.total_commute=self.total_commute+self.interim_commute_time+self.pickup_drop_time
            reward=self.reward_func(state,action,Time_matrix)
        else:
            drop_location=current_location
            hour_of_day,day_of_week=self.day_time_changer(hour_of_day+1,day_of_week)
            reward=0 # as per the MDP process guidelines where driver get reward of 0 and hour is moved +1
        if self.total_commute>=720:
            is_terminal=True
        next_state=((drop_location,hour_of_day,day_of_week),action,reward,is_terminal) #state returned without encoding
        return next_state

    def reset(self):
        """Output
            \n action_space:<list>
            \n state_space:<list>
            \n state_init: (location,hour_of_day,day_of_week)
        """
        self.total_commute=0
        return self.action_space, self.state_space, self.state_init
