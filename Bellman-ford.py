from math import inf;

graphe = {"A" :{"C": 1},
"B" : {"C" : 2, "E" : 3},
"C" : {"A" : 1, "B" : 2, "D" : 4, "E" : 3},
"D" : {"C" : 4},
"E" : {"C" : 3, "B" : 3},
"F" : {}
}

def Bellman_Ford(g,s):
    D={};
    for cle in graphe:
        D[cle]=inf
    D[s]=0;
    P={};
    i=0;
    for i in range(len(g)-1):
        for u in graphe:
            for v in graphe[u]:
                if D[v]>D[u]+graphe[u][v]:
                    D[v]=D[u]+graphe[u][v];
                    P[v]=u;
    
    for u in graphe:
        for v in graphe[u]:
            if D[v] > D[u]+graphe[u][v]:
                return False;
    return(D,P);


print(Bellman_Ford(graphe,"A"));
    
            
    