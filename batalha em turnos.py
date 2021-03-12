import pygame
import random

pygame.init()

#variaveis para mudança de turno
turno_p1 = True
turno_p2 = False
turno = 1

# posição do painel
pos_x = 0
pos_y = 400

# posição personagem 1(kenshiro):
x = 100
y = 242

# posição personagem 2(seiya):
a = 450
b = 250

# imagem de fundo usada para simular a fase do jogo
fundo = pygame.image.load('1.png')

# alterando resolução de imagem de fundo para se adequar ao tamanho da janela
fundo = pygame.transform.scale(fundo, (600, 400))

# painel de texto
painel = pygame.image.load('painel.png')

janela = pygame.display.set_mode((600, 400 + 100))
pygame.display.set_caption('Kenshiro vs Seiya')

# criando a fonte de texto
fonte = pygame.font.SysFont('Arial', 20)

# cores para fonte
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


# função para texto
def texto(texto, font, cor, x, y):
    img = font.render(texto, True, cor)
    janela.blit(img, (x, y))

#função para escrever informações do jogo na tela
def escrever_texto():
    #contagem de turnos
    global turno
    global turno_p1
    global turno_p2

    #inserindo painel na tela
    janela.blit(painel, (pos_x, pos_y))

    #informações de vida, energia e outros
    texto(f'{kenshiro.nome} HP: {kenshiro.hp}', fonte, white, pos_x + 10, pos_y + 5)
    texto(f'{seiya.nome} HP: {seiya.hp}', fonte, white, pos_x + 430, pos_y + 5)
    texto(f'ENERGIA: {kenshiro.energia}', fonte, white, pos_x + 10, pos_y + 40)
    texto(f'ENERGIA: {seiya.energia}', fonte, white, pos_x + 430, pos_y + 40)

    #informações de turno
    texto(f'Turno: {turno}', fonte, white, pos_x + 250, pos_y + 5)
    if turno_p1 == True:
        texto(f'Turno de {kenshiro.nome} P1', fonte, white, pos_x + 200, pos_y + 25)
    else:
        texto(f'Turno de {seiya.nome} P2', fonte, white, pos_x + 200, pos_y + 25)

    #informações de comandos kenshiro
    texto(f'atacar = A - energia = 0', fonte, white, pos_x + 10, pos_y - 400)
    texto(f'chutes = W - energia = 40', fonte, white, pos_x + 10, pos_y - 380)
    texto(f'socos = E - energia = 75', fonte, white, pos_x + 10, pos_y - 360)
    texto(f'concentrar = Q - energia = 25', fonte, white, pos_x + 10, pos_y - 340)

    # informações de comandos seiya
    texto(f'atacar = 1 - energia = 0', fonte, white, pos_x + 330, pos_y - 400)
    texto(f'meteoro = 2 - energia = 70', fonte, white, pos_x + 330, pos_y - 380)
    texto(f'cometa = 3 - energia = 50', fonte, white, pos_x + 330, pos_y - 360)
    texto(f'concentrar = 4 - energia = 40', fonte, white, pos_x + 330, pos_y - 340)

#efeitos de batalha
def efeitos_actions():
    global turno
    #efeitos de batalha kenshiro
    if kenshiro.atacar == True:
        rand = random.randint(-10, 15)
        dano = (kenshiro.forca + rand) - int(seiya.defesa_df / 10)
        seiya.hp -= dano

    if kenshiro.concentrar == True:
        kenshiro.defesa_df += 10
        kenshiro.forca += 10
        kenshiro.energia -= 25

    if kenshiro.chutes == True:
        rand = random.randint(-10, 20)
        dano = (kenshiro.forca + rand) - int(seiya.defesa_df / 10)
        seiya.hp -= dano
        kenshiro.energia -= 40


    if kenshiro.sequencia == True:
        rand = random.randint(-10, 50)
        dano = (kenshiro.forca + rand) - int(seiya.defesa_df / 10)
        seiya.hp -= dano
        kenshiro.energia -= 75

    #efeitos de batalha do seiya
    if seiya.soco == True:
        rand = random.randint(-10, 10)
        dano = (seiya.forca + rand) - int(kenshiro.defesa_df / 10)
        kenshiro.hp -= dano

    if seiya.concentrar == True:
        seiya.hp += 30
        seiya.defesa_df += 1
        seiya.forca += 1
        seiya.energia -= 40

    if seiya.meteoro == True:
        rand = random.randint(-10, 30)
        dano = (seiya.forca + rand) - int(kenshiro.defesa_df / 10)
        kenshiro.hp -= dano
        seiya.forca += 10
        seiya.energia -= 70

    if seiya.cometa == True:
        rand = random.randint(-10, 35)
        dano = (seiya.forca + rand) - int(kenshiro.defesa_df / 10)
        kenshiro.hp -= dano
        seiya.forca += 10
        seiya.energia -= 50

    turno += 1

