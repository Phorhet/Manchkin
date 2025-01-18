"ПРИМЕРНЫЙ СКИЛЕТ"
import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Card Game")


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

dungeon_bg = pygame.image.load("dungeon_background.png")
table_image = pygame.image.load("table.png")
deck_image = pygame.image.load("deck.png")
paper_image = pygame.image.load("paper.png")
hand_image = pygame.image.load("hand.png")


def draw_table():
    screen.blit(table_image, (WIDTH//2 - table_image.get_width()//2, HEIGHT//2 - table_image.get_height()//2))
    screen.blit(deck_image, (WIDTH//2 - 200, HEIGHT//2))
    screen.blit(deck_image, (WIDTH//2 + 50, HEIGHT//2))
    screen.blit(paper_image, (WIDTH//2 - 50, HEIGHT//2 - 50))
    screen.blit(paper_image, (WIDTH//2 + 200, HEIGHT//2 + 50))
    screen.blit(hand_image, (WIDTH//2 - 50, HEIGHT//2 + 100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(dungeon_bg, (0, 0))
    draw_table()

    pygame.display.flip()



"""
Не используемая часть!!!!!!!!!!!
import pygame
import sys



pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Munchkin")
clock = pygame.time.Clock()

background_image = pygame.image.load('assets/background.png').convert()


deck_door = [
    DoorCard('assets/cards/door/monster1.jpg', 1, ['+1 к уровню']),
    DoorCard('assets/cards/door/monster2.jpg', 2, ['+2 к здоровью'])
]
random.shuffle(deck_door)

deck_treasure = [
    TreasureCard('assets/cards/treasure/bonus1.jpg', '+1 к уровню'),
    TreasureCard('assets/cards/treasure/bonus2.jpg', '+2 к здоровью')
]
random.shuffle(deck_treasure)


players = [Player("Игрок 1"), Player("Игрок 2")]
current_player_index = 0
current_player = players[current_player_index]

def next_turn():
    global current_player_index, current_player
    current_player_index = (current_player_index + 1) % len(players)
    current_player = players[current_player_index]

def draw_cards(player, deck, number=1):
    for _ in range(number):
        player.draw_card(deck)

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                next_turn()

def update():
    screen.blit(background_image, (0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render(f"Текущий игрок: {current_player.name}", True, (255, 255, 255))
    screen.blit(text, (20, 20))
    pygame.display.flip()

while True:
    handle_events()
    update()
    clock.tick(60)"""