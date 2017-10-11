# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create yours class here.
from enum import Enum, unique

@unique
class EnumStatus(Enum):
    Active = 1
    Inactive = 2
    Delete = 3

    def __int__(self):
        return int(self.value)

    def __str__(self):
        return str(self.name)

@unique
class EnumType(Enum):
    CardPopup = 1
    InvitationCard = 2

    def __int__(self):
        return int(self.value)

    def __str__(self):
        return str(self.name)

@unique
class EnumCategory(Enum):
    Married = 1
    Decoration = 2
    Party = 3
    Game = 4
    Others = 10

    def __int__(self):
        return int(self.value)

    def __str__(self):
        return str(self.name)