#limite de energia e vida
def limite():
    # testando limite de vida seiya e kenshiro
    if kenshiro.energia <= 0:
        kenshiro.energia = 0
    if kenshiro.energia >= 100:
        kenshiro.energia = 100

    if kenshiro.hp <= 0:
        kenshiro.hp = 0
    if kenshiro.hp >= 200:
        kenshiro.hp = 200

    if seiya.energia <= 0:
        seiya.energia = 0
    if seiya.energia >= 100:
        seiya.energia = 100

    if seiya.hp <= 0:
        seiya.hp = 0
    if seiya.hp >= 200:
        seiya.hp = 200

#bonus final de turno
def bonus():
    global turno_p1
    if turno_p1 == True:
        kenshiro.hp += 10
        kenshiro.energia += 20
        seiya.hp += 10
        seiya.energia += 20

#final de jogo
def final():
    global turno_p1, turno_p2
    if seiya.hp == 0:
        seiya.perdeu = True
        kenshiro.ganhou = True
        turno_p1 = False
        turno_p2 = False

    elif kenshiro.hp == 0:
        kenshiro.perdeu = True
        seiya.ganhou = True
        turno_p1 = False
        turno_p2 = False


# criação de classe do personagem 2(seiya)
class Seiya(pygame.sprite.Sprite):
    def __init__(self, hp_max, forca, defesa_df, nome, energia_max, velocidade):

        self.nome = nome
        self.hp_max = hp_max
        self.hp = hp_max
        self.forca = forca
        self.defesa_df = defesa_df
        self.energia_max = energia_max
        self.energia = energia_max
        self.velocidade = velocidade
        self.vivo = True

        # criação de uma lista para armazenar as sprites do personagem
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        for i in range(4):
            self.sprites.append(pygame.image.load(f'sprites_seiya/stand/stand{i}.png'))
        self.sprites.append(pygame.image.load('sprites_seiya/stand/stand2.png'))
        self.sprites.append(pygame.image.load('sprites_seiya/stand/stand1.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = a, b
        self.parado = False

        self.sprites1 = []
        for i in range(4):
            self.sprites1.append(pygame.image.load(f'sprites_seiya/hit/hit{i}.png'))
        self.golpeado = False

        self.sprites2 = []
        for i in range(5):
            self.sprites2.append(pygame.image.load(f'sprites_seiya/soco/soco{i}.png'))
        self.soco = False

        self.sprites3 = []
        for i in range(12):
            self.sprites3.append(pygame.image.load(f'sprites_seiya/meteoro/{i}.png'))
        self.meteoro = False

        self.sprites4 = []
        for i in range(9):
            self.sprites4.append(pygame.image.load(f'sprites_seiya/cometa/{i}.png'))
        self.cometa = False

        self.sprites5 = []
        for i in range(11):
            self.sprites5.append(pygame.image.load(f'sprites_seiya/buff/{i}.png'))
        self.concentrar = False

        self.sprites6 = []
        for i in range(3):
            self.sprites6.append(pygame.image.load(f'sprites_seiya/defesa/guard{i}.png'))
        self.defesa = False

        self.sprites7 = []
        for i in range(1):
            self.sprites7.append(pygame.image.load(f'sprites_seiya/lose/{i}.png'))
        self.perdeu = False

        self.sprites8 = []
        for i in range(3):
            self.sprites8.append(pygame.image.load(f'sprites_seiya/vencedor/{i}.png'))
        self.ganhou = False

    # funções do personagem(o que ele faz, como por exemplo pular ou bater)
    def defense(self):
        self.defesa = True

    def buff(self):
        self.concentrar = True

    def comet(self):
        self.cometa = True

    def meteor(self):
        self.meteoro = True

    def atack(self):
        self.soco = True

    def stand(self):
        self.parado = True

    def hit(self):
        self.golpeado = True

    def winner(self):
        self.ganhou = True

    def lose(self):
        self.perdeu = True

    # utilização da função update para animar as spritez armazenadas nas listas
    def update(self):
        # animação 1
        if self.parado == True:
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites):
                self.atual = 0
            self.image = self.sprites[int(self.atual)]

        #animação 2
        if self.golpeado == True:
            self.parado = False
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites1):
                self.atual = 0
                self.golpeado = False
                self.parado = True
            self.image = self.sprites1[int(self.atual)]

        #animação 3
        if self.soco == True:
            self.parado = False
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites2):
                self.atual = 0
                self.soco = False
                self.parado = True
            self.image = self.sprites2[int(self.atual)]

        #animação 4
        if self.meteoro == True:
            self.parado = False
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites3):
                self.atual = 0
                self.meteoro = False
                self.parado = True
            self.image = self.sprites3[int(self.atual)]

        #animação 5
        if self.cometa == True:
            self.parado = False
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites4):
                self.atual = 0
                self.cometa = False
                self.parado = True
            self.image = self.sprites4[int(self.atual)]

        # animação 6
        if self.concentrar == True:
            self.parado = False
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites5):
                self.atual = 0
                self.concentrar = False
                self.parado = True
            self.image = self.sprites5[int(self.atual)]

        # animação 7
        if self.defesa == True:
            self.parado = False
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites6):
                self.atual = 0
                self.defesa = False
                self.parado = True
            self.image = self.sprites6[int(self.atual)]

        # animação 8
        if self.perdeu == True:
            self.parado = False
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites7):
                self.atual = 0
                self.perdeu = False
            self.image = self.sprites7[int(self.atual)]

        # animação 9
        if self.ganhou == True:
            self.parado = False
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites8):
                self.atual = 0
                self.ganhou = False
            self.image = self.sprites8[int(self.atual)]



# criando objeto personagem 2(seiya)
all_sprites_seiya = pygame.sprite.Group()
seiya = Seiya(200, 25, 10, 'seiya', 100, 10)
all_sprites_seiya.add(seiya)


# criando a classe do personagem 1(kenshiro)
class Kenshiro(pygame.sprite.Sprite):
    def __init__(self, hp_max, forca, defesa_df, nome, energia_max, velocidade):

        self.nome = nome
        self.hp_max = hp_max
        self.hp = hp_max
        self.forca = forca
        self.defesa_df = defesa_df
        self.energia_max = energia_max
        self.energia = energia_max
        self.velocidade = velocidade
        self.vivo = True
        self.turno = True

        pygame.sprite.Sprite.__init__(self)
        # Sprites do personagem 'kenshiro' parado
        self.sprites = []
        for i in range(4):
            self.sprites.append(pygame.image.load(f'sprites_kenshiro/stand/stand{i}.png'))
        self.sprites.append(pygame.image.load('sprites_kenshiro/stand/stand2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
        self.parado = False

        self.sprites1 = []
        for i in range(8):
            self.sprites1.append(pygame.image.load(f'sprites_kenshiro/soco/soco{i}.png'))
        self.atacar = False

        self.sprites2 = []
        for i in range(8):
            self.sprites2.append(pygame.image.load(f'sprites_kenshiro/buff/buff{i}.png'))
        self.concentrar = False

        self.sprites3 = []
        for i in range(3):
            self.sprites3.append(pygame.image.load(f'sprites_kenshiro/defesa/defesa{i}.png'))
        self.defesa = False

        self.sprites4 = []
        for i in range(4):
            self.sprites4.append(pygame.image.load(f'sprites_kenshiro/hit/hit{i}.png'))
        self.golpeado = False

        self.sprites5 = []
        for i in range(10):
            self.sprites5.append(pygame.image.load(f'sprites_kenshiro/kicks/{i}.png'))
        self.chutes = False

        self.sprites6 = []
        for i in range(6):
            self.sprites6.append(pygame.image.load(f'sprites_kenshiro/super/super{i}.png'))
        self.sequencia = False

        self.sprites7 = []
        for i in range(6):
            self.sprites7.append(pygame.image.load(f'sprites_kenshiro/lose/lose{i}.png'))
        self.perdeu = False

        self.sprites8 = []
        for i in range(2):
            self.sprites8.append(pygame.image.load(f'sprites_kenshiro/win/win{i}.png'))
        self.ganhou = False

    # Todas as funções do personagem kenshiro: pular, correr, bater e etc...
    def atack(self):
        self.atacar = True

    def stand(self):
        self.parado = True

    def buff(self):
        self.concentrar = True

    def defense(self):
        self.defesa = True

    def hit(self):
        self.golpeado = True

    def kicks(self):
        self.chutes = True

    def punch(self):
        self.sequencia = True

    def lose(self):
        self.perdeu = True

    def winner(self):
        self.ganhou = True


    # animando as sprites do personagem 1(kenshiro)
    def update(self):
        # animação 1
        if self.parado == True:
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites):
                self.atual = 0
            self.image = self.sprites[int(self.atual)]

        # animação 2
        if self.atacar == True:
            self.parado = False
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites1):
                self.atual = 0
                self.atacar = False
                self.parado = True
            self.image = self.sprites1[int(self.atual)]

        # animação 3
        if self.concentrar == True:
            self.parado = False
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites2):
                self.atual = 0
                self.concentrar = False
                self.parado = True
            self.image = self.sprites2[int(self.atual)]

        # animação 4
        if self.defesa == True:
            self.parado = False
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites3):
                self.atual = 0
                self.defesa = False
                self.parado = True
            self.image = self.sprites3[int(self.atual)]

        # animação 5
        if self.golpeado == True:
            self.parado = False
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites4):
                self.atual = 0
                self.golpeado = False
                self.parado = True
            self.image = self.sprites4[int(self.atual)]

        # animação 6
        if self.chutes == True:
            self.parado = False
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites5):
                self.atual = 0
                self.chutes = False
                self.parado = True
            self.image = self.sprites5[int(self.atual)]

        # animação 7
        if self.sequencia == True:
            self.parado = False
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites6):
                self.atual = 0
                self.sequencia = False
                self.parado = True
            self.image = self.sprites6[int(self.atual)]

        # animação 8
        if self.perdeu == True:
            self.parado = False
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites7):
                self.atual = 0
                self.perdeu = False
            self.image = self.sprites7[int(self.atual)]

        # animação 9
        if self.ganhou == True:
            self.parado = False
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites8):
                self.atual = 0
                self.ganhou = False
            self.image = self.sprites8[int(self.atual)]



