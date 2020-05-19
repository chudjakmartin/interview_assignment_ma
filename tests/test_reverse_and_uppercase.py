# -*- coding: utf-8 -*-
"""
Created on Fri May 15 18:53:29 2020

@author: Martin Chudjak
"""
from ..utils.reverse_and_uppercase import reverse_and_uppercase
from ..utils.reverse_and_uppercase import parse_arguments


def test_parse_arguments():
    """Tests for parse_arguments()"""
    # Test cases with one word
    cmd_arguments = ['Hello!']
    assert parse_arguments(cmd_arguments) == (True, True, 'Hello!')
    cmd_arguments = ['Hello!', '-r']
    assert parse_arguments(cmd_arguments) == (True, False, 'Hello!')
    cmd_arguments = ['Hello!', '-u']
    assert parse_arguments(cmd_arguments) == (False, True, 'Hello!')
    cmd_arguments = ['Hello!', '-r', '-u']
    assert parse_arguments(cmd_arguments) == (True, True, 'Hello!')

    # Test cases with many words in the string to process
    cmd_arguments = ['Hello nice world!']
    assert parse_arguments(cmd_arguments) == (True, True, 'Hello nice world!')
    cmd_arguments = ['Hello nice world!', '-r']
    assert parse_arguments(cmd_arguments) == (True, False, 'Hello nice world!')
    cmd_arguments = ['Hello nice world!', '-u']
    assert parse_arguments(cmd_arguments) == (False, True, 'Hello nice world!')
    cmd_arguments = ['Hello nice world!', '-r', '-u']
    assert parse_arguments(cmd_arguments) == (True, True, 'Hello nice world!')


def test_reverse_and_uppercase():
    """Tests for reverse_and_uppercase()"""
    # Tests for nonempty input string to process
    assert reverse_and_uppercase(
        reverse_bool=True, uppercase_bool=True,
        string_to_process='Hello nice world.'
        ) == '.DLROW ECIN OLLEH'
    assert reverse_and_uppercase(
        reverse_bool=True, uppercase_bool=False,
        string_to_process='Hello nice world.'
        ) == '.dlrow ecin olleH'
    assert reverse_and_uppercase(
        reverse_bool=False, uppercase_bool=True,
        string_to_process='Hello nice world.'
        ) == 'HELLO NICE WORLD.'
    assert reverse_and_uppercase(
        reverse_bool=False, uppercase_bool=False,
        string_to_process='Hello nice world.'
        ) == 'Hello nice world.'

    # Tests for empty input string to process
    assert reverse_and_uppercase(
        reverse_bool=True, uppercase_bool=True,
        string_to_process=''
        ) == ''
    assert reverse_and_uppercase(
        reverse_bool=True, uppercase_bool=False,
        string_to_process=''
        ) == ''
    assert reverse_and_uppercase(
        reverse_bool=False, uppercase_bool=True,
        string_to_process=''
        ) == ''
    assert reverse_and_uppercase(
        reverse_bool=False, uppercase_bool=False,
        string_to_process=''
        ) == ''
