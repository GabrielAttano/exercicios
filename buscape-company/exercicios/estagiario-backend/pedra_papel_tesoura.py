from enum import Enum

class Juiz:
    @classmethod
    def julgar_vencedor(cls, input_jogador1, input_jogador2):
        pass
    

class PedraPapelTesoura:
    input_tipos = ["pedra", "papel", "tesoura", "fim"]

    def _get_input_jogador(self, ):
        input_jogador = None
        while input_jogador not in self.input_tipos:
            input_jogador = input().lower()
        return input_jogador


    @classmethod
    def jogar(cls, ):

        pararJogo = False
        while not pararJogo:
            input_jogador1 = cls._get_input_jogador()
            input_jogador2 = cls._get_input_jogador()
            




        

if __name__ == "__main__":
    pass