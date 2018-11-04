import unittest
from full_names import get_full_name

class NamesTestCase(unittest.TestCase):
    """Tests for names.py."""
    
    def test_first_last(self):
        """Test names like Janis Joplin."""
        full_name = get_full_name('janis','joplin')
        self.assertEqual(full_name, 'Janis Joplin')
    
    def test_middle(self):
        """Test names like David Lee Roh"""
        full_name = get_full_name('david','roth','lee')
        self.assertEqual(full_name, 'David Roth Lee')

unittest.main()
