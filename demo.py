import sys
sys.dont_write_bytecode = True

import duelcraftpy

game = duelcraftpy.Game([
    duelcraftpy.Player("Test1", 20, 3, duelcraftpy.Skill("Skill1", duelcraftpy.SkillType.Incapacitated, duelcraftpy.SkillTarget.Other, 2, 3)),
    duelcraftpy.Player("Test2", 20, 3, duelcraftpy.Skill("Skill1", duelcraftpy.SkillType.Health, duelcraftpy.SkillTarget.Self, 5, 2)),
    duelcraftpy.Player("Test3", 20, 3, duelcraftpy.Skill("Skill1", duelcraftpy.SkillType.Health, duelcraftpy.SkillTarget.Other, -5, 2))
])

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

@game.onTurn
def onTurn(turn):
    try:
        while True:
            user_input = input("You are " + str(turn.player) + ". | 1: Attack, 2: Skill, 3: Guard, 4: Pass > ")
            if user_input == "1":
                turn.attack()
                break
            elif user_input == "2":
                try:
                    turn.skill()
                except duelcraftpy.Exception.SkillCooldownException:
                    print("Skill is cooling down")
                break
            elif user_input == "3":
                turn.guard()
                break
            elif user_input == "4":
                turn.passTurn()
                break
        print(game.state())
    except KeyboardInterrupt:
        print()
        import sys
        sys.exit()

game.start()
