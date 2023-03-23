import unittest
from mysqlquerygenerator import generate_query

class TestGenerateQuery(unittest.TestCase):
    
    def test_generate_query(self):
        # Test case 1: select query with one table and no additional parameters
        self.assertEqual(generate_query('select', ['customers'], '', '', ''), "SELECT * FROM customers   ;")
         
if __name__ == '__main__':
    unittest.main()
