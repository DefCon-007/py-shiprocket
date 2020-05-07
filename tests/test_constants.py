from unittest import TestCase

from shiprocket import OrderStatus

class TestConstants(TestCase):

    def test_values(self): 
        self.assertEqual(OrderStatus.NEW_ORDER, "1")


    # def test_is_string(self):
    #     s = funniest.joke()
    #     self.assertTrue(isinstance(s, basestring))