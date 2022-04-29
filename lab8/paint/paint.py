import pygame

pygame.init()

# класс для  инструментов


class tools(pygame.sprite.Sprite):
    def __init__(self, pic, position):
        super().__init__()
        self.pic = pygame.image.load(f'{pic}')  # берет картинку из директория
        self.pic = pygame.transform.scale(
            self.pic, (40, 40))  # изменяет ее размер на 30х30
        # центром становится данная нам координата
        self.rect = self.pic.get_rect(center=position)

    def draw(self):
        # вставляет рисунок в нужные нам координаты
        screen.blit(self.pic, self.rect)

# для рисования


def drawing_line(start_pos, end_pos, shirina, current_color):
    pygame.draw.line(screen, current_color, start_pos, end_pos, shirina)


def calculateRect(x1, y1, x2, y2):
    r = pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))
    pygame.draw.rect(screen, current_color, pygame.Rect(r), shirina)


def calculatedCircle(x1, y1, x2, y2):
    r = max(abs(x2 - x1), abs(y2 - y1))
    pygame.draw.circle(screen, current_color, (x1, y1), r, shirina)


# функция для изменение ширины линий
def the_size(i):
    global shirina
    if i.key == pygame.K_1:
        shirina = 1
    if i.key == pygame.K_2:
        shirina = 5
    if i.key == pygame.K_3:
        shirina = 10
    if i.key == pygame.K_4:
        shirina = 15
    if i.key == pygame.K_5:
        shirina = 20
    if i.key == pygame.K_0:
        shirina = 0


def figure_tools_setting():
    global figure_mode
    figure_mode = True
    for i in state:
        state[i] = False


# нужные переменные
WHITE = (255, 255, 255)
WIDTH = 900
HEIGHT = 700
shirina = 1


# создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
baseLayer = pygame.Surface((WIDTH, HEIGHT))
pygame.display.set_caption('Paint')
screen.fill(WHITE)
baseLayer.fill(WHITE)

clock = pygame.time.Clock()

color_pallete = pygame.image.load("color.jpg")
current_color = (0, 0, 0)

# список и спрайт группа для интсрументов для рисования
items = [['eraser.jpg', (395, 30)], ['pen.jpg', (440, 30)], [
    'rect.jpg', (485, 30)], ['circle.jpg', (530, 30)]]
Tools = pygame.sprite.Group()
for i in items:
    temp = tools(i[0], i[1])  # добавляем в группу через функцию
    Tools.add(temp)

state = {"eraser": False, "circle": False, 'rect': False}

startX = endX = 0
startY = endY = 0

draw_mode = False
figure_mode = False
pen = True

finished = False

while not finished:

    # вставляем цветовой круг и инструменты
    screen.blit(color_pallete, (0, 0))
    for tool in Tools:
        tool.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        if event.type == pygame.KEYDOWN:  # если зажата какая либо клавиша
            if event.key == pygame.K_c:  # если равна с то ресерт страницы
                screen.fill(WHITE)
            # а также мониторит нажата ли кнопка для изменения ширины
            the_size(event)

        if event.type == pygame.MOUSEBUTTONDOWN:  # проверка на зажатость кнопки мышки
            draw_mode = True
            pos = pygame.mouse.get_pos()  # берем начальную позицию
            if draw_mode:
                startX = pos[0]
                startY = pos[1]

            if startX > 0 and startX < color_pallete.get_width() and startY > 0 and startY < color_pallete.get_height():
                # получает цвет с пикселя на который нажали
                current_color = color_pallete.get_at(pos)

        if event.type == pygame.MOUSEMOTION:  # если мышка двигается
            pos2 = pygame.mouse.get_pos()
            endX = pos2[0]
            endY = pos2[1]

        if event.type == pygame.MOUSEBUTTONUP:
            draw_mode = False
            baseLayer.blit(screen, (0, 0))
    k = 0
    for tool in Tools:
        point = pygame.mouse.get_pos()
        # the tool is picked only if it's clicked in it's area
        if tool.rect.collidepoint(point) and pygame.MOUSEBUTTONDOWN:
            if 'eraser' in items[k][0]:
                figure_mode = pen = False  # the eraser can't have figure form
                current_color = (255, 255, 255)
            elif 'pen' in items[k][0]:
                figure_mode, pen = False, True
                current_color = (0, 0, 0)
            elif 'rect' in items[k][0]:
                figure_tools_setting()
                state['rect'] = True
            elif 'circle' in items[k][0]:
                figure_tools_setting()
                state['circle'] = True
        k += 1
    if draw_mode and figure_mode:
        if not pen:
            pen = not pen
            current_color = (0, 0, 0)
        screen.blit(baseLayer, (0, 0))
        if state['circle']:
            calculatedCircle(startX, startY, endX, endY)
        if state['rect']:
            calculateRect(startX, startY, endX, endY)

    if not figure_mode:
        if draw_mode:
            if shirina == 0:
                shirina = 25
            pygame.draw.line(screen, current_color,
                             (startX, startY), (endX, endY), shirina)
        startX = endX
        startY = endY

    pygame.display.flip()

    clock.tick(30)


pygame.quit()
