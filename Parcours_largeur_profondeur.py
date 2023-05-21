
from collections import deque
from math import inf

graphe = {1 :{6},
     2 : {3, 5},
     3 : {1, 2, 4, 5},
     4 : {3},
     5 : {3, 2},
     6 : {2}
    }


def parcours_lageur():
        v=0
        file=deque()   
        file.append(1)
        distance=[]
        dict={};
        for i in range(len(graphe)):
            distance.append(inf)
        distance[file.index(1)]=0
        while len(file)!=0:
            v=file.pop()
            for parcour in graphe[v] :
                if(distance[parcour-1] == inf):
                    distance[parcour-1]=0;
                    distance[parcour-1]= distance[v-1]+1;
                    file.append(parcour)
                    dict[v]=parcour;
        return (distance,dict)


print(parcours_lageur());
                    
            
        