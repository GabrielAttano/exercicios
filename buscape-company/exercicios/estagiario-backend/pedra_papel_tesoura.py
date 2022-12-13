from enum import Enum

class Juiz:
    @classmethod
    def julgar_vencedor(cls, input_jogador1, input_jogador2):
        if input_jogador1 == input_jogador2:
            return 0

        if input_jogador1 == "pedra":
            if input_jogador2 == "papel":
                return 2
            if input_jogador2 == "tesoura":
                return 1
        if input_jogador1 == "papel":
            if input_jogador2 == "pedra":
                return 1
            if input_jogador2 == "tesoura":
                return 2
        if input_jogador1 == "tesoura":
            if input_jogador2 == "papel":
                return 1
            if input_jogador2 == "pedra":
                return 2
    

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
            print("===================")
            print("Input (Jogador 1):")
            input_jogador1 = cls._get_input_jogador()
            print("Input (Jogador 2):")
            input_jogador2 = cls._get_input_jogador()
            print("===================")
            if input_jogador1 == "fim" or input_jogador2 == "fim":
                print("Finalizando jogo")
                pararJogo = True
            else:
                vencedor = Juiz.julgar_vencedor(input_jogador1, input_jogador2)
                if vencedor == 0:
                    print("Empate")
                else:
                    print(f"Jogador {vencedor}")





        

if __name__ == "__main__":
    PedraPapelTesoura.jogar()