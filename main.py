from random import randint
from time import sleep
import cowsay
import sys
import os
import pygame


pygame.mixer.init()


class Game():
    def __init__(self):
        self.clean_screen()
        self.first_phase()


    def clean_screen(self) -> None:
        os.system("cls")


    def play_music(self, music: str) -> None:
        pygame.mixer.music.load(f"music/{music}")
        pygame.mixer.music.play()


    def speed_text(self, text: str) -> None:
        for letra in text:
            sys.stdout.write(letra)
            sys.stdout.flush()
            sleep(0.06)


    def first_phase(self) -> None:
        self.play_music("first_phase.mp3")
        self.speed_text("Vivemos num planeta onde temos que enfrentar desafios e criaturas assustadoras...\nAcho que está na hora de você conhecer algum...")
        sleep(0.5)
        self.clean_screen()

        tentativas = 3

        cowsay.ghostbusters("Olá humano, me diga seu nome...")
        self.nome = str(input("Seu nome: "))

        while self.nome == '':
            cowsay.ghostbusters("\033[1;31mDigita teu nomeeeeee\033[m")
            self.nome = str(input("Seu nome: "))

        cowsay.ghostbusters(f"{self.nome.upper()}, irei pensar em um número entre 0 e 5.\nTente adivinhar...\nVocê possui 3 chances para conseguir...")
        escolhido = randint(0, 5)

        while True:
            try:
                numero = int(input("Digite o número: "))

                if numero == escolhido:
                    self.play_music("venceu.mp3")
                    cowsay.ghostbusters("\033[1;32mParabéns! Você acertou.\033[m")
                    sleep(4)
                    self.clean_screen()
                    self.second_phase()
                    break
                else:
                    tentativas -= 1
                    cowsay.ghostbusters(f"\033[1;31mErrado! Deixa de ser burro e tenta de novo.\n\nVocê tem {tentativas} tentativas\033[m")

                    if tentativas == 0:
                        self.play_music("game_over.mp3")
                        self.clean_screen()
                        cowsay.ghostbusters(f"\033[1;31mFim de jogo\n\nHAHAHAHAHAHAHA\n\nO número era {escolhido}\033[m")
                        sleep(12)
                        
                        try_again = str(input("Tentar novamente [S / N]?: "))

                        if try_again.upper() == 'S':
                            self.clean_screen()
                            self.first_phase()
                        else:
                            break
            
            except ValueError:
                cowsay.ghostbusters("\033[1;31mApenas números são permitidos!\033[m")

    
    def second_phase(self) -> None:
        self.play_music("second_phase.mp3")
        self.speed_text("Vejo que você conseguiu ser bem sucedido na sua primeira missão.\nVeremos no próximo desafio...")
        sleep(0.5)
        self.clean_screen()
        cowsay.meow(f"{self.nome.upper()}, você passou de fase. Aguarde as próximas aventuras...")

        while True:
            print("Aguarde as atualizações...")
            sleep(5)



Game()