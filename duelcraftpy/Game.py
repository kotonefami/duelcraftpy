from .Skill import Skill
from .Player import Player
from .Turn import Turn
from .Exception import *

class Game:
    def __init__(self, players:list[Player]):
        if len(players) < 2:
            raise NotEnoughPlayersException("Not enough players")
        self.players = players
        self.turn = -1
        self._turnObj = None

        self._onDiedPlayer = []
        self._onWonPlayer = []
        self._onTurn = None
        self._onAttackPlayer = []
        self._onUseSkill = []
        self._onGuard = []
        self._onPassTurn = []
        self._onIncapacitated = []

        self.isGameEnded = False

    def __len__(self):
        return self.turn

    def nextTurn(self):
        if not self.isGameEnded:
            self.turn += 1
            if self.turn >= len(self.players):
                self.turn = 0
            if self.players[self.turn].isIncapacitated > 0:
                self.players[self.turn].isIncapacitated -= 1
                for onIncapacitated in self._onIncapacitated:
                    onIncapacitated(self.players[self.turn])
                if not self.isGameEnded:
                    self.nextTurn()
                else:
                    raise GameEndedException("This game is already ended")
            else:
                for _player in self.players:
                    if self.turn == 0:
                        if _player.isGuarding > 0: _player.isGuarding -= 1
                        if _player.isSkillCooldown > 0: _player.isSkillCooldown -= 1
                    if _player.health <= 0 and _player.isDied == False:
                        _player.health = 0
                        for onDiedPlayer in self._onDiedPlayer:
                            onDiedPlayer(_player)
                        _player.isDied = True

                        _live_player_count = 0
                        _last_live_player = None
                        for _counting_player in self.players:
                            if not _counting_player.isDied:
                                _live_player_count += 1
                                _last_live_player = _counting_player
                        if _live_player_count == 1:
                            self.isGameEnded = True
                            for onWonPlayer in self._onWonPlayer:
                                onWonPlayer(_last_live_player)
                                break
                if not self.isGameEnded:
                    if self.players[self.turn].health > 0 and not self.players[self.turn].isDied:
                        self._onTurn(Turn(self, self.players[self.turn], self.players, self.turn))
                    self.nextTurn()
        else:
            raise GameEndedException("This game is already ended")

    def onDiedPlayer(self, func):
        self._onDiedPlayer.append(func)
        return func

    def onWonPlayer(self, func):
        self._onWonPlayer.append(func)
        return func

    def onTurn(self, func):
        if self._onTurn == None:
            self._onTurn = func
        else:
            raise InvalidEventException("Already onTurn event has been set")
        return func

    def onAttackPlayer(self, func):
        self._onAttackPlayer.append(func)
        return func

    def onUseSkill(self, func):
        self._onUseSkill.append(func)
        return func

    def onGuard(self, func):
        self._onGuard.append(func)
        return func

    def onPassTurn(self, func):
        self._onPassTurn.append(func)
        return func

    def onIncapacitated(self, func):
        self._onIncapacitated.append(func)
        return func

    def state(self):
        _result = ""
        for _player in self.players:
            _isGuarding = "-"
            if _player.isGuarding > 0: _isGuarding = str(_player.isGuarding)
            _isIncapacitated = "-"
            if _player.isIncapacitated > 0: _isIncapacitated = str(_player.isIncapacitated)
            _result += str(_player) + " | " + str(_player.health) + " HP | Guard " + str(_isGuarding) + " | Incapacitated " + str(_isIncapacitated)
            if _player != self.players[len(self.players)-1]: _result += "\n"
        return _result

    def start(self):
        if self._onTurn == None:
            raise InvalidEventException("No onTurn event has been set")
        self.nextTurn()
