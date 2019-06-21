import unittest
from itertools import product
from Env import CabDriver
import numpy as np
import HtmlTestRunner

class Test_Env(unittest.TestCase):
    def setUp(self):
        self.env=CabDriver()
        self.locations=['A','B','C','D','E']
        self.test_action_space=[a for a in list(product(self.locations,self.locations)) if a[0]!=a[1]]
        # self.test_action_space.extend([(0,0)])
        self.week_days=np.arange(0,7)
        self.hours_in_day=np.arange(0,24)
        self.time_matrix=np.load('./TM.npy')

    # TEST SCENARIOS
    def test_init_len_of_action_space(self):
        self.assertEqual(20,len(self.env.action_space),
        msg="The action_space is not of length 20 {}".format(self.env.action_space))
    def test_init_elements_of_action_space(self):
        self.assertCountEqual(self.env.action_space,self.test_action_space,
        msg="The action_space is not same\n Env action_space {} \nExpected action space {}".format(self.env.action_space,self.test_action_space))
    def test_init_state_space(self):
        self.assertEqual(len(self.locations)*len(self.week_days)*len(self.hours_in_day), len(self.env.state_space),
        msg="The lenght of state_space is not of length 840 -> env state_space_lenght {}".format(len(self.env.state_space)))
    def test_init_elements_of_state_space(self):
        self.assertCountEqual(product(self.locations,self.hours_in_day,self.week_days),self.env.state_space,
        msg="The lenght of state_space is not of length 840 -> env state_space_lenght {}".format(len(self.env.state_space)))
    def test_hours(self):
        pass
    def test_days(self):
        pass
    def test_locations(self):
        pass
    def test_state_encod_arch1(self):
        self.assertEqual(len(self.locations)+self.week_days.size+self.hours_in_day.size, self.env.state_encod_arch1(('B',23,5)).size,
        msg="Failure: Length of encoded vector is not 36")
    def test_state_encod_arch2(self):
        self.assertEqual(len(self.locations)+self.week_days.size+self.hours_in_day.size+len(self.locations)+len(self.locations), 
        self.env.state_encod_arch2(('B',23,5),('C','D')).size,msg="Failure: Length of encoded vector is not 46")
    def test_offline_state_encod_arch2(self):
        self.assertCountEqual([0,0,0,0,0,0,0,0,0,0],self.env.state_encod_arch2(('B',23,5),(0,0))[36:46],msg="Failure: Length of encoded vector is not 46")
    def test_request(self):
        index,a_s=self.env.requests(('A',6,10))
        self.assertLess(len(index),len(a_s))
    def test_day_time_changer_1(self):
        self.assertEqual((10,6),self.env.day_time_changer(10,6))
    def test_day_time_changer_2(self):
        self.assertEqual((0,0),self.env.day_time_changer(24,6))
    def test_day_time_changer_3(self):
        self.assertEqual((1,0),self.env.day_time_changer(25,6))
    def test_day_time_changer_4(self):
        self.assertEqual((5,1),self.env.day_time_changer(53,6))
    def test_day_time_changer_5(self):
        self.assertEqual((5,6),self.env.day_time_changer(53,4))
    def test_day_time_changer_6(self):
        self.assertEqual((5,0),self.env.day_time_changer(53,5))
    
    def test_next_state_same_location(self):
        self.assertEqual('C',self.env.next_state_func(('B',12,4),('B','C'),self.time_matrix)[0][0])
    def test_next_state_same_location_day_change(self):
        self.assertEqual(9,self.env.next_state_func(('B',23,4),('B','C'),self.time_matrix)[0][1])
    
    def test_reward_1(self):
        self.env.next_state_func(('B',12,4),('B','C'),self.time_matrix)
        expected_reward=(9*self.env.pickup_drop_time)-(self.env.total_commute*5)
        self.assertEqual(expected_reward,self.env.reward_func(('B',12,4),('B','C'),self.time_matrix))
 
    def test_get_dict_keys(self):
        self.assertEqual(0,self.env.get_dict_keys('A'))
    # TEST SCENARIOS ENDS
    def tearDown(self):
        self.test_action_space.clear()

if __name__=='__main__':
    TM_data=np.load('TM.npy')
    ## for console testing
    # unittest.main()
    test_suite = unittest.TestSuite()
    test = unittest.makeSuite(Test_Env)
    test_runner = HtmlTestRunner.HTMLTestRunner(output='./')
    unittest.main(testRunner=test_runner)
    