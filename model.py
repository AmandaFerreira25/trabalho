# model.py

class Roupa:
    def __init__(self, codigo, nome, tamanho, cor, preco, estoque):
        self.codigo = codigo
        self.nome = nome
        self.tamanho = tamanho
        self.cor = cor
        self.preco = preco
        self.estoque = estoque

    def atualizar_estoque(self, quantidade):
        """Atualiza o estoque somando ou subtraindo quantidade"""
        self.estoque += quantidade

    def vender(self, quantidade):
        """Tenta vender uma quantidade de peças"""
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            return True
        else:
            return False

    def __str__(self):
            return f"{self.nome} - Tam: {self.tamanho} - Cor: {self.cor} - R$ {self.preco:.2f} - Estoque: {self.estoque}"


class Venda:
    def __init__(self):
        self.itens = []
        self.total = 0.0

    def adicionar_item(self, roupa, quantidade):
        if roupa.vender(quantidade):
            self.itens.append((roupa.nome, roupa.tamanho, roupa.cor, quantidade, roupa.preco))
            self.total += roupa.preco * quantidade
        else:
            print(f"❌ Estoque insuficiente para {roupa.nome} (Tam: {roupa.tamanho}, Cor: {roupa.cor})")

    def finalizar_venda(self):
         return f"✅ Venda finalizada. Total: R$ {self.total:.2f}"

    def listar_itens(self):
         return self.itens


    def relatorio_estoque_baixo(lista_roupas, minimo=3):
     alerta = []
     for roupa in lista_roupas:
        if roupa.estoque < minimo:
            alerta.append(f"⚠️ {roupa.nome} (Tam: {roupa.tamanho}, Cor: {roupa.cor}) tem apenas {roupa.estoque} em estoque!")
        return alerta


class Roupa:
    def __init__(self, codigo, nome, tamanho, cor, preco, estoque):
        self.codigo = codigo
        self.nome = nome
        self.tamanho = tamanho
        self.cor = cor
        self.preco = preco
        self.estoque = estoque


def atualizar_estoque(self, quantidade):
    """Atualiza o estoque somando ou subtraindo quantidade"""
    self.estoque += quantidade

def vender(self, quantidade):
    """Tenta vender uma quantidade de peças"""
    if quantidade <= self.estoque:
        self.estoque -= quantidade
        return True
    else:
        return False

def __str__(self):
    return f"{self.nome} - Tam: {self.tamanho} - Cor: {self.cor} - R$ {self.preco:.2f} - Estoque: {self.estoque}"


class Venda:
    def __init__(self):
     self.itens = []
     self.total = 0.0


    def adicionar_item(self, roupa, quantidade):
        if roupa.vender(quantidade):
            self.itens.append((roupa.nome, roupa.tamanho, roupa.cor, quantidade, roupa.preco))
            self.total += roupa.preco * quantidade
        else:
            print(f"❌ Estoque insuficiente para {roupa.nome} (Tam: {roupa.tamanho}, Cor: {roupa.cor})")

    def finalizar_venda(self):
        return f"✅ Venda finalizada. Total: R$ {self.total:.2f}"

    def listar_itens(self):
        return self.itens




    def relatorio_estoque_baixo(lista_roupas, minimo=3):
        alerta = []
        for roupa in lista_roupas:
            if roupa.estoque < minimo:
                alerta.append(f"⚠️ {roupa.nome} (Tam: {roupa.tamanho}, Cor: {roupa.cor}) tem apenas {roupa.estoque} em estoque!")
                return alerta

    

    def excluir_roupa(lista_roupas, codigo):
        for roupa in lista_roupas:
            if roupa.codigo == codigo:
                lista_roupas.remove(roupa)
                print(f"🗑️ Roupa '{roupa.nome}' (código {codigo}) removida com sucesso.")
                return True
            print(f"❌ Nenhuma roupa encontrada com o código {codigo}.")
            return False

