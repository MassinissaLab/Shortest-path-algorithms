# Implementation of Johnson's algorithm in Python3 
import string
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict 
MAX_INT = float('Inf') 

def BellmanFordbf(matrice_adj ,h ,src): 
    edges = [] 
    nbn=len(matrice_adj)
    for i in range(len(matrice_adj)): 
        for j in range(len(matrice_adj[i])): 
            if matrice_adj[i][j] != 0: 
                edges.append([i, j, matrice_adj[i][j]]) 
    dist = [MAX_INT] * (nbn ) 
    dist[src] = 0
    l = [None] * (nbn)
    l[src]=0
    h.extend(dist)
    for i in range(nbn): 
        for (src, des, weight) in edges: 
            if((dist[src] != MAX_INT) and (dist[src] + weight < dist[des])): 
                dist[des] = dist[src] + weight
                l[des]=dist[des]
                k=dist[:]
                h.extend(k)          
    h.extend(l)    
    return dist[0:nbn] 
def drawBellmanFordTablebf(l,nbn,src):
    k=[]
    i=0
    while i<len(l):
        k.append(l[i:i+nbn])
        i+=nbn
    for i in range(0,nbn):
        for j in range(0,len(k)-1):
            v=k[j][i]
            while  j+1<len(k)-1 :
                if(k[j+1][i]== v) :
                    k[j+1][i]=''
                j+=1
                pass
            pass
        pass
    r = [''] * nbn
    for j in range(1,nbn):
        for i in range(0,len(k)-1):
            if k[i]==r:
                k.pop(i)
    for j in range(0,nbn):
        for i in range(0,len(k)-1):
            if k[i][j]!='' and k[i][j]!=MAX_INT:
                k[i][j]=str(k[i][j])+"(*)"
    fig, ax = plt.subplots()

    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    Alphebt2= list(string.ascii_uppercase)
    Alphebt=["λ(" + suit+")" for suit in Alphebt2]   
    Alphebt1=[str(x) for x in range(1, 27)]

    k=[Alphebt[:len(k[1])]]+k
    mp = ['k']+['0(init)']+Alphebt1[:len(k)-3]+[str(len(k)-2)+'(fin)']
    
    for i in range(0,len(k)):
        k[i]=[mp[i]]+k[i]
    lt=len(k[1])
    colors = [["#F79862"]*(len(k[1]))]+[ ["#F79862"]+["w" for x in range(1,len(k[1]))] for x in range(1,len(k))  ]

    # Draw table
    the_table = plt.table(cellText=k ,
                          colWidths=[0.1] *(nbn+1),
                          cellColours=colors,
                          loc='center')
    
    the_table.set_fontsize(12)
    fig.suptitle("Table de Bellman Ford a partire de la racine :"+str(Alphebt2[src]), fontsize=12)
    fig.savefig("Bellf_img/Table.png")
def createGraphbf():#takes input from the file and creates a weighted graph
    wtMatrix=[]
    G = nx.DiGraph()
    f = open('bellmanford.txt')
    list1 = list(map(int, (f.readline()).split()))
    wtMatrix.append(list1)
    n=len(list1)
    for i in range(1,n):
        list1 = list(map(int, (f.readline()).split()))
        if(len(list1)==n):
            wtMatrix.append(list1)
    try:
        Alphebt= list(string.ascii_uppercase)
        for i in range(n) :
            for j in range(n) :
                if wtMatrix[i][j] != 0 :
                    G.add_edge(Alphebt[i],Alphebt[j], length = wtMatrix[i][j])
    except :
        return None,None
    return G ,wtMatrix

    #draws the graph and displays the weights on the edges
def DrawGraphbf(G):
    pos = nx.circular_layout(G) 
    plt.clf()
    plt.suptitle("Graphe initiale")
    nx.draw(G, pos, with_labels = True)  
    edge_labels = dict([((u, v), d['length']) for u, v, d in G.edges(data = True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, label_pos = 0.3, font_size = 14) #prints weight on all the edge
    nx.draw_networkx_nodes(G, pos,
                       node_color='#f45619',
                       node_size=500,
                       alpha=1)

    plt.savefig('Bellf_img/0Graph_initiale.png', format="PNG")


def DrawbfGraphdbf(G,mw,M,srcc):
    src=srcc
    l=[]
    
    
    
    
    srcs=[]
    mm=[]
    #successors=[]
    Alphebt= list(string.ascii_uppercase)

    for j in range(len(mw)):
        srcs.append([Alphebt[j],j])

    c=[x[0] for x in srcs if x[1]==srcc]
    otmp=[c[0]]
    
    paths(G,mw,srcc,l,otmp,srcs,mm)


    
    
    
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
                       alpha=0.9)

    nx.draw_networkx_nodes(G, pos,
                       nodelist=l[n][0],
                       node_color='#00ade6',
                       node_size=600,
                       alpha=0.8)
    
    
    plt.savefig("Bellf_img/Bellman_Ford.png", format="PNG")



def _paths(G,mw,srcc,l,otmp,srcs,mm):  #fonction récursive qui permet de récupérer les pcc de floyd-warshall
    
    for u in otmp[:] :
        if u not in mm:
            mm.append(u)
        
        
        tmp=[x for x in G.successors(u)]
        
        for s in tmp[:]:
            
            ori=[x[1]  for x in srcs if x[0]==u] #retourne l'indice du poid du noeud courant 
            fin=[x[1]  for x in srcs if x[0]==s] #retourne l'indice du poid du successeur
            i=ori[0]
            f=fin[0]
            
            if mw[f]-mw[i]== G[u][s]['length'] and s not in mm and (u,s) not in l:
                                
                l.append((u,s))
                tmp=tmp[1:]
                otmp=otmp+[s]
                

            if len(tmp)==0:

                otmp=otmp[1:]

    if otmp!=[] and otmp[-1] not in mm:
        _paths(G,mw,srcc,l,otmp,srcs,mm)    

def paths(G,mw,srcc,l,otmp,srcs,mm):

    _paths(G,mw,srcc,l,otmp,srcs,mm)
