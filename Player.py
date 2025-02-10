class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 10
        self.hand = []  # Карты на руке
        self.equipped_items = {}  # Снаряжение (оружие, броня и т.п.)
        self.class_race = None  # Класс и раса персонажа
        self.status_effects = set()  # Эффекты, наложенные на игрока (например, проклятия)
        self.falllevel = False  # Признак потери уровня игроком

    def draw_card(self, deck):
        """Достает карту из колоды."""
        if len(deck) > 0:
            self.hand.append(deck.pop())

    def play_card(self, index):
        """Игрок играет карту из руки."""
        return self.hand.pop(index)

    def level_up(self):
        """Повышает уровень игрока."""
        self.level += 1

    def take_damage(self, damage):
        """Наносит игроку урон."""
        self.health -= damage
        if self.health <= 0:
            self.backup()

    def backup(self):
        """Обработка потери уровня игроком."""
        self.falllevel = True
        print(f"{self.name} потеря уровня!")


    def equip_item(self, item):
        """Оборудование предмета."""
        if item.item_type not in self.equipped_items:
            self.equipped_items[item.item_type] = item
        else:
            old_item = self.equipped_items[item.item_type]
            self.hand.append(old_item)
            self.equipped_items[item.item_type] = item

    def unequip_item(self, item_type):
        """Снятие предмета."""
        if item_type in self.equipped_items:
            item = self.equipped_items.pop(item_type)
            self.hand.append(item)

    def add_status_effect(self, effect):
        """Добавление эффекта на игрока."""
        self.status_effects.add(effect)

    def remove_status_effect(self, effect):
        """Удаление эффекта с игрока."""
        if effect in self.status_effects:
            self.status_effects.remove(effect)

    def get_total_attack_bonus(self):
        """Расчет общего бонуса атаки."""
        total_bonus = sum([item.attack_bonus for item in self.equipped_items.values()])
        return total_bonus

    def get_total_defense_bonus(self):
        """Расчет общего бонуса защиты."""
        total_bonus = sum([item.defense_bonus for item in self.equipped_items.values()])
        return total_bonus

    def has_class_or_race(self, class_or_race):
        """Проверка наличия определенного класса или расы."""
        return self.class_race is not None and class_or_race in self.class_race

    def reset_hand(self):
        """Сбрасывает руку игрока (используется при конце хода)."""
        self.hand.clear()

    def to_string(self):
        """Отображение информации об игроке."""
        equipped_items_str = ', '.join([f'{k}: {v}' for k, v in self.equipped_items.items()])
        status_effects_str = ', '.join(self.status_effects)
        return f'Имя: {self.name}\n' \
               f'Уровень: {self.level}\n' \
               f'Рука: {len(self.hand)} карт\n' \
               f'Экипировка: {equipped_items_str}\n' \
               f'Эффекты: {status_effects_str}'
               f'Уровень: {self.level}\n' \
               f'Здоровье: {self.health}\n' \
               f'Рука: {len(self.hand)} карт\n' \
               f'Экипировка: {equipped_items_str}\n' \
               f'Эффекты: {status_effects_str}'
""" Примерный код игрока который должен присутствовать в финальной версии.
import sqlite3
import random

class Card:
    def __init__(self, name, card_type, effect=None, attack_bonus=0, defense_bonus=0):
        """
        Инициализация карты с именем, типом и необязательными эффектами или бонусами.
        """
        self.name = name
        self.card_type = card_type  # "Treasure", "Door", "Class", "Race", etc.
        self.effect = effect  # Функция или описание эффекта карты
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus

    def __repr__(self):
        return self.name


class Monster:
    def __init__(self, name, power, reward_level, reward_item=None):
        """
        Инициализация монстра с именем, силой и наградами за его победу.
        """
        self.name = name
        self.power = power
        self.reward_level = reward_level
        self.reward_item = reward_item

    def __repr__(self):
        return f"{self.name} (Power: {self.power})"


class Player:
    def __init__(self, name, db_path='cards.db'):
        """
        Инициализация игрока с именем, уровнем, здоровьем и другими атрибутами.
        Также, подключение к базе данных SQLite3 для управления картами.
        """
        self.name = name
        self.level = 1
        self.health = 10
        self.hand = []  # Карты в руке
        self.equipped_items = {}  # Снаряженные предметы (оружие, броня и т.д.)
        self.class_race = None  # Класс и раса персонажа
        self.status_effects = set()  # Эффекты статуса (например, проклятия)
        self.falllevel = False  # Указывает, потерял ли игрок уровень

        # Подключение к базе данных SQLite3
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

        # Создание таблицы для карт, если она не существует
        self.cursor.execute("""
