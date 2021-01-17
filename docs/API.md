# API Reference

## Events

```
@game.onDiedPlayer
def onDiedPlayer(player):
    print(str(player) + " is died.")

@game.onWonPlayer
def onWonPlayer(player):
    print(str(player) + " is won!")

@game.onAttackPlayer
def onAttackPlayer(player):
    print(str(player) + "'s attack!")

@game.onUseSkill
def onUseSkill(player, skill):
    print(str(player) + " used skill!")

@game.onGuard
def onGuard(player):
    print(str(player) + " is guarding!")

@game.onPassTurn
def onPassTurn(player):
    print(str(player) + " passed turn!")

@game.onIncapacitated
def onIncapacitated(player):
    print(str(player) + " is incapacitated!")
```

## Game Class

<a id="duelcraftpy-game"></a>
### class duelcraftpy.Game(players)

#### Parameters
* players(List[[Player](#duelcraftpy-player)]) - Joining players.

#### Supported Operations
##### len(duelcraftpy.Game)
Return a turn count of the game.

#### players
The players in the game.
##### Type
List[[Player](#duelcraftpy-player)]

#### turn
Return a turn count of the game.
##### Type
int

#### onDiedPlayer
If died a player, fire this event.
##### Type
Function

## Player Class

<a id="duelcraftpy-player"></a>
### class duelcraftpy.Player(name, health, strength, skill)

#### Parameters
* name(str) - Player's name.
* health(float) - Player's health.
* strength(int) - Player's strength.
* skill([Skill](#duelcraftpy-skill)) - Player's skill.

#### Supported Operations
##### str(duelcraftpy.Player)
Return the Player's name.

#### name
The name of player.
##### Type
str

#### health
The health of player.
##### Type
float

#### strength
The strength of player.
##### Type
int

#### skill
The skill of player.
##### Type
[Skill](#duelcraftpy-skill)

#### isGuarding
Is the player guarding
##### Type
int

#### isSkillCooldown
Player's skill cooldown timing
##### Type
int

#### isIncapacitated
Player's incapacitated time
##### Type
int

#### isDied
Is the player died
##### Type
bool

## Turn Class

<a id="duelcraftpy-turn"></a>
### class duelcraftpy.Turn(game, player, players, count)

#### Parameters
* game([Game](#duelcraftpy-game)) - Game of Turn.
* player([Player](#duelcraftpy-player)) - Player in Turn.
* players(list[[Player](#duelcraftpy-player)]) - Players in Turn.
* count(int) - Turn's count.

#### Supported Operations
##### len(duelcraftpy.Player)
Return the Turn's count.

#### player
The player of turn.
##### Type
[Player](#duelcraftpy-player)

#### game
The game of turn.
##### Type
[Game](#duelcraftpy-game)

#### count
The count of turn.
##### Type
int

## Skill Class

<a id="duelcraftpy-skill"></a>
### class duelcraftpy.Skill(name, type, amount)

#### Parameters
* name(str) - Skill's name.
* type([SkillType](#duelcraftpy-skilltype)) - Skill's type.
* target([SkillTarget](#duelcraftpy-skilltarget)) - Skill's type.
* amount(int) - Skill's amount.

#### name
The name of skill.
##### Type
str

#### type
The type of skill.
##### Type
[SkillType](#duelcraftpy-skilltype)

#### target
The type of target.
##### Type
[SkillTarget](#duelcraftpy-skilltarget)

#### amuont
The amount of skill.
##### Type
int

#### cooldown
The cooldown of skill.
##### Type
int

## SkillType

<a id="duelcraftpy-skilltype"></a>
### duelcraftpy.SkillType

#### health
Health
##### Value
0

## SkillTarget

<a id="duelcraftpy-skilltarget"></a>
### duelcraftpy.SkillTarget

#### Self
Self
##### Value
0

#### Other
Other
##### Value
1
