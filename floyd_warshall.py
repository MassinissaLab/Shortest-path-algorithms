import networkx as nx
import matplotlib.pyplot as plt
import sys
import string
from collections import defaultdict 

def info(f):
    max=0
    f = open('floyd.txt')
    list2= list(map(int, (f.readline()).split()))

    n = len(list2)
    if  max < list2[0]:
       max = list2[0]
    for i in range (n-1):
        list2 = list(map(int, (f.readline()).split())) 
        if  max < list2[i]:
            max = list2[i]
    return max,n
def FloydWarshall():
    src=0
    f = open('floyd.txt')
    max,n=info(f)
    inf = float("inf")
    wtMatrix = []
    #Remplire les données dans la matrice depuis le fichier input dans la latrice list1
    try:  
        for i in range(n):
            list1 = list(map(int, (f.readline()).split()))
            for i in range (len(list1)):
                if  list1[i]==max:
                    list1[i]=inf
            wtMatrix.append(list1)
    except:
        print("manque des élemets dans la table d'adjacent")


    DrawFloyd(wtMatrix,n,src)
    G=CreateGraphFloyd(wtMatrix,n)
    DrawInit(G)
    src+=1
    # appliquer Floyd Warshall  sur la matrice
    for k in range(n):
        for i in range(n):
            for j in range (n):
                
                if wtMatrix[i][j]>wtMatrix[i][k]+wtMatrix[k][j]:
                    wtMatrix[i][j]=wtMatrix[i][k]+wtMatrix[k][j]
                    
        ff=open("output.txt","w")
        ff.write(str(wtMatrix))
        DrawFloyd(wtMatrix,n,src)
        
        src+=1
        ff.close()
    Lst=dict([((u, v), d['length']) for u, v, d in G.edges(data = True)])
    
    for src in range(n):

        DrawGraphFloyd(G,wtMatrix,src)
        

    f.close()
    return n
    
    
def DrawFloyd(l,nbn,src):
    k=l[0:nbn] 
    fig, ax = plt.subplots()

    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    # Draw table
    the_table = plt.table(cellText=k,colWidths=[0.1] * nbn,loc='center')
    the_table.auto_set_font_size(False)
    the_table.scale(2, 1.5)
    the_table.set_fontsize(12)
    for key, cell in the_table.get_celld().items():
        cell.set_linewidth(0)
    fig.suptitle("Floyd Warshall matrice "+str(src), fontsize=12)
    fig.savefig("Floyd_img/Table_Floyd"+str(src)+".png")

def CreateGraphFloyd(M,n):
    G = nx.DiGraph()
    Alphebt= list(string.ascii_uppercase)
    for i in range(n) :
        for j in range(n) :
            if i!=j and  M[i][j] !=float('inf'):
                    G.add_edge(Alphebt[i],Alphebt[j], length = M[i][j])
    
    return G
    
def DrawGraphFloyd(G,M,k):
    
    
    src=k
    l=[]
    srcs=[]
    Alphebt= list(string.ascii_uppercase)

    for j in range(len(M)):
        srcs.append([Alphebt[j],j])

    o=[x[0] for x in srcs if x[1]==k]

    
    
    os=o[0]

    
    otmp=[os]
    
    mm=[]
    paths(G,M,k,l,otmp,srcs,mm) #appel de la fonction récursive pour déssiner les pcc 
                

    
    
    c=[x[0] for x in srcs if x[1]==k]
    
    n=0

    while n<len(l)and l[n][0]!=c[0]:
         n+=1
   
   
    pos = nx.circular_layout(G) 
    plt.clf()
    nx.draw(G, pos, with_labels = True,node_size=500)  #with_labels=true is to show the node number in the output graph
    edge_labels = dict([((u, v), d['length']) for u, v, d in G.edges(data = True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, label_pos = 0.3, font_size = 14)
    nx.draw_networkx_edges(G, pos,edgelist=l  ,width=4, alpha=0.9, edge_color='r')
    nx.draw_networkx_nodes(G, pos,
                       node_color='#f45619',
                       node_size=500,
                       alpha=1)

    nx.draw_networkx_nodes(G, pos,
                           nodelist=l[n][0],
                           node_color='#00ade6',
                           node_size=600,
                           alpha=0.8)
                    
    
    plt.savefig("Floyd_img/FloydGraph"+str(k)+".png", format="PNG")

def _paths(G,M,k,l,otmp,srcs,mm):  #fonction récursive qui permet de récupérer les pcc de floyd-warshall
    
    for u in otmp[:] :
        if u not in mm:
            mm.append(u)
        
        
        tmp=[x for x in G.successors(u)]
        
        for s in tmp[:]:
            
            ori=[x[1]  for x in srcs if x[0]==u] #retourne l'indice du poid du noeud courant 
            fin=[x[1]  for x in srcs if x[0]==s] #retourne l'indice du poid du successeur
            i=ori[0]
            f=fin[0]
            
            if(M[k][i]+G[u][s]['length']==M[k][f]) and s not in mm and (u,s) not in l:
                                
                l.append((u,s))
                tmp=tmp[1:]
                otmp=otmp+[s]
                

            if len(tmp)==0:

                otmp=otmp[1:]

    if otmp!=[] and otmp[-1] not in mm:
        _paths(G,M,k,l,otmp,srcs,mm)    

def paths(G,M,k,l,otmp,srcs,mm):

    _paths(G,M,k,l,otmp,srcs,mm)



def DrawInit(G):
    plt.clf()
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels = True,node_size=500)  #with_labels=true is to show the node number in the output graph
    edge_labels = dict([((u, v), d['length']) for u, v, d in G.edges(data = True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, label_pos = 0.3, font_size = 11) #prints weight on all the edges
    nx.draw_networkx_nodes(G, pos,
                   node_color='#f45619',
                   node_size=500,
                   alpha=1)
    plt.savefig('Floyd_img/ainitFloyd.png', format="PNG") 

