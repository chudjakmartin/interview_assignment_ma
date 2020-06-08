# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 15:55:09 2020

@author: Martin Chudjak
"""
import argparse
from statistics import mean

import apache_beam as beam
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions


def get_city_and_tmax(element):
    """
    Process one element from the input dataset.

    Try to convert tmax column to float. If it is not possible returns tuple
    of the form ('wrong_input', 0.0)

    Parameters
    ----------
    element (string): row from source dataset. Columns are expected to be
    separated by comma.

    Returns
    -------
    out_tuple (tuple): city, tmax
    """
    line = element.split(',')
    try:
        out_tuple = (line[6], float(line[21]))
    except ValueError:
        out_tuple = ('wrong_input', 0.0)
    return out_tuple


def get_city_means(city_temperatures):
    """Computes mean of the temperatures for the given city."""
    (city, mean_temp) = city_temperatures
    return (city, mean(mean_temp))


def format_result(input_tuple):
    """Format tuple to the form: key_string,float.
    The float is rounded to 3 decimal places."""
    (key, value) = input_tuple
    return '{},{:.3f}'.format(key, value)


def count_ones(city_ones):
    """Computes number of city occurences."""
    (city, ones) = city_ones
    return (city, sum(ones))


def run_main(argv=None, save_main_session=True):
    """Pipeline for processing weather .

    It works with the dataset
    https://www.kaggle.com/PROPPG-PPG/hourly-weather-surface-brazil-southeast-region

    It produces two datasets:
        - Mean of maximum measured temperature in each city included in dataset
        Colums: city, mean tmax for that city
        - Number of records per city in source dataset
        Columns: city, number of records for that city
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input',
        dest='input',
        required=True,
        help='Input file to process.')
    parser.add_argument(
        '--output_temp',
        dest='output_temp',
        required=True,
        help='Output file for the city means of tmax.')
    parser.add_argument(
        '--output_counts',
        dest='output_counts',
        required=True,
        help='Output file for num of records per city.')
    known_args, pipeline_args = parser.parse_known_args(argv)

    pipeline_options = PipelineOptions(pipeline_args)
    pipeline_options.view_as(SetupOptions).save_main_session = \
        save_main_session
    pipeline = beam.Pipeline(options=pipeline_options)

    lines = pipeline | beam.io.ReadFromText(known_args.input)

    city_tmax = (
        lines
        | 'get city tmax' >> beam.Map(get_city_and_tmax)
        )

    temp_means = (
        city_tmax
        | 'group by city' >> beam.GroupByKey()
        | 'get mean' >> beam.Map(get_city_means)
        | 'format city means' >> beam.Map(format_result)
        )

    # pylint: disable=expression-not-assigned
    temp_means | 'write means' >> WriteToText(known_args.output_temp)

    name_counts = (
        city_tmax
        | 'pair city with one' >> beam.Map(lambda x: (x[0], 1))
        | 'group' >> beam.GroupByKey()
        | 'count' >> beam.Map(count_ones)
        | 'format city counts' >> beam.Map(lambda x:
                                           '{},{}'.format(x[0], x[1]))
        )

    # pylint: disable=expression-not-assigned
    name_counts | 'write occurence' >> WriteToText(known_args.output_counts)

    result = pipeline.run()
    result.wait_until_finish()


if __name__ == '__main__':
    run_main()
