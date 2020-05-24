# -*- coding: utf-8 -*-
"""
Created on Fri May 15 16:19:48 2020

@author: Martin Chudjak
Module for revert a string and/or make it uppercase
"""
import argparse


def parse_arguments(cmd_arguments=None):
    """
    Parse argument from the cmd so they may be used
    by the reverse_and_uppercase() function.

    Parameters
    -------
        cmd_arguments (list): Variable to pass arguments during testing

    Returns
    -------
        input_variables['r'] (bool): If True, string should be reversed
        input_variables['u'] (bool): If True, string should be uppercased
        string_to_process (str): Contains whole string to process
    """
    parser = argparse.ArgumentParser(
        description='Function revert a string and/or make it uppercase.'
        'Default behavior is reverse and uppercase.',
        argument_default='')
    parser.add_argument('-r',
                        action="store_true",
                        help='If argument given, reverse the input string.',
                        default=False)
    parser.add_argument('-u',
                        action="store_true",
                        help='If argument given, transforms the input string'
                        'to uppercase.',
                        default=False)
    parser.add_argument('string_to_process',
                        action="store",
                        nargs='*', default='', type=str, help='input string')
    input_variables = vars(parser.parse_args(cmd_arguments))

    string_to_process = ' '.join(input_variables['string_to_process'])

    # if no flag given, we want both bool vars to be True
    if (not input_variables['r']) and (not input_variables['u']):
        input_variables['r'], input_variables['u'] = True, True
    return input_variables['r'], input_variables['u'], string_to_process


def reverse_string(input_string=''):
    """
    Resevre the input_string.

    Parameters
    -------
        input_string (str): string to be reverted

    Returns
    -------
        output_string (str): reverted string
    """
    try:
        output_string = input_string[::-1]
    except TypeError:
        raise Exception("Invalid input format")
    return output_string


def uppercase_string(input_string=''):
    """
    Transform input string to uppercase.

    Parameters
    ----------
        input_string (str): string to be uppercased

    Returns
    -------
        output_string (str): string transformed to uppercase

    """
    try:
        output_string = input_string.upper()
    except AttributeError:
        raise Exception("Invalid input format")
    return output_string


def reverse_and_uppercase(reverse_bool=True, uppercase_bool=True,
                          string_to_process=''):
    """
    Function revert a string and/or make it uppercase.

    Parameters
    -------
        reverse_bool (bool): If True, string should be reversed
        uppercase_bool (bool): If True, string should be uppercased
        string_to_process (str): Contains whole string to process
    Returns
    -------
        string_to_process (str): Processed string
    """
    if reverse_bool:
        string_to_process = reverse_string(string_to_process)
    if uppercase_bool:
        string_to_process = uppercase_string(string_to_process)

    return string_to_process


if __name__ == '__main__':
    print('Reversed input string in the uppercase is: %s'
          % reverse_and_uppercase(*parse_arguments()))
