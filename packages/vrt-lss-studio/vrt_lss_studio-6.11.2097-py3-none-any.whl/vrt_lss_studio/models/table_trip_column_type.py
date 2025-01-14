# coding: utf-8

"""
    VRt.Studio [ST]

    The version of the OpenAPI document: 6.11.2097

    Generated by OpenAPI Generator: 6.6.0

    Do not edit the code manually

    2023 Veeroute
"""


from inspect import getfullargspec
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class TableTripColumnType(str, Enum):
    """
    Trip table column name. 
    """

    """
    allowed enum values
    """
    ESSENCE_KEY = 'ESSENCE_KEY'
    ENABLED = 'ENABLED'
    PRISTINE = 'PRISTINE'
    TRIP_NAME = 'TRIP_NAME'
    ATTRIBUTES = 'ATTRIBUTES'
    COST = 'COST'
    REWARD = 'REWARD'
    DISTANCE = 'DISTANCE'
    TIME_WINDOW = 'TIME_WINDOW'
    ORDERS_COUNT = 'ORDERS_COUNT'
    PLAN_ORDERS_COUNT = 'PLAN_ORDERS_COUNT'
    WAITLIST_ORDERS_COUNT = 'WAITLIST_ORDERS_COUNT'
    STOPS_COUNT = 'STOPS_COUNT'
    LOCATIONS_COUNT = 'LOCATIONS_COUNT'
    CARGO_CAPACITY_RATIO_MASS = 'CARGO_CAPACITY_RATIO_MASS'
    CARGO_CAPACITY_RATIO_VOLUME = 'CARGO_CAPACITY_RATIO_VOLUME'
    CARGO_CAPACITY_RATIO_CAPACITY_A = 'CARGO_CAPACITY_RATIO_CAPACITY_A'
    CARGO_CAPACITY_RATIO_CAPACITY_B = 'CARGO_CAPACITY_RATIO_CAPACITY_B'
    CARGO_CAPACITY_RATIO_CAPACITY_C = 'CARGO_CAPACITY_RATIO_CAPACITY_C'
    MAX_TRANSPORT_LOAD_MASS = 'MAX_TRANSPORT_LOAD_MASS'
    MAX_TRANSPORT_LOAD_VOLUME = 'MAX_TRANSPORT_LOAD_VOLUME'
    MAX_TRANSPORT_LOAD_CAPACITY_A = 'MAX_TRANSPORT_LOAD_CAPACITY_A'
    MAX_TRANSPORT_LOAD_CAPACITY_B = 'MAX_TRANSPORT_LOAD_CAPACITY_B'
    MAX_TRANSPORT_LOAD_CAPACITY_C = 'MAX_TRANSPORT_LOAD_CAPACITY_C'

