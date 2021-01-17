# -*- coding: utf-8 -*-

# duelcraftpy 1.0.0

__title__ = 'duelcraftpy'
__author__ = 'Fami'
__license__ = 'MIT'
__copyright__ = '(C) Fami 2021'
__version__ = '1.0.0'

from .Player import Player
from .Skill import Skill
from .Game import Game
from . import SkillType
from . import SkillTarget

__all__ = ["Player", "Skill", "Game", "SkillType", "SkillTarget"]
