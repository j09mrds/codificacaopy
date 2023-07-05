# Codificação em Python (Revista, Edição e Artigo)
# Atividade do 2° bimestre 

class Artigo:
    def __init__ (self,titulo, autor, idArtigo):
        self.titulo = titulo
        self.autor = autor
        self.idArtigo = idArtigo
    
    def getArtigo(self):
        return "Titulo:" + self.titulo + " | " + "Autor: " + self.autor + " | " + self.idArtigo

class Edicao:

    def __init__ (self, numero, volume, data, idEdicao):
        self.numero = numero
        self.volume = volume
        self.data = data
        self.idEdicao = idEdicao
        self.artigos = []
    
    def addNovoArtigo(self, idArtigo):
        self.artigos.append(artigo)

    def alterarArtigo(self, idArtigo, titulo, autor):
        artigo_para_modificar = input(" Digite o número do artigo que deseja modificar: ")
        if (artigo_para_modificar == idArtigo):
            novoTitulo = input("Escreva o novo titulo do artigo: ")
            titulo = novoTitulo
            novoAutor = input("Escreva o novo nome do autor do artigo: ")
            autor = novoAutor
            print("Alteração realizada com sucesso !!")
        else:
            input("Artigo não encontrado, tente novamente ou certifique se é um número existente no sistema")

    def deletarArtigo(self,idArtigo):
        artido_para_deletar = input(" Digite o artigo que deseja deletar:")
        if (artido_para_deletar == idArtigo):
            resposta = input ("Realmente deseja deletar esse arquivo?? Digite S para sim e N para não")
            if(resposta == "S" | "s"):
                print("O artigo foi deletado com sucesso!!")
            else:
                return("O Artigo não foi excluido")
        else:
            return("Artigo não encontrado no sistema, tente novamente ou certifique se é um número existente no sistema")

    def getEdicao(self):
        return "Edição número: " +  str(self.numero) + " | " + "Volume: " str(self)

    def showArtigos(self):
        data = ""
        for artigo in self.artigos:
            print(artigo.getArtigo())
    
    def getNumeroDeArtigo(self):
        return len(self.artigos)

class Revista:

    def __init__(self, titulo, issn, periodicidade):
        self.titulo = titulo
        self.issn = issn
        self.periodicidade = periodicidade
        self.edicoes = []

    def addNovaEdicao(self, edicao):
        num_artigos = edicao.getNumeroDeArtigo()
        if(num_artigos >= 10 and num_artigos <= 15):
            self.edicoes.append(edicao)
            return "Edição Lançada com Sucesso !"
        else:
            return "É necessário no mínimo 10 artigos e no màximo 15 artigos para registrar "
    
    def showEdicoes(self):
        data =""
        for edicao in self.edicoes:
            print(edicao.getEdicao())

    def alterarEdicao(self, idEdicao, numero, volume, data):
         edicao_para_modificar = input(" Digite a edição que deseja modificar: ")
        if (edicao_para_modificar == idEdicao):
            novo_numero_edicao = input("Escreva o novo numero da edicão: ")
            numero = novo_numero_edicao
            novo_volume_edicao = input("Escreva o novo volume da edição: ")
            volume = novo_volume_edicao
            nova_data_edicao = input("Escreva a nova data da edição: ")
            data = nova_data_edicao
        else:
            input("Edição não encontrado, tente novamente ou certifique se é um número existente no sistema")


    def deletarEdicao (self, idEdicao):
        edicao_para_deletar = input(" Digite a edição que deseja deletar:")
        if (edicao_para_deletar == idEdicao):
            resposta = input ("Realmente deseja deletar essa edição?? Digite S para sim e N para não")
            if(resposta == "S" | "s"):
                print("A edição foi deletada com sucesso!!")
            else:
                return("A edição não foi excluida")
        else:
            return("Edição não encontrada no sistema, tente novamente ou certifique se é um número existente no sistema")
