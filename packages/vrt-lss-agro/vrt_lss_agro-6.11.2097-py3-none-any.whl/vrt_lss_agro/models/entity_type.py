# coding: utf-8

"""
    VRt.Agro [AG]

    The version of the OpenAPI document: 6.11.2097

    Generated by OpenAPI Generator: 6.6.0

    Do not edit the code manually

    2023 Veeroute
"""


from inspect import getfullargspec
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class EntityType(str, Enum):
    """
    Entity type.
    """

    """
    allowed enum values
    """
    TASK = 'TASK'
    SETTINGS = 'SETTINGS'
    CROP = 'CROP'
    FIELD = 'FIELD'
    ELEVATOR = 'ELEVATOR'
    FACTORY = 'FACTORY'
    MARKET = 'MARKET'
    STORAGE = 'STORAGE'
    SILO = 'SILO'
    BUNKER = 'BUNKER'
    DRYER = 'DRYER'
    GATE = 'GATE'
    CONSUMER = 'CONSUMER'
    LEFTOVER = 'LEFTOVER'
    FORECAST_ELEMENT = 'FORECAST_ELEMENT'

