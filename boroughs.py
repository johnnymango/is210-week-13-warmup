#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Boros"""

import csv
import json


GRADES = {
    'A': 1.00,
    'B': .90,
    'C': .80,
    'D': .70,
    'F': .60
    }


def get_score_summary(mycsvfile):
    """This functions returns a summary of boro statistics.

    Args:
        mycsvfile (str): The boro csv file.

    Returns:
        Dictionary: containing the summary boro data.

    Example:
    >>> get_score_summary('inspection_results.csv')
    >>> {'BRONX': (156, 0.9762820512820514), 'BROOKLYN':
    (417, 0.9745803357314141), 'STATEN ISLAND': (46, 0.9804347826086955),
    'MANHATTAN': (748, 0.9771390374331531), 'QUEENS':
    (414, 0.9719806763285017)}
    """
    myfile = open(mycsvfile, 'r')

    csvfile = csv.reader(myfile)
    next(csvfile)

    mydict = {}
    for row in csvfile:
        if row[0] not in mydict and row[10] != '' and row[10] != 'P':
            mydict[row[0]] = row[1], row[9], row[10]

    myfile.close()

    bronxtotal = 0
    bronxscores = 0
    brooklyntotal = 0
    brooklynscores = 0
    sitotal = 0
    siscores = 0
    queenstotal = 0
    queensscores = 0
    manhattantotal = 0
    manhattanscores = 0

    for myvalue in mydict.itervalues():

        if myvalue[0] == 'MANHATTAN':
            manhattantotal += 1
            manhattanscores += int(myvalue[1])

        if myvalue[0] == 'BROOKLYN':
            brooklyntotal += 1
            brooklynscores += int(myvalue[1])

        if myvalue[0] == 'BRONX':
            bronxtotal += 1
            bronxscores += int(myvalue[1])

        if myvalue[0] == 'QUEENS':
            queenstotal += 1
            queensscores += int(myvalue[1])

        if myvalue[0] == 'STATEN ISLAND':
            sitotal += 1
            siscores += int(myvalue[1])

    borostats = {
        'BROOKLYN': (brooklyntotal, (brooklynscores / brooklyntotal)),
        'BRONX': (bronxtotal, (bronxscores / bronxtotal)),
        'QUEENS': (queenstotal, (queensscores / queenstotal)),
        'MANHATTAN': (manhattantotal, (manhattanscores / manhattantotal)),
        'STATEN ISLAND': (sitotal, (siscores / sitotal))
        }

    return borostats


def get_market_density(myjsonfile):
    """This fucntion process a json file.

    Args:
        myjsonfile(str): The JSON file name.

    Returns:
        Dictionary: containing market data.

    Examples:
    >>> get_market_density('green_markets.json')
    {u'STATEN ISLAND': 2, u'BROOKLYN': 48, u'BRONX': 32,
    u'MANHATTAN': 39, u'QUEENS': 16}

    """
    jsonfile = open(myjsonfile, 'r')
    dataload = json.load(jsonfile)
    data = dataload['data']

    bxcount = 0
    mhcount = 0
    qncount = 0
    sicount = 0
    bkcount = 0

    markets = {}
    for values in data:
        boro = values[8].strip().upper()

        if boro == 'BRONX':
            bxcount += 1
            markets[boro] = bxcount

        if boro == 'QUEENS':
            qncount += 1
            markets[boro] = qncount

        if boro == 'MANHATTAN':
            mhcount += 1
            markets[boro] = mhcount

        if boro == 'BROOKLYN':
            bkcount += 1
            markets[boro] = bkcount

        if boro == 'STATEN ISLAND':
            sicount += 1
            markets[boro] = sicount

    return markets
