# test_codeiumext.py
"""
Tests for CodeiumExt module.
"""

import unittest
from codeiumext import CodeiumExt

class TestCodeiumExt(unittest.TestCase):
    """Test cases for CodeiumExt class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CodeiumExt()
        self.assertIsInstance(instance, CodeiumExt)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CodeiumExt()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
