# -*- coding: utf-8 -*-
"""
Created on Fri May 15 18:53:29 2020

@author: Martin Chudjak
"""
import pytest
from interview_assignment_ma.utils.reverse_and_uppercase import \
    reverse_and_uppercase
from interview_assignment_ma.utils.reverse_and_uppercase import parse_arguments
from interview_assignment_ma.utils.reverse_and_uppercase import reverse_string
from interview_assignment_ma.utils.reverse_and_uppercase import \
    uppercase_string
from interview_assignment_ma.utils.reverse_and_uppercase import \
    read_string_from_file


def test_parse_arguments(tmpdir):
    """Tests for parse_arguments()"""
    # Test cases with one word
    cmd_arguments = ['Hello!']
    assert parse_arguments(cmd_arguments) == (True, True, 'Hello!', None)
    cmd_arguments = ['Hello!', '-r']
    assert parse_arguments(cmd_arguments) == (True, False, 'Hello!', None)
    cmd_arguments = ['Hello!', '-u']
    assert parse_arguments(cmd_arguments) == (False, True, 'Hello!', None)
    cmd_arguments = ['Hello!', '-r', '-u']
    assert parse_arguments(cmd_arguments) == (True, True, 'Hello!', None)

    # Test cases with many words in the string to process
    cmd_arguments = ['Hello nice world!']
    assert parse_arguments(cmd_arguments) == (True, True, 'Hello nice world!',
                                              None)
    cmd_arguments = ['Hello nice world!', '-r']
    assert parse_arguments(cmd_arguments) == (True, False, 'Hello nice world!',
                                              None)
    cmd_arguments = ['Hello nice world!', '-u']
    assert parse_arguments(cmd_arguments) == (False, True, 'Hello nice world!',
                                              None)
    cmd_arguments = ['Hello nice world!', '-r', '-u']
    assert parse_arguments(cmd_arguments) == (True, True, 'Hello nice world!',
                                              None)

    # Test for input with file name
    file = tmpdir.join('test_file.txt')
    file.write('TEST STRING')
    cmd_arguments = ['-f', file.strpath, '-r', '-u']
    assert parse_arguments(cmd_arguments) == (True, True, 'TEST STRING',
                                              file.strpath)

    # Tests if correct exception is rised in case of wrong flag on input
    with pytest.raises(SystemExit):
        cmd_arguments = ['-t']
        assert parse_arguments(cmd_arguments)

    # Tests wrong number of arguments
    with pytest.raises(TypeError):
        cmd_arguments = []
        assert parse_arguments(cmd_arguments, 'Aditional argument')


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

    # Tests wrong number of arguments
    with pytest.raises(TypeError):
        assert reverse_and_uppercase(
            '',
            reverse_bool=False,
            uppercase_bool=False,
            string_to_process='',
            )


def test_reverse_string():
    """Tests for reverse_string()"""
    # Test for correct reversion
    assert reverse_string('Hello world.') == '.dlrow olleH'
    assert reverse_string('.,;~`@5$#(%$^*]\\ľščťžýáíéňäô') == \
        'ôäňéíáýžťčšľ\\]*^$%(#$5@`~;,.'

    # Tests if correct exception is raised in case of wrong input type
    with pytest.raises(Exception):
        assert reverse_string(12)
    with pytest.raises(Exception):
        assert reverse_string(12.1)

    # Tests wrong number of arguments
    with pytest.raises(TypeError):
        assert reverse_string(
            '', 'Aditional argument'
            )


def test_uppercase_string():
    """Tests for uppercase_string()"""
    # Test for correct uppercasing a string
    assert uppercase_string('Hello world.') == 'HELLO WORLD.'
    assert uppercase_string('.,;~`@5$#(%$^*]\\;ľščťžýáíéňäô') == \
        '.,;~`@5$#(%$^*]\\;ĽŠČŤŽÝÁÍÉŇÄÔ'

    # Tests if correct exception is raised in case of wrong input type
    with pytest.raises(Exception):
        assert uppercase_string(12)
    with pytest.raises(Exception):
        assert uppercase_string(12.1)

    # Tests wrong number of arguments
    with pytest.raises(TypeError):
        assert uppercase_string(
            '', 'Aditional argument'
            )


def test_read_string_from_file(tmpdir):
    """Tests for read_string_from_file()"""
    # Test if string is read correctly from a file containing 1 line
    file = tmpdir.join('testfile.txt')
    file.write('TEST STRING')
    assert read_string_from_file(file.strpath) == 'TEST STRING'

    # Test if string is read correctly from a file containing 2 lines
    file = tmpdir.join('testfile.txt')
    file.write('TEST STRING1\nTEST STRING2')
    assert read_string_from_file(file.strpath) == 'TEST STRING1\nTEST STRING2'

    # Tests if the correct Error is raised in case of missing file
    with pytest.raises(FileNotFoundError):
        assert read_string_from_file('nonexistting_file')
