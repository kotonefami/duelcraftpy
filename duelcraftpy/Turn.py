from .Player import Player
from .Exception import *
from . import SkillType
from . import SkillTarget
class Turn:
    def __init__(self, game, player:Player, players:list[Player], count:int):
        self.player = player
        self._players = players
        self.count = count
        self.game = game

    def __len__(self):
        return self.count

    def attack(self):
        if not self.game.isGameEnded:
            for _player in self._players:
                if _player != self.player:
                    if _player.isGuarding > 0:
                        _player.health -= self.player.strength / 2
                    else:
                        _player.health -= self.player.strength
                if _player.health <= 0:
                    _player.health = 0
            for onAttackPlayer in self.game._onAttackPlayer:
                onAttackPlayer(self.player)
        else:
            raise GameEndedException("This game is already ended")

    def skill(self):
        if not self.game.isGameEnded:
            if self.player.isSkillCooldown == 0:
                if self.player.skill.target == SkillTarget.Self:
                    if self.player.skill.type == SkillType.Health:
                        self.player.health += self.player.skill.amount
                    elif self.player.skill.type == SkillType.Incapacitated:
                        self.player.isIncapacitated += self.player.skill.amount
                    if self.player.health <= 0:
                        self.player.health = 0
                elif self.player.skill.target == SkillTarget.Other:
                    for _player in self._players:
                        if _player != self.player:
                            if self.player.skill.type == SkillType.Health:
                                _player.health += self.player.skill.amount
                            elif self.player.skill.type == SkillType.Incapacitated:
                                _player.isIncapacitated += self.player.skill.amount
                        if _player.health <= 0:
                            _player.health = 0
                self.player.isSkillCooldown += self.player.skill.cooldown
                for onUseSkill in self.game._onUseSkill:
                    onUseSkill(self.player, self.player.skill)
            else:
                raise SkillCooldownException("Skill is cooling down")
        else:
            raise GameEndedException("This game is already ended")

    def guard(self):
        if not self.game.isGameEnded:
            self.player.isGuarding += 1
            for onGuard in self.game._onGuard:
                onGuard(self.player)
        else:
            raise GameEndedException("This game is already ended")

    def passTurn(self):
        if not self.game.isGameEnded:
            for onPassTurn in self.game._onPassTurn:
                onPassTurn(self.player)
        else:
            raise GameEndedException("This game is already ended")
