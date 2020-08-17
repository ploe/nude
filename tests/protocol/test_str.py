"""unittests for nude.protocol.str Type"""

import unittest

import nude.protocol.str

class TestProtocolStr(unittest.TestCase):
    """Tests for nude.protocol.str"""

    def test_str_init(self):
        """unittest to ensure we can create a new nude.protocol.str.Type"""
        protocol_type = nude.protocol.str.Type({})
        self.assertIsInstance(protocol_type, nude.protocol.str.Type)

    def test_schema_uppercase(self):
        """unittest to check the 'uppercase?' constraint only accepts bool"""

        component = {
            'uppercase?': 'Not a bool',
        }

        # Does an incorrect type raise the correct error?
        with self.assertRaises(nude.protocol.str.ConstraintDefinitionError):
            nude.protocol.str.Type(component)

        component = {
            'uppercase?': True,
        }

        # Does a bool return a new protocol_type?
        protocol_type = nude.protocol.str.Type(component)
        self.assertIsInstance(protocol_type, nude.protocol.str.Type)

    def test_constraint_uppercase(self):
        """unittest to ensure uppercase? validator works as expected"""
        component = {
            'uppercase?': True,
        }

        protocol_type = nude.protocol.str.Type(component)

        # Should generate an error in the list
        errors = protocol_type.validate('lowercase')
        self.assertTrue(errors, list)

        # List should be empty
        errors = protocol_type.validate('UPPERCASE')
        self.assertFalse(errors, list)

        component = {
            'uppercase?': False,
        }

        protocol_type = nude.protocol.str.Type(component)

        # List should be empty
        errors = protocol_type.validate('lowercase')
        self.assertFalse(errors, list)

        # Should generate an error in the list
        errors = protocol_type.validate('UPPERCASE')
        self.assertTrue(errors, list)
