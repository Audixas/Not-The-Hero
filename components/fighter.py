class Fighter:
    def __init__(self, hp, defense, power):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self. power = power

    def take_damage(self, amount):
        results = []

        self.hp -= amount

        if self.hp <= 0:
            results.append({'dead': self.owner})

        return results

    def attack(self, target):
        results = []

        if target.harmless:
            damage = self.power - target.harmless.defense
        elif target.fighter:
            damage = self.power - target.fighter.defense

        if damage >= 0:
            results.append({'message': '{0} attacks {1} for {2} hit points.'.format(
                self.owner.name.capitalize(), target.name, str(damage))})
            if target.harmless:
                results.extend(target.harmless.take_damage(damage))
            elif target.fighter:
                results.extend(target.fighter.take_damage(damage))
        else:
            results.append({'message': '{0} attacks {1} but does no damage.'.format(
                self.owner.name.capitalize(), target.name)})

        return results