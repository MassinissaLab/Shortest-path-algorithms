# Implementation of dijkstra algorithm in Python3 
import string
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict 
MAX_INT = float('Inf') 
def minDistanced(dist, visited): 

    (minimum, minVertex) = (MAX_INT, 0) 
    for vertex in range(len(dist)): 
        if minimum > dist[vertex] and visited[vertex] == False: 
            (minimum, minVertex) = (dist[vertex], vertex) 

    return minVertex 
def Dijkstrad(graph, ma, src,h,p): 
    print(graph)
    Alphebt= list(string.ascii_uppercase)
    num_vertices = len(graph) 
    sptSet = defaultdict(lambda : False) 

    dist = [MAX_INT] * num_vertices 
    l = [None] * num_vertices
    l[src]=0
    dist[src] = 0
    h.extend(dist)
    for count in range(num_vertices): 
        
        curVertex = minDistanced(dist, sptSet) 
        sptSet[curVertex] = True
        
        for vertex in range(num_vertices):  
               
            if ((sptSet[vertex] == False) and (dist[vertex] > (dist[curVertex] +ma[curVertex][vertex])) and
                (ma[curVertex][vertex] != 0)):

                dist[vertex] = (dist[curVertex] +
                                ma[curVertex][vertex]);
                leng=len(p)
                i=0
                while i<leng and len(p)>0:
                    j=0
                    while j<leng and leng>0:
                        try:
                            if(p[i][1]==Alphebt[vertex]):
                                p.pop(p.index(p[i]))
                                leng-=1
                        except:
                            pass
                        j+=1
                    i+=1
                p.append((Alphebt[curVertex],Alphebt[vertex]))

        k=dist[:]
        l[curVertex]=dist[curVertex]
        k[curVertex]=str(k[curVertex])+"(*)"
        h.extend(k)
    h.extend(l)

def drawDijksraTabled(l,nbn,path,src):

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

    if(len(path)<nbn-1):
        k=k[:len(k)-2]+[k[len(k)-1]]
    
        

    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    Alphebt2= list(string.ascii_uppercase)
    Alphebt=["π(" + suit+")" for suit in Alphebt2]   
    Alphebt1=[x for x in range(1, 27)]
    k=[Alphebt[:nbn]]+k
    mp = ['k']+['0(init)']+Alphebt1[:len(k)-3]+[str(len(k)-2)+'(fin)']
    for i in range(0,len(k)):
        k[i]=[mp[i]]+k[i]
    colors = [["#F79862"]*len(k[1])]+[ ["#F79862"]+["w" for x in range(1,len(k[1]))] for x in range(1,len(k))  ]
    # Draw table
    the_table = plt.table(cellText=k,
                          colWidths=[0.1] * (nbn+1),
                          cellColours=colors,
                          loc='center')
    the_table.set_fontsize(12)
    fig.suptitle("Table de Dijkstra a partir de la source : "+str(Alphebt2[src]), fontsize=12)
    fig.savefig("Dijkstra_img/Table")             
def DrawDijksraGraphd(path,graph,src):
    G = nx.MultiDiGraph()
    n=len(graph[0])  
    Alphebt= list(string.ascii_uppercase)
    for i in range(n) :
        for j in range(n) :
            if graph[i][j] != 0 :
                G.add_edge(Alphebt[i],Alphebt[j], length = graph[i][j])

    pos = nx.circular_layout(G) 
    plt.clf()
    nx.draw(G, pos, with_labels = True,node_size=500)  #with_labels=true is to show the node number in the output graph
    edge_labels = dict([((u, v), d['length']) for u, v, d in G.edges(data = True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, label_pos = 0.5, font_size = 10)
    nx.draw_networkx_edges(G, pos,
                       edgelist= path ,
                       width=4, alpha=0.9, edge_color='r')
    nx.draw_networkx_nodes(G, pos,
                       node_color='#f45619',
                       node_size=500,
                       alpha=1)
    nx.draw_networkx_nodes(G, pos,
                       nodelist=path[0][0],
                       node_color='#00ade6',
                       node_size=600,
                       alpha=0.8)
    plt.savefig("Dijkstra_img/1DijksraGraph_"+str(src)+".png", format="PNG")



def createGraphd():
    Matriceaj=[]
    G = nx.DiGraph()
    f = open('dijkstra.txt')
    list1 = list(map(int, (f.readline()).split()))
    Matriceaj.append(list1)
    n=len(list1)
    for i in range(1,n):
        list1 = list(map(int, (f.readline()).split()))
        if(len(list1)==n):
            Matriceaj.append(list1)
    try:
        Alphebt= list(string.ascii_uppercase)

        for i in range(n) :
            for j in range(n) :
                if  Matriceaj[i][j] <0 :
                    print("il existe des valeurs négatives")
                    return None,None

                if Matriceaj[i][j] != 0 :
                    G.add_edge(Alphebt[i],Alphebt[j], length = Matriceaj[i][j])
        
    except :

        print("manque d'élemets dans la table d'adjacent")
        return None,None
    return G ,Matriceaj

    #draws the graph and displays the weights on the edges
def DrawGraphd(G):
    pos = nx.circular_layout(G) #position des noeuds
    plt.clf() #initialiser le plans
    nx.draw(G, pos, with_labels = True)  #dessiner le graphe
    edge_labels = dict([((u, v), d['length']) for u, v, d in G.edges(data = True)]) #les poids 
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, label_pos = 0.5, font_size = 10) #prints weight on all the edge
    nx.draw_networkx_nodes(G, pos,
                       node_color='#f45619',
                        alpha=1)
    plt.savefig('Dijkstra_img/0Graph_initiale.png', format="PNG")