# criando objeto personagem 1(kenshiro)
all_sprites_kenshiro = pygame.sprite.Group()
kenshiro = Kenshiro(200, 25, 10, 'kenshiro', 100, 10)
all_sprites_kenshiro.add(kenshiro)




# criando classe para desenhar a barra de vida das personagens na tela
class vida():
    def __init__(self, pos_x, pos_y, hp, hp_max):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp
        self.hp_max = hp_max

    def desenhe(self, hp):
        self.hp = hp
        ratio = self.hp / self.hp_max
        pygame.draw.rect(janela, red, (self.pos_x, self.pos_y, 150, 10))
        pygame.draw.rect(janela, green, (self.pos_x, self.pos_y, 150 * ratio, 10))


# atribuindo barra de vida para cada personagem
kenshiro_vida = vida(pos_x + 10, pos_y + 30, kenshiro.hp, kenshiro.hp_max)
seiya_vida = vida(pos_x + 430, pos_y + 30, kenshiro.hp, kenshiro.hp_max)


# classe para desenhar barra de energia
class energia():
    def __init__(self, pos_x, pos_y, energia, energia_max):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.energia = energia
        self.energia_max = energia_max

    def desenhe(self, energia):
        self.energia = energia
        ratio = self.energia / self.energia_max
        pygame.draw.rect(janela, red, (self.pos_x, self.pos_y, 150, 10))
        pygame.draw.rect(janela, blue, (self.pos_x, self.pos_y, 150 * ratio, 10))


