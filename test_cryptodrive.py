# test_cryptodrive.py
"""
Tests for CryptoDrive module.
"""

import unittest
from cryptodrive import CryptoDrive

class TestCryptoDrive(unittest.TestCase):
    """Test cases for CryptoDrive class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoDrive()
        self.assertIsInstance(instance, CryptoDrive)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoDrive()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
