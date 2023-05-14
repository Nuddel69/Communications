import pygame
from example_network import GameNetwork

WIDTH = 500
HEIGHT= 500

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")

CLIENTNUMBER = 0


class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def redrawWindow(win,players: list[Player]):
    win.fill((255,255,255))

    for player in players:
        player.draw(win)

    pygame.display.update()

def parse_pos(string: str) -> tuple[int, int]:
    pos = string.split(",")
    return int(pos[0]), int(pos[1])

def stringify_pos(pos:  tuple[int, int]) -> str:
    return f"{pos[0]},{pos[1]}"


def main() -> None:
    run = True
    n = GameNetwork("127.0.0.1", 5555)
    startPos = parse_pos(n.getPos())

    p = Player(startPos[0],startPos[1],100,100,(0,255,0))
    p2 = Player(0,0,100,100,(0,255,0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        p2_pos = parse_pos(n.send(stringify_pos((p.x, p.y))))
        p2.x, p2.y = p2_pos
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                n.send(stringify_pos((p.x, p.y)))
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, [p, p2])

if __name__ == "__main__":
    main()
