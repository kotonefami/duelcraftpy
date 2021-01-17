from . import SkillType
from .Exception import *
class Skill:
    def __init__(self, name:str, type:int, target:int, amount:int, cooldown:int):
        self.name = name
        self.type = type
        self.target = target
        self.amount = amount
        self.cooldown = cooldown
        if self.type == SkillType.Incapacitated and self.amount < 1:
            raise InvalidSkillAmountException("If the type is set to incapacitated, you cannot specify amount as a negative number.")

    def __str__(self):
        return self.name
