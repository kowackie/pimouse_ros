#!/usr/bin/env python3

import time

import rospy
import unittest
import rostest
import rosnode

class BuzzerTest(unittest.TestCase):
    def test_node_exist(self):
        nodes = rosnode.get_node_names()
        self.assertIn('/buzzer', nodes, "node does not exist")

if __name__ == '__main__':
    time.sleep(3)
    rospy.init_node('travis_test_buzzer')
    rostest.rosrun('pimouse_ros', 'travis_test_buzzer', BuzzerTest)