//////////////
            )
        """)
        self.conn.commit()

    def draw_card(self, deck):
        """
        Взятие карты из колоды и добавление ее в руку игрока.
        Также, обновление базы данных для отражения новой карты в руке игрока.
        """
        if len(deck) > 0:
            card = deck.pop()
            self.hand.append(card)
            self.cursor.execute()////
            self.conn.commit()
            print(f"{self.name} взял карту: {card.name}")

    def play_card(self, index):
        """
        Игра карты из руки игрока.
        Удаление карты из руки и обновление базы данных.
        """
        if 0 <= index < len(self.hand):
            card = self.hand.pop(index)
            self.cursor.execute(////_)
            self.conn.commit()
            print(f"{self.name} сыграл карту: {card.name}")
            return card
        else:
            print(f"Неверный индекс карты: {index}")
            return None

    def level_up(self):
        """Увеличение уровня игрока."""
        self.level += 1
        print(f"{self.name} повысил уровень до {self.level}!")

    def take_damage(self, damage):
        """Нанесение урона игроку."""
        self.health -= damage
        if self.health <= 0:
            self.backup()
            print(f"{self.name} был побежден!")

    def backup(self):
        """Обработка потери уровня."""
        self.falllevel = True
        self.level -= 1
        print(f"{self.name} потерял уровень! Текущий уровень: {self.level}")

    def equip_item(self, item):
        """
        Надевание предмета. Если предмет такого же типа уже надет,
        заменить его и переместить старый предмет обратно в руку.
        """
        if item.card_type not in self.equipped_items:
            self.equipped_items[item.card_type] = item
            print(f"{self.name} надел {item.name}.")
        else:
            old_item = self.equipped_items[item.card_type]
            self.hand.append(old_item)
            self.equipped_items[item.card_type] = item
            print(f"{self.name} заменил {old_item.name} на {item.name}.")

    def unequip_item(self, item_type):
        """Снятие предмета и перемещение его обратно в руку."""
        if item_type in self.equipped_items:
            item = self.equipped_items.pop(item_type)
            self.hand.append(item)
            print(f"{self.name} снял {item.name}.")

    def get_total_attack_bonus(self):
        """Расчет общего бонуса атаки от снаряженных предметов."""
        total_bonus = sum([item.attack_bonus for item in self.equipped_items.values()])
        return total_bonus

    def get_total_defense_bonus(self):
        """Расчет общего бонуса защиты от снаряженных предметов."""
        total_bonus = sum([item.defense_bonus for item in self.equipped_items.values()])
        return total_bonus

    def fight_monster(self, monster):
        """
        Бой с монстром. Игрок может выбрать, сражаться, просить о помощи или убежать.
        """
        total_power = self.level + self.get_total_attack_bonus()
        print(f"{self.name} встречает {monster.name} (Power: {monster.power})")
        print(f"Общая сила {self.name}: {total_power}")

        choice = input("Хотите [F]ight, [A]sk for help, or [R]un away? ").lower()
        if choice == 'f':
            success_chance = total_power / (monster.power + 1)
            if random.random() < success_chance:
                print(f"{self.name} победил {monster.name}!")
                self.level_up()
                if monster.reward_item:
                    self.hand.append(monster.reward_item)
                    print(f"{self.name} получил {monster.reward_item.name} в качестве награды!")
            else:
                print(f"{self.name} не смог победить {monster.name}!")
                self.take_damage(1)
        elif choice == 'a':
            print("Запрос помощи не реализован еще.")
        elif choice == 'r':
            print(f"{self.name} убежал от {monster.name}.")
        else:
            print("Неверный выбор. Вы колеблетесь и теряете возможность действовать.")

    def reset_hand(self):
        """Сброс руки игрока (используется в конце хода)."""
        self.hand.clear()
        self.cursor.execute(///)
        self.conn.commit()
        print(f"{self.name} очистил свою руку.")

    def to_string(self):
        """Отображение информации о игроке."""
        equipped_items_str = ', '.join([f'{k}: {v.name}' for k, v in self.equipped_items.items()])
        status_effects_str = ', '.join(self.status_effects)
        return f'Имя: {self.name}\n' \
               f'Уровень: {self.level}\n' \
               f'Здоровье: {self.health}\n' \
               f'Рука: {len(self.hand)} карт\n' \
               f'Снаряженные предметы: {equipped_items_str}\n' \
               f'Эффекты статуса: {status_effects_str}'

    def close_db_connection(self):
        """Закрытие подключения к базе данных SQLite3."""
        self.conn.close()
        print(f"Подключение к базе данных для {self.name} закрыто.")"""
