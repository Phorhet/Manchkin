import random

class NPC(Player):  
    def __init__(self, name, x, y):
        super().__init__(name, x, y)
        self.strategy = random.choice(["Aggressive", "Defensive", "Cooperative"])

    def choose_card(self):
        """Выбор карты """
        best_card = None
        max_bonus = -float('inf')

        for card in self.hand:
            if card.card_type == "Treasure" and card.bonus > max_bonus:
                best_card = card
                max_bonus = card.bonus

        if best_card:
            print(f"{self.name} Экипирует {best_card.name} (+{best_card.bonus}).")
            self.equipped_items.append(best_card)
            self.hand.remove(best_card)

    def attack_monster(self, monster):
        """ Оценка стоит ли атаковать монстра смотря на его статы"""
        total_power = self.level + sum(card.bonus for card in self.equipped_items)
        success_chance = total_power / (monster.power + 1)  #Расчет вероятности успеха

        if success_chance > 0.5:  # атака если вероятность успеха больше 5
            print(f"{self.name} attacks {monster.name} with power {total_power}.")
            if random.random() < success_chance:  # Бросок кубика для смывки
                self.level += 1
                print(f"{self.name} победил {monster.name} и подянл свой уровень {self.level}!")
            else:
                print(f"{self.name} не вывез файт с монстром {monster.name}!")
        else:
            print(f"{self.name} решил убежать как волк позорный от {monster.name}.")

    def interact_with_players(self, other_players):
        """Взаимодействие с игроками"""
        if self.strategy == "Cooperative":
            for player in other_players:
                if player.level < self.level:  # помощь слабым игрокам
                    print(f"{self.name} помогает{player.name} дав ему предмет")
                    if self.equipped_items:
                        gift = self.equipped_items.pop(0)
                        player.equipped_items.append(gift)
                        print(f"{self.name} дал {gift.name} для {player.name}.")
        elif self.strategy == "Aggressive":
            for player in other_players:
                if player.level > self.level:  # Саботировать более сильных игроков
                    print(f"{self.name} саботирует {player.name} !")
                    if player.equipped_items:
                        stolen_item = player.equipped_items.pop(0)
                        self.equipped_items.append(stolen_item)
                        print(f"{self.name} свистнул {stolen_item.name} у {player.name}!")

    def sell_cards(self):
        """Продажа карт"""
        while len(self.hand) > 5:
            discarded_card = self.hand.pop(0)
            self.gold += discarded_card.gold_value if hasattr(discarded_card, 'gold_value') else 0
            print(f"{self.name} продал {discarded_card.name} получил {discarded_card.gold_value} золота.")

    def take_turn(self, door_deck, treasure_deck, other_players):
        """Ход NPC"""
        print(f"\n{self.name}'s turn! Strategy: {self.strategy}")

        # Выбивание двери
        if random.random() < 0.7:  # 70% chance to kick down the door
            if door_deck:
                card = door_deck.pop(0)
                print(f"{self.name} drew a {card.name}")
                self.hand.append(card)
        else:
            print(f"{self.name} ищет приключения на свою...")

        # выбор и снаряжение карт
        self.choose_card()

        # Использовать монстра если таково возможно
        for card in self.hand:
            if card.card_type == "Monster":
                self.attack_monster(card)
                self.hand.remove(card)
                break

        # взаимодействие с щдругими игроками
        self.interact_with_players(other_players)

        # Продажа карт
        self.sell_cards()

        # шутейка
        self.make_joke()

    def make_joke(self):
        """Комментарий по ходу игры"""
        jokes = [
            "I'm not saying I'm better than you... but I am.",
            "Looks like someone forgot their lucky dice today!",
            "Leveling up is my cardio.",
            "Why fight fair when you can fight dirty?",
            "Who needs friends when you have swords?"
        ]
        print(f"{self.name}: {random.choice(jokes)}")
