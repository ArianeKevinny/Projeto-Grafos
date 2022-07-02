#include <stdlib.h>
#include <stdio.h>
#include "grafo.h"

struct verticeListaAdjacencia {
    int peso; //peso do v�rtice at� o pr�ximo
    struct verticeListaAdjacencia *prox;
};

typedef struct verticeListaAdjacencia Vertice;

struct ListaAdjacencia {
    Vertice *inicio;
};

typedef struct ListaAdjacencia Lista;

struct grafo {
    string nome; //nome do grafo
    int n; //n�mero de v�rtices
    int m; //n�mero de arestas
    Lista* lista; //lista de adjac�ncia
};

typedef struct grafo Grafo;
