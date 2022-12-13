from enum import Enum

class Juiz:
    @classmethod
    def julgar_vencedor(cls, input_jogador1, input_jogador2):
        pass
    

class PedraPapelTesoura:
    input_tipos = ["pedra", "papel", "tesoura", "fim"]

    @classmethod
    def _get_input_jogador(cls, ):
        input_jogador = None
        while input_jogador not in cls.input_tipos:
            input_jogador = input().lower()
            if input_jogador not in cls.input_tipos:
                print(f"Input inválido. Tente: {cls.input_tipos}")
        return input_jogador


    @classmethod
    def jogar(cls, ):

        pararJogo = False
        while not pararJogo:
            print("Input (Jogador 1):")
            input_jogador1 = cls._get_input_jogador()
            print("Input (Jogador 2):")
            input_jogador2 = cls._get_input_jogador()
            





        

if __name__ == "__main__":
    PedraPapelTesoura.jogar()