# atribuindo barra de energia para cada personagem
kenshiro_energia = energia(pos_x + 10, pos_y + 65, kenshiro.energia, kenshiro.energia_max)
seiya_energia = energia(pos_x + 430, pos_y + 65, seiya.energia, seiya.energia_max)

# execução da animação dos personagens parados
kenshiro.stand()
seiya.stand()

# criação da variavel para definir tempo develocidade do jogo
clock = pygame.time.Clock()

# inicio do jogo
window_open = True
while window_open:
    # definição do tempo do jogo em velocidade
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_open = False

    # comandos do personagem kenshiro e execução de funções:
    ordens = pygame.key.get_pressed()
    if ordens[pygame.K_a] and turno_p1 == True:
        kenshiro.atack()
        seiya.hit()
        efeitos_actions()
        turno_p1 = False
        turno_p2 = True

    if ordens[pygame.K_q] and turno_p1 == True and kenshiro.energia >= 25:
        kenshiro.buff()
        efeitos_actions()
        turno_p1 = False
        turno_p2 = True

    if ordens[pygame.K_w] and turno_p1 == True and kenshiro.energia >= 40:
        kenshiro.kicks()
        seiya.hit()
        efeitos_actions()
        turno_p1 = False
        turno_p2 = True

    if ordens[pygame.K_e] and turno_p1 == True and kenshiro.energia >= 75:
        kenshiro.punch()
        seiya.hit()
        efeitos_actions()
        turno_p1 = False
        turno_p2 = True



    # comandos seiya e execução de funções:
    if ordens[pygame.K_1] and turno_p2 == True:
        seiya.atack()
        kenshiro.hit()
        efeitos_actions()
        turno_p2 = False
        turno_p1 = True
        bonus()

    if ordens[pygame.K_2] and turno_p2 == True and seiya.energia >= 70:
        seiya.meteor()
        kenshiro.hit()
        efeitos_actions()
        turno_p2 = False
        turno_p1 = True
        bonus()

    if ordens[pygame.K_3] and turno_p2 == True and seiya.energia >= 50:
        seiya.comet()
        kenshiro.hit()
        efeitos_actions()
        turno_p2 = False
        turno_p1 = True
        bonus()

    if ordens[pygame.K_4] and turno_p2 == True and seiya.energia >= 40:
        seiya.buff()
        efeitos_actions()
        turno_p2 = False
        turno_p1 = True
        bonus()

    #final de combate
    final()

    limite()
    # inserindo fundo na tela
    janela.fill((0, 0, 0))
    janela.blit(fundo, (0, 0))

    # escreve as informações das personagens na tela
    escrever_texto()

    # desenhando barra de vida e energia de cada personagem
    kenshiro_vida.desenhe(kenshiro.hp)
    kenshiro_energia.desenhe(kenshiro.energia)
    seiya_vida.desenhe(seiya.hp)
    seiya_energia.desenhe(seiya.energia)

    # desenhando os personagens, fundo e outros elementos na tela
    all_sprites_kenshiro.draw(janela)
    all_sprites_kenshiro.update()

    all_sprites_seiya.draw(janela)
    all_sprites_seiya.update()

    pygame.display.flip()
