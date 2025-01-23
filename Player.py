class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 10
        self.hand = []  # Карты на руке
        self.equipped_items = {}  # Снаряжение (оружие, броня и т.п.)
        self.class_race = None  # Класс и раса персонажа
        self.status_effects = set()  # Эффекты, наложенные на игрока (например, проклятия)
        self.falllevel = False  # Признак отката по уровню игрока

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
        """Обработка смерти игрока."""
        self.falllevel = True
        print(f"{self.name} умер!")

    def heal(self, healing):
        """Восстанавливает здоровье игрока."""
        self.health += healing
        if self.health > 10:
            self.health = 10

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
               f'Здоровье: {self.health}\n' \
               f'Рука: {len(self.hand)} карт\n' \
               f'Экипировка: {equipped_items_str}\n' \
               f'Эффекты: {status_effects_str}'