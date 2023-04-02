    
from collections import deque

graphe = {1  :{4},
          2 : {3, 5,6},
          3 : {2, 4, 5,1},
          4 : {3},
          5 : {3, 2},
          6 : {2}
          }




def connexe(g):    #Le graphe est t'il connexe?
    
    retourner=False;
    Q=deque();
    Q.append(1);
    D = [0 for i in range(len(g))];
    c=1;
    while (len(Q)!=0):
        v=Q.pop();
        for w in g[v]:
            if((D[w-1]==0)):
                D[w-1]=1;
                c=c+1;
                Q.append(w);

    if(c==len(g)):
        retourner=True; 
    return retourner;
    

def cycles(g,destination):                     #le graphe possède t'il un cycle ?
    cycle=False;
    D= [0 for i in range(len(g))];
    Q=deque();   							#liste des sommets visités  . 
    Q.append(destination);
    desti_final=destination;
    destination=-1;
    while(cycle==False and len(Q)!=0):
        v=Q.pop();
        for w in g[v]:
            print(w)
            if(w==desti_final):
                cycle=True;
                break;
            else:
                Q.append(w);
    if (destination==desti_final):
        cycle=True;
    return cycle;
        
                



print((cycles(graphe,1)))
