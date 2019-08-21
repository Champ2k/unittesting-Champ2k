import unittest
from listutil import unique

class ListutilTest(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual([], unique([]))

    def test_one_item(self):
        self.assertEqual([1], unique([1]))
        self.assertEqual(["a"], unique(["a"]))
    
    def test_one_item_many_times(self):
        self.assertEqual(["q","w",2,3,4], unique(["q","w","w","w","w",2,3,4,4,4,4,4,4]))

    def test_many_item_many_times_many_orders(self):
        self.assertEqual([["a","a","b","c","a",1]], unique([["a","a","b","c","a",1],["a","a","b","c","a",1]]))
        self.assertEqual([[2,3,4,5,1],["a","a","b","c","a"]], unique([[2,3,4,5,1],[2,3,4,5,1],["a","a","b","c","a"]]))

    def test_int(self):
        with self.assertRaises(TypeError):
            unique_list = list(4123)

    def test_name(self):
        with self.assertRaises(NameError):
            unique_list = list(Name)
    
    def test_str(self):
        self.assertEqual(['N', 'a', 'm', 'e'], unique("Name"))
