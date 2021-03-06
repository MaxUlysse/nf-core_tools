#!/usr/bin/env python
""" Tests covering for utility functions.
"""

import nf_core.utils

import unittest


class TestUtils(unittest.TestCase):
    """Class for utils tests"""

    def test_check_if_outdated_1(self):
        current_version = "1.0"
        remote_version = "2.0"
        is_outdated, current, remote = nf_core.utils.check_if_outdated(current_version, remote_version)
        assert is_outdated

    def test_check_if_outdated_2(self):
        current_version = "2.0"
        remote_version = "2.0"
        is_outdated, current, remote = nf_core.utils.check_if_outdated(current_version, remote_version)
        assert not is_outdated

    def test_check_if_outdated_3(self):
        current_version = "2.0.1"
        remote_version = "2.0.2"
        is_outdated, current, remote = nf_core.utils.check_if_outdated(current_version, remote_version)
        assert is_outdated

    def test_check_if_outdated_4(self):
        current_version = "1.10.dev0"
        remote_version = "1.7"
        is_outdated, current, remote = nf_core.utils.check_if_outdated(current_version, remote_version)
        assert not is_outdated

    def test_check_if_outdated_5(self):
        current_version = "1.10.dev0"
        remote_version = "1.11"
        is_outdated, current, remote = nf_core.utils.check_if_outdated(current_version, remote_version)
        assert is_outdated
