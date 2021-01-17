from .Skill import Skill
class Player:
    def __init__(self, name:str, health:float, strength:int, skill:Skill):
        self.name = name
        self.health = float(health)
        self.strength = strength
        self.skill = skill
        self.isGuarding = 0
        self.isSkillCooldown = 0
        self.isIncapacitated = 0
        self.isDied = False

    def __str__(self):
        return self.name
