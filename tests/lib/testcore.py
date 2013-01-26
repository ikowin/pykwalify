# -*- coding: utf-8 -*-

""" Unit test for pyKwalify - Core """

# Testhelper class
from tests.testhelper import TestHelper, gettestcwd, _set_log_lv

# pyKwalify imports
from pykwalify.core import Core

class TestCore(TestHelper):

    def f(self, *args):
        return gettestcwd("tests", "files", *args)

    def testCoreDataMode(self):
        Core(source_data = 3.14159,  schema_data = {"type": "number"} ).run_core()
        Core(source_data = 3.14159,  schema_data = {"type": "float"} ).run_core()
        Core(source_data = 3,        schema_data = {"type": "int"} ).run_core()
        Core(source_data = True,     schema_data = {"type": "bool"} ).run_core()
        Core(source_data = "foobar", schema_data = {"type": "str"} ).run_core()
        Core(source_data = "foobar", schema_data = {"type": "text"} ).run_core()
        Core(source_data = "foobar", schema_data = {"type": "any"} ).run_core()

        with self.assertRaises(Exception):
            Core(source_data = "abc",  schema_data = {"type": "number"} ).run_core()

        with self.assertRaises(Exception):
            Core(source_data = 3, schema_data = {"type": "float"} ).run_core()

        with self.assertRaises(Exception):
            Core(source_data = 3.14159, schema_data = {"type": "int"} ).run_core()

        with self.assertRaises(Exception):
            Core(source_data = 1337, schema_data = {"type": "bool"} ).run_core()

        with self.assertRaises(Exception):
            Core(source_data = 1, schema_data = {"type": "str"} ).run_core()

        with self.assertRaises(Exception):
            Core(source_data = True, schema_data = {"type": "text"} ).run_core()

        with self.assertRaises(Exception):
            Core(source_data = dict, schema_data = {"type": "any"} ).run_core()

    def testCore(self):
        # Test sequence with only string values
        Core(source_file = self.f("1a.yaml"), schema_file = self.f("1b.yaml") ).run_core()

        # Test sequence with defined string content type but data only has integers
        with self.assertRaises(Exception):
            Core(source_file = self.f("2a.yaml"), schema_file = self.f("2b.yaml") ).run_core()

        # Test sequence where the only valid items is integers
        Core(source_file = self.f("3a.yaml"), schema_file = self.f("3b.yaml") ).run_core()

        # Test sequence with only booleans
        Core(source_file = self.f("4a.yaml"), schema_file = self.f("4b.yaml") ).run_core()

        # Test sequence with defined string content type but data only has booleans
        with self.assertRaises(Exception):
            Core(source_file = self.f("5a.yaml"), schema_file = self.f("5b.yaml") ).run_core()

        # Test sequence with defined booleans but with one integer
        with self.assertRaises(Exception):
            Core(source_file = self.f("6a.yaml"), schema_file = self.f("6b.yaml") ).run_core()

        # Test sequence with strings and and lenght on each string
        with self.assertRaises(Exception):
            Core(source_file = self.f("7a.yaml"), schema_file = self.f("7b.yaml") ).run_core()

        # Test mapping with different types of data and some extra conditions
        Core(source_file = self.f("8a.yaml"), schema_file = self.f("8b.yaml") ).run_core()

        # Test mapping that do not work
        with self.assertRaises(Exception):
            Core(source_file = self.f("9a.yaml"), schema_file = self.f("8b.yaml") ).run_core()

        # Test sequence with mapping with valid mapping
        Core(source_file = self.f("10a.yaml"), schema_file = self.f("10b.yaml") ).run_core()

        # Test sequence with mapping with missing required key
        with self.assertRaises(Exception):
            Core(source_file = self.f("11a.yaml"), schema_file = self.f("10b.yaml") ).run_core()

        # Test mapping with sequence with mapping and valid data
        Core(source_file = self.f("12a.yaml"), schema_file = self.f("12b.yaml") ).run_core()

        # Test mapping with sequence with mapping and invalid data
        with self.assertRaises(Exception):
            Core(source_file = self.f("13a.yaml"), schema_file = self.f("12b.yaml") ).run_core()

        # Test most of the implemented functions
        Core(source_file = self.f("14a.yaml"), schema_file = self.f("14b.yaml") ).run_core()

        with self.assertRaises(Exception):
            Core(source_file = self.f("15a.yaml"), schema_file = self.f("14b.yaml") ).run_core()

        # This will test the unique constraint
        Core(source_file = self.f("16a.yaml"), schema_file = self.f("16b.yaml") ).run_core()

        # TODO: The reverse unique do not currently work proper
        # This will test the unique constraint but should fail
        with self.assertRaises(Exception):
            Core(source_file = self.f("17a.yaml"), schema_file = self.f("16b.yaml") ).run_core()

        Core(source_file = self.f("18a.yaml"), schema_file = self.f("18b.yaml") ).run_core()

        Core(source_file = self.f("19a.yaml"), schema_file = self.f("19b.yaml") ).run_core()

        Core(source_file = self.f("20a.yaml"), schema_file = self.f("20b.yaml") ).run_core()

        # This tests number validation rule
        Core(source_file = self.f("21a.yaml"), schema_file = self.f("21b.yaml") ).run_core()

        # This tests number validation rule with wrong data
        with self.assertRaises(Exception):
            Core(source_file = self.f("22a.yaml"), schema_file = self.f("22b.yaml") ).run_core()

        # This test the text validation rule
        Core(source_file = self.f("23a.yaml"), schema_file = self.f("23b.yaml") ).run_core()

        # This test the text validation rule with wrong data
        with self.assertRaises(Exception):
            Core(source_file = self.f("24a.yaml"), schema_file = self.f("24b.yaml") ).run_core()

        # This test the text validation rule
        Core(source_file = self.f("24a.yaml"), schema_file = self.f("25b.yaml") ).run_core()

        Core(source_file = self.f("26a.yaml"), schema_file = self.f("26b.yaml") ).run_core()

        # This tests pattern matching on keys in a map
        with self.assertRaises(Exception):
            Core(source_file = self.f("27a.yaml"), schema_file = self.f("27b.yaml") ).run_core()

        Core(source_file = self.f("28a.yaml"), schema_file = self.f("28b.yaml") )    
        