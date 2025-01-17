from asyncio import gather
from time import sleep
import numpy as np

class Vertice(object):
    def __init__(self, valor):
        self.indice = valor
        self.adjacentes = 0
        self.vizinhos = {}

    def add_vizinho(self, vizinho, peso):
        self.vizinhos[vizinho] = peso
        self.adjacentes += 1

    def remove_vizinho(self, vizinho):
        del self.vizinhos[vizinho]
        self.adjacentes -= 1

    def __str__(self):
        text = []
        for x in self.vizinhos:
            text.append('{} -> {} com peso: {}'.format(self.indice, x.indice, self.vizinhos[x]))
            text.append(', ')
        text = text[:-1]
        return ''.join(text)

    def get_vizinhos(self):
        return self.vizinhos

    def get_coneccoes(self):
        return self.vizinhos.keys()

    def get_peso(self, vizinho):
        return self.vizinhos[vizinho]

class Grafo(object):
    def __init__(self):
        self.nome = 'G'
        self.vertice = 0
        self.aresta = 0
        self.vertices = {}
        self.matrizVertices = []
        self.AddVertice(Vertice(1))

    def existe(self):
        try:
            self.nome
            return True
        except:
            print('Grafo não existe')

    def AddVertice(self, vertice):
        if self.existe():
            self.vertices[vertice.indice] = vertice
            self.vertice += 1

    def get_vertice(self, indice):
        if self.existe():
            try:
                return self.vertices[indice]
            except KeyError:
                return None

    def Grafo(self):
        if self.existe():
            for v in self:
                print('Vértice {}'.format(v.indice), end="")
                for w in v.get_coneccoes():
                    print(' -Peso {}-> Vértice {}'.format(v.get_peso(self.get_vertice(w.indice)), w.indice), end="")
                print('')

    def EVertice(self, indice):
        if self.existe():
            if self.get_vertice(indice) is not None:
                print('Vértice {} pertece ao Grafo {}'.format(indice, self.nome))
            else:
                print('Vértice {} não pertece ao Grafo {}'.format(indice, self.nome))

    def __contains__(self, indice):
        if self.existe():
            return indice in self.vertices

    def AddAresta(self, indice_saida, indice_chegada, peso):
        if self.existe():
            if indice_saida not in self.vertices or indice_chegada not in self.vertices:
                print('Um ou mais vértices não existem!')
                return 0
            self.vertices[indice_saida].add_vizinho(self.vertices[indice_chegada], peso)
            self.aresta += 1
    
    def RemoveAresta(self, indice_saida, indice_chegada, peso):
        if self.existe():
            if indice_saida not in self.vertices or indice_chegada not in self.vertices:
                print('Um ou mais vértices não existem!')
                return 0
            if self.vertices[indice_saida].get_peso(self.vertices[indice_chegada]) != peso:
                print('Não existe aresta com peso {} do vértice {} para o vértice {}'.format(peso, indice_saida, indice_chegada))
                return 0
            self.vertices[indice_saida].remove_vizinho(self.vertices[indice_chegada])
            self.aresta -= 1
            print('Aresta removida com sucesso')
    
    def ExisteAresta(self, indice_saida, indice_chegada, peso):
        if self.existe():
            if indice_saida not in self.vertices or indice_chegada not in self.vertices:
                print('Um ou mais vértices não existem!')
                return 0
            if self.vertices[indice_saida].get_peso(self.vertices[indice_chegada]) != peso:
                print('Não existe aresta com peso {} do vértice {} para o vértice {}'.format(peso, indice_saida, indice_chegada))
                return 0
            print('Existe aresta com peso {} do vértice {} para o vértice {}'.format(peso, indice_saida, indice_chegada))

    def MudaPeso(self, indice_saida, indice_chegada, peso, novo_peso):
        if self.existe():
            if indice_saida not in self.vertices or indice_chegada not in self.vertices:
                print('Um ou mais vértices não existem!')
                return 0
            if self.vertices[indice_saida].get_peso(self.vertices[indice_chegada]) != peso:
                print('Não existe aresta com peso {} do vértice {} para o vértice {}'.format(peso, indice_saida, indice_chegada))
                return 0
            self.vertices[indice_saida].add_vizinho(self.vertices[indice_chegada], novo_peso)
            print('Peso mudado com sucesso')

    def ImprimeGrafo(self):
        if self.existe():
            print('Grafo {}:'.format(self.nome))
            print('Vértices: {}'.format([x.indice for x in self]))
            print('Arestas: ')
            for v in self:
                print(v)
    
    #def RecuperaPeso(self, indice_saida, indice_chegada):

    def GrafoSimples(self):
        if self.existe():
            for v in self:
                vetor = np.zeros((self.vertice), dtype=np.int)
                for w in v.get_coneccoes():
                    if v.indice == w.indice:
                        print('O Grafo {} não é simples'.format(self.nome))
                        return 0
                    vetor[w.indice-1] += 1
                    if vetor[w.indice-1] > 1:
                        print('O Grafo {} não é simples'.format(self.nome))
                        return 0
            print('O Grafo {} é simples'.format(self.nome))

    #def EArvore(self):

    #def EBipartido(self):

    def Complemento(self, grafo):
        if self.existe():
            for v in self:
                vetor = np.zeros((self.vertice), dtype=np.int)
                for w in v.get_coneccoes():
                    vetor[w.indice-1] = 1
                print('{}'.format(self.vertice))
                for j in range(self.vertice):
                    if vetor[j] == 0:
                        print('{} {}'.format(v.indice, j+1))
                        grafo.AddAresta(v.indice, j+1, 1)
            return grafo

    def EAdj(self, indice_saida, indice_chegada):
        if self.existe():
            if indice_saida not in self.vertices or indice_chegada not in self.vertices:
                print('Um ou mais vértices não existem!')
                return 0
            for w in self.vertices[indice_saida].get_coneccoes():
                if w.indice == indice_chegada:
                    print('A aresta V{}V{} existe'.format(indice_saida, indice_chegada))
                    return 0
            print('A aresta V{}V{} não existe'.format(indice_saida, indice_chegada))

    def Adjacencia(self, indice):
        if self.existe():
            if indice not in self.vertices:
                print('Vértice não existe!')
                return 0
            print('Vértice {}'.format(indice), end="")
            for w in self.vertices[indice].get_coneccoes():
                print(' -Peso {}-> Vértice {}'.format(self.vertices[indice].get_peso(self.get_vertice(w.indice)), w.indice), end="")
            print('')

    def Incidencia(self, indice):
        if self.existe():
            if indice not in self.vertices:
                print('Vértice não existe!')
                return 0
            print('Arestas incidentes ao vértice {}: '.format(indice))
            i = 0
            for w in self.vertices[indice].get_coneccoes():
                if i == 0:
                    print('V{}V{}'.format(indice, w.indice), end="")
                else:
                    print(' ,V{}V{}'.format(indice, w.indice), end="")
                i = 1
            print('')

    def MatrizAdj(self):
        if self.existe():
            matriz = np.zeros((self.vertice, self.vertice), dtype=np.int)
            for v in self:
                for w in v.get_coneccoes():
                    matriz[v.indice-1][w.indice-1] = v.get_peso(self.get_vertice(w.indice))
            self.matrizVertices = matriz

    def ImprimeMatrizAdj(self):
        for i in range(self.vertice):
            for j in range(self.vertice):
                if j != self.vertice-1:
                    print('{}, '.format(self.matrizVertices[i][j]), end="")
                else:
                    print('{}'.format(self.matrizVertices[i][j]), end="")
            print('')

    #def Conexo(self):

    def del_grafo(self):
        if self.existe():
            del self.nome
            del self.vertice
            del self.aresta
            del self.vertices
            del self.matrizVertices

    def get_vertices(self):
        if self.existe():
            return self.vertices.keys()

    def __iter__(self):
        if self.existe():
            return iter(self.vertices.values())

def NovoGrafo():
    g = Grafo()
    return g

def RemoveGrafo(g):
    g.del_grafo()

def Complemento(g):
    gc = NovoGrafo()
    for i in range(2, (g.vertice)+1):
        gc.AddVertice(Vertice(i))
    return g.Complemento(gc)

if __name__ == "__main__":
    g = NovoGrafo()
    for i in range(2, 7):
        g.AddVertice(Vertice(i))
    g.EVertice(6)
    g.EVertice(7)
    g.AddAresta(1, 2, 5)
    g.AddAresta(1, 6, 2)
    g.AddAresta(2, 3, 4)
    g.AddAresta(3, 4, 9)
    g.AddAresta(4, 5, 7)
    g.AddAresta(4, 6, 3)
    g.AddAresta(5, 1, 1)
    g.AddAresta(6, 5, 8)
    g.AddAresta(6, 3, 1)
    g.RemoveAresta(7, 3, 5)
    g.RemoveAresta(6, 3, 5)
    g.RemoveAresta(6, 3, 1)
    g.ExisteAresta(5, 1, 1)
    g.MudaPeso(5, 1, 1, 4)
    g.Grafo()
    g.ImprimeGrafo()
    g.GrafoSimples()
    gc = Complemento(g)
    gc.Grafo()
    gc.ImprimeGrafo()
    #g.AddAresta(1, 1, 3)
    g.GrafoSimples()
    g.EAdj(1, 2)
    g.EAdj(1, 3)
    g.Adjacencia(3)
    g.Adjacencia(4)
    g.Incidencia(2)
    g.Incidencia(1)
    g.MatrizAdj()
    g.ImprimeMatrizAdj()
    print('')
    gc.MatrizAdj()
    gc.ImprimeMatrizAdj()
    #RemoveGrafo(g)
    #g.Grafo()