from asyncio import gather
from time import sleep
import numpy as np

#Classe que representa um vértice na lista de adjacência
class Vertice(object):

    #Ele guarda o seu índice, quantos vértices são adjacentes a ele,
    #e um dicionário que guarda os pesos das arestas incidentes
    def __init__(self, valor):
        self.indice = valor
        self.adjacentes = 0
        self.vizinhos = {}

    #Função que adiciona um vizinho ao vértice
    #Ela insere o peso da aresta na posição de índice "vizinho" do dicionário
    def add_vizinho(self, vizinho, peso):
        self.vizinhos[vizinho] = peso
        self.adjacentes += 1

    #Função que remove um vizinho do vértice
    def remove_vizinho(self, vizinho):
        del self.vizinhos[vizinho]
        self.adjacentes -= 1

    #Função que imprime a lista de adjacência do vértice
    def __str__(self):
        text = []
        for x in self.vizinhos:
            text.append('{} -> {} com peso: {}'.format(self.indice, x.indice, self.vizinhos[x]))
            text.append(', ')
        text = text[:-1]
        return ''.join(text)

    #Função que retorna o dicionário contendo os vizinhos
    #do vértice e o peso das arestas até eles
    def get_vizinhos(self):
        return self.vizinhos

    #Função que retorna os outros vértices que estão conectados ao vértice
    def get_coneccoes(self):
        return self.vizinhos.keys()

    #Função que retorna o peso de uma aresta até outro vértice
    def get_peso(self, vizinho):
        return self.vizinhos[vizinho]

#Classe que representa um grafo
class Grafo(object):

    #Ele guarda o seu nome, quantos vértices e quantas arestas o grafo possui,
    #e a lista e a matriz de adjacência do grafo
    #Ele adiciona 1 vértice no grafo ao ser criado
    def __init__(self):
        self.nome = 'G'
        self.vertice = 0
        self.aresta = 0
        self.vertices = {}
        self.matrizVertices = []
        self.AddVertice(Vertice(1))

    #Função que verifica se o grafo existe
    def existe(self):
        try:
            self.nome
            return True
        except:
            print('Grafo não existe')

    #Função que adiciona um vértice com índice "vertice" ao grafo
    def AddVertice(self, vertice):
        if self.existe():
            self.vertices[vertice.indice] = vertice
            self.vertice += 1

    #Função que retorna um vértice com índice "indice" do grafo
    def get_vertice(self, indice):
        if self.existe():
            try:
                return self.vertices[indice]
            except KeyError:
                return None

    #Função que imprime a lista de adjacência do grafo
    def Grafo(self):
        if self.existe():
            for v in self:
                print('Vértice {}'.format(v.indice), end="")
                for w in v.get_coneccoes():
                    print(' -Peso {}-> Vértice {}'.format(v.get_peso(self.get_vertice(w.indice)), w.indice), end="")
                print('')

    #Função que retorna se o vértice de índice "indice" pertence ao Grafo
    def EVertice(self, indice):
        if self.existe():
            if self.get_vertice(indice) is not None:
                print('Vértice {} pertece ao Grafo {}'.format(indice, self.nome))
            else:
                print('Vértice {} não pertece ao Grafo {}'.format(indice, self.nome))

    def __contains__(self, indice):
        if self.existe():
            return indice in self.vertices

    #Função que adiciona uma aresta de peso "peso" saindo do vértice de índice
    #"indice_saida" e chegando ao vértice de índice "indice_chegada"
    def AddAresta(self, indice_saida, indice_chegada, peso):
        if self.existe():
            if indice_saida not in self.vertices or indice_chegada not in self.vertices:
                print('Um ou mais vértices não existem!')
                return 0
            self.vertices[indice_saida].add_vizinho(self.vertices[indice_chegada], peso)
            self.aresta += 1
    
    #Função que remove uma aresta de peso "peso" saindo do vértice de índice
    #"indice_saida" e chegando ao vértice de índice "indice_chegada",
    #se esta aresta existir
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
    
    #Função que retorna se existe uma aresta de peso "peso" saindo do vértice de
    #índice "indice_saida" e chegando ao vértice de índice "indice_chegada",
    def ExisteAresta(self, indice_saida, indice_chegada, peso):
        if self.existe():
            if indice_saida not in self.vertices or indice_chegada not in self.vertices:
                print('Um ou mais vértices não existem!')
                return 0
            if self.vertices[indice_saida].get_peso(self.vertices[indice_chegada]) != peso:
                print('Não existe aresta com peso {} do vértice {} para o vértice {}'.format(peso, indice_saida, indice_chegada))
                return 0
            print('Existe aresta com peso {} do vértice {} para o vértice {}'.format(peso, indice_saida, indice_chegada))

    #Função que muda o peso de uma aresta de peso "peso" para "novo_peso", saindo do vértice de índice
    #"indice_saida" e chegando ao vértice de índice "indice_chegada", se esta aresta existir
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

    #Função que imprime todos os vértices e todas as arestas do grafo
    def ImprimeGrafo(self):
        if self.existe():
            print('Grafo {}:'.format(self.nome))
            print('Vértices: {}'.format([x.indice for x in self]))
            print('Arestas: ')
            for v in self:
                print(v)
    
    #def RecuperaPeso(self, indice_saida, indice_chegada):

    #Função que retorna se o grafo é simples ou não
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

    #Função que retorna o complemento do grafo 
    def Complemento(self, grafo):
        if self.existe():
            for v in self:
                vetor = np.zeros((self.vertice), dtype=np.int)
                for w in v.get_coneccoes():
                    vetor[w.indice-1] = 1
                for j in range(self.vertice):
                    if vetor[j] == 0:
                        grafo.AddAresta(v.indice, j+1, 1)
            return grafo

    #Função que retorna se existe uma aresta saindo do vértice de
    #índice "indice_saida" e chegando ao vértice de índice "indice_chegada"
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

    #Função que retorna a lista de adjacência do vértice de índice "indice"
    def Adjacencia(self, indice):
        if self.existe():
            if indice not in self.vertices:
                print('Vértice não existe!')
                return 0
            print('Vértice {}'.format(indice), end="")
            for w in self.vertices[indice].get_coneccoes():
                print(' -Peso {}-> Vértice {}'.format(self.vertices[indice].get_peso(self.get_vertice(w.indice)), w.indice), end="")
            print('')

    #Função que retorna as arestas incidentes as vértice de índice "indice"
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

    #Função que constrói a matriz de adjacência do grafo
    def MatrizAdj(self):
        if self.existe():
            matriz = np.zeros((self.vertice, self.vertice), dtype=np.int)
            for v in self:
                for w in v.get_coneccoes():
                    matriz[v.indice-1][w.indice-1] = v.get_peso(self.get_vertice(w.indice))
            self.matrizVertices = matriz

    #Função que imprime a matriz de adjacência do grafo
    def ImprimeMatrizAdj(self):
        for i in range(self.vertice):
            for j in range(self.vertice):
                if j != self.vertice-1:
                    print('{}, '.format(self.matrizVertices[i][j]), end="")
                else:
                    print('{}'.format(self.matrizVertices[i][j]), end="")
            print('')

    #def Conexo(self):

    #Função que deleta as informações do grafo
    def del_grafo(self):
        if self.existe():
            del self.nome
            del self.vertice
            del self.aresta
            del self.vertices
            del self.matrizVertices

    #Função que retorna os vértices existentes no grafo
    def get_vertices(self):
        if self.existe():
            return self.vertices.keys()

    def __iter__(self):
        if self.existe():
            return iter(self.vertices.values())

#Função que cria um novo grafo com apenas um vértice
def NovoGrafo():
    g = Grafo()
    return g

#Função que remove o grafo da memória
def RemoveGrafo(g):
    g.del_grafo()

#Função que cria um novo grafo vazio e 
#transforma ele no complemento do grafo "g"
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
    
   

#Funções de Percursos


def DSF(G, vi):

    saida = {}  #Vai associar cada vertice ao vertice que o alconçou pela primeira vez

    #Cor cinza para visitados, bracos não visitados e preto para os percorridos
    #Custo é o custo para chegar aquele vertice

    for vertice in G.vertices():
        G.vertices[vertice]['cor'] = 'branco'
        G.vertices[vertice]['custo'] = float('inf')

    G.vertices[vi]['cor'] = 'cinza'
    G.nodes[vi]['custo'] = 0

    #Iniciando uma pilha (estrtura usado para busca em profundidade)
    pilha = Pilha()

    #insere vi (raiz) na fila

    pilha.push(vi)

    while not pilha.isEmpty():

        #Pegar o ultimo elemento empilhado
        u = pilha.pop()

        for vertice in G.vizinhos(u):
            if (G.vertices[vertice]['cor'] == 'branco'):
                G.vertices[vertice]['custo'] = G.vertices[u]['custo'] + 1
                saida[vertice] = u
                G.vertices[vertice]['cor'] = 'cinza'
                pilha.push(vertice)
        
        #Depois que o vertice 'u' é percorrido, muda para a cor 'preto'
        G.vertices[u]['cor'] = 'preto'

    return saida


def BSF(G, vi):

    saida = {}  #Vai associar cada vertice ao vertice que o alconçou pela primeira vez

    #Cor cinza para visitados, bracos não visitados e preto para os percorridos
    #Custo é o custo para chegar aquele vertice

    for vertice in G.vertices():
        G.vertices[vertice]['cor'] = 'branco'
        G.vertices[vertice]['custo'] = float('inf')

    G.vertices[vi]['cor'] = 'cinza'
    G.nodes[vi]['custo'] = 0

    #Iniciando uma fila (estrtura usado para busca em largura), o que difere do código de DSF
    fila = deque()

    #insere vi (raiz) na fila

    fila.append(vi)

    while (len(fila) > 0):
        u = fila.popleft()

        for vertice in G.vizinhos(u):
            if (G.vertices[vertice]['cor'] == 'branco'):
                G.vertices[vertice]['custo'] = G.vertices[u]['custo'] + 1
                saida[vertice] = u
                G.vertices[vertice]['cor'] = 'cinza'
                fila.append(vertice)
        
        #Depois que o u é percorrido, muda para a cor 'preto'
        G.vertices[u]['cor'] = 'preto'

    return saida


#Caminhos Minimos

def escolherMinimo():    #Função usada para escolher o vertice vj que pertence a V - V' que minimiza o c(j)
    a = 1

def dijkstra(G, vi, vj):

    listaV = list()       #lista de vert V - V'
    lista = list()         #Lista de vertices V'
    infinito = float('inf')
    distancia = []     #Distancia de vi a cada vertice
    pred = []   #predecessor de cada vértice


    listaV = G.vertices()
    listaV.remove(vi)
    lista.append(vi)

    for v in range(G.vertice()):
        distancia[v].append(RecuperaPeso(G, vi, v))
        pred[v].append(None)

    
    while (len(lista) != len(G.vertice)):
        vmin = escolherMinimo() #Escrever função escolherMinimo()
        lista.append(vmin)
        for i in 

        for i in lista:
            if (distancia[i] < min):
                min = distancia[i];
                u = i
        
        try:
            lista.remove(u)
        except:
            lista.pop(0)

        for i in #vizinhos de vmin:
            if((distancia[i]) < (distancia[vmin] + RecuperaPeso(G, vmin, i))):
                distancia[i] = distancia[i]
            else:
                distancia[i] = (distancia[vmin] + RecuperaPeso(G, vmin, i))
            


