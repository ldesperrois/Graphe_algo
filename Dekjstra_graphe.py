from math import inf


graphe = {"A" :{"C": 1},
"B" : {"C" : 2, "E" : 3},
"C" : {"A" : 1, "B" : 2, "D" : 4, "E" : 3},
"D" : {"C" : 4},
"E" : {"C" : 3, "B" : 3},
"F" : {}
}

def minimum(d):
    mini=inf
    val=-1
    for cle in d:
        if d[cle]<mini:
            mini=d[cle]
            val=cle
    
    return val;



def Dijkstra(graphe,V):
    D = {};
    d = {};
    v="";
    for cle in graphe:
        
        if cle==V:
            d[cle]=0;
        else:
            d[cle]=inf;
    while(d!={}):
        if(V==-1):
            while(d!={}):
                for par in graphe:
                    if(par not in D):
                        d.pop(par);
                        D[par]="Noeud_Isolé";
        else:          
            for parcour in graphe[V]:
                if parcour not in D and d[parcour]>graphe[V][parcour]+d[V] :
                    d[parcour]=graphe[V][parcour]+d[V];
        
            a=d.pop(V);
            D[V]=a;
            V=minimum(d);
    return D;
    
def main():
    reponse=str(input("donnez une lettre entre A et F pour effectuer l'algorithme de Dijkstra"));
    resultat=Dijkstra(graphe,reponse);
    for parcour in resultat :
        if resultat[parcour]=="Noeud_Isolé":
            print("Ce noeud est isolé");
            break;
        elif parcour!=reponse:
            print("la distance minimum entre",reponse,"et",parcour,"est de ",resultat[parcour]);
        
            
            
            
                
    
main();
    
    
    
