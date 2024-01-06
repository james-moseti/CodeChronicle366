import unittest
from domain_update import update_domain

class DomainUpdateTest(unittest.TestCase):
    def test_update_domain(self):
        testcase = update_domain('jacob@yahoo.com', 'gmail.com', 'yahoo.com')
        self.assertEqual(testcase, 'jacob@gmail.com')
    
    def test_update_domain_2(self):
        testcase = update_domain('dennis@hotmail.com', 'gmail.com', 'hotmail.com')
        self.assertEqual(testcase, 'dennis@gmail.com')

unittest.main()