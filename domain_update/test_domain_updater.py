import unittest
from domain_update import update_domain

class DomainUpdateTest(unittest.TestCase):
    def test_update_domain(self):
        testcase = update_domain('jacob@olddomain.xyz', 'gmail.com', 'olddomain.xyz')
        self.assertEqual(testcase, 'jacob@gmail.com')
    
    def test_update_domain_2(self):
        testcase = update_domain('dennis@oldhotm.ru', 'gmail.com', 'oldhotm.ru')
        self.assertEqual(testcase, 'dennis@gmail.com')

unittest.main()