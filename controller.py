# controlle.py
# controller.py
from model import Roupa, Venda, relatorio_estoque_baixo

class LojaController:
    def __init__(self):
        self.estoque = []
        self.venda_atual = Venda()

    def adicionar_roupa_estoque(self, roupa):
        self.estoque.append(roupa)

    def listar_estoque(self):
        return [str(roupa) for roupa in self.estoque]

    def realizar_venda(self, codigo, quantidade):
        for roupa in self.estoque:
            if roupa.codigo == codigo:
                self.venda_atual.adicionar_item(roupa, quantidade)
                return
        print("❌ Produto não encontrado!")

    def finalizar_venda(self):
        return self.venda_atual.finalizar_venda()

    def gerar_relatorio_estoque_baixo(self):
        return relatorio_estoque_baixo(self.estoque)
    def excluir_roupa(self, codigo):
     for roupa in self.estoque:
        if roupa.codigo == codigo:
            self.estoque.remove(roupa)
            print(f"✅ Produto {roupa.nome} removido do estoque.")
            return True
            print("❌ Produto não encontrado!")
            return False
