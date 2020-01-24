# Implementation of Johnson's algorithm in Python3 
import string
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from collections import defaultdict 
MAX_INT = float('Inf') 
def minDistance(dist, visited): 

    (minimum, minVertex) = (MAX_INT, 0) 
    for vertex in range(len(dist)): 
        if minimum > dist[vertex] and visited[vertex] == False: 
            (minimum, minVertex) = (dist[vertex], vertex) 

    return minVertex 
def Dijkstra(graph, modifiedGraph, src,h,p): 
    Alphebt= list(string.ascii_uppercase)
    num_vertices = len(graph) 
    sptSet = defaultdict(lambda : False) 

    dist = [MAX_INT] * num_vertices 
    l = [None] * num_vertices
    l[src]=0
    dist[src] = 0
    h.extend(dist)
    for count in range(num_vertices): 
        curVertex = minDistance(dist, sptSet) 
        sptSet[curVertex] = True
        for vertex in range(num_vertices):      
            if ((sptSet[vertex] == False) and
                (dist[vertex] > (dist[curVertex] +
                modifiedGraph[curVertex][vertex])) and
                (graph[curVertex][vertex] != 0)):

                dist[vertex] = (dist[curVertex] +
                                modifiedGraph[curVertex][vertex]);
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

      

    

def BellmanFord(edges, graph, num_vertices,h): 

    # Add a source s and calculate its min 
    # distance from every other node 
    dist = [MAX_INT] * (num_vertices + 1) 
    dist[num_vertices] = 0
    l = [None] * (num_vertices+1)
    l[num_vertices]=0
    
 
    h.extend(dist)

    for i in range(num_vertices): 
        edges.append([num_vertices, i, 0]) 
    
    for i in range(num_vertices): 
        for (src, des, weight) in edges: 
            if((dist[src] != MAX_INT) and (dist[src] + weight < dist[des])): 
                dist[des] = dist[src] + weight
                l[des]=dist[des]
                k=dist[:]
                
        h.extend(k)
                 
    h.extend(l)    

    # Don't send the value for the source added 
    return dist[0:num_vertices] 
def JohnsonAlgorithm(graph): 
    
    edges = [] 
    nbn=len(graph)
    # Create a list of edges for Bellman-Ford Algorithm 
    for i in range(len(graph)): 
        for j in range(len(graph[i])): 

            if graph[i][j] != 0: 
                edges.append([i, j, graph[i][j]]) 

    # Weights used to modify the original weights 
    h=[]
    modifyWeights = BellmanFord(edges, graph, len(graph),h) 
  
    drawBellmanFordTable(h,nbn+1)
    modifiedGraph = [[0 for x in range(len(graph))] for y in range(len(graph))] 
    # Modify the weights to get rid of negative weights 
    for i in range(len(graph)): 
        for j in range(len(graph[i])): 
            if graph[i][j] != 0: 
                modifiedGraph[i][j] = (graph[i][j] +
                        modifyWeights[i] - modifyWeights[j]); 

    
    
    # Run Dijkstra for every vertex as source one by one 
    
                
                
    for src in range(len(graph)):
        path=[] 
        h=[]
        Dijkstra(graph, modifiedGraph, src,h,path)

        drawDijksraTable(h,nbn,src)
        DrawDijksraGraph(path,graph,src)
    return (modifiedGraph)  
def drawDijksraTable(l,nbn,src):
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
    fig.suptitle("Table de Dijkstra a partire de la racine : "+str(Alphebt2[src]), fontsize=12)
    fig.savefig("Johnson_img/Table_"+str(src))            

def DrawDijksraGraph(path,graph,src):
    G = nx.MultiDiGraph()
    n=len(graph[0])  
    Alphebt= list(string.ascii_uppercase)
    for i in range(n) :
        for j in range(n) :
            if graph[i][j] != 0 :
                G.add_edge(Alphebt[i],Alphebt[j], length = graph[i][j])

    pos = nx.circular_layout(G) 
    plt.clf()
    plt.suptitle("Graphe de Dijksra a partire de la racine : "+str(Alphebt[src]))
    nx.draw(G, pos, with_labels = True,node_size=500)  #with_labels=true is to show the node number in the output graph
    edge_labels = dict([((u, v), d['length']) for u, v, d in G.edges(data = True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, label_pos = 0.3, font_size = 14)
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
    plt.savefig("Johnson_img/DijksraGraph_"+str(src)+".png", format="PNG")


def drawBellmanFordTable(l,nbn):
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


    
    k=[Alphebt[:len(k[1])-1]+['λ(Q°)']]+k
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
    fig.suptitle("Table de Bellman Ford a partire de la racine : Q ", fontsize=12)
    fig.savefig("Johnson_img/aTable_BellmanFord")


def createBellmanFordGraph1(ma,ma1):
    G = nx.MultiDiGraph()
    n=len(ma[0])  
    Alphebt= list(string.ascii_uppercase)
    for i in range(n) :
        for j in range(n) :
            if ma1[i][j] != 0 :
                G.add_edge(Alphebt[i],Alphebt[j], length = ma[i][j])
    return G  
def createBellmanFordGraph(ma,ma1):
    G = nx.MultiDiGraph()
    n=len(ma[0])  
    Alphebt= list(string.ascii_uppercase)
    for i in range(n) :
        for j in range(n) :
            if ma1[i][j] != 0 :
                G.add_edge(Alphebt[i],Alphebt[j], length = ma[i][j])
    for i in range(n) :
        G.add_edge('Q°',Alphebt[i], length = 0)
    return G    
def DrawBellmanFordGraph(G,m): 
    pos = nx.circular_layout(G) 
    Alphebt= list(string.ascii_uppercase)
    path=[]
    for i in range(len(m)) :
        path.append(('Q°',Alphebt[i]))
    plt.clf()
    plt.suptitle("Graphe de Bellman Ford avec le sommet Q°")
    nx.draw(G, pos, with_labels = True)  #with_labels=true is to show the node number in the output graph
    edge_labels = dict([((u, v), d['length']) for u, v, d in G.edges(data = True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, label_pos = 0.7, font_size = 14) #prints weight on all the edges
    collection=nx.draw_networkx_edges(G, pos,edgelist= path , width=3, alpha=1, edge_color='w')
    nx.draw_networkx_nodes(G, pos,
                       node_color='#f45619',
                       node_size=500,
                       alpha=1)
  
    for patch in collection:
        patch.set_linestyle('dotted')
        

    plt.savefig('Johnson_img/aGraph_BellmanFord1.png', format="PNG")
def DrawBellmanFordGraph1(G): 
    pos = nx.circular_layout(G) 
    plt.clf()
    plt.suptitle("Graphe de Bellman Ford aprés MAJ des poids")
    nx.draw(G, pos, with_labels = True)  #with_labels=true is to show the node number in the output graph
    edge_labels = dict([((u, v), d['length']) for u, v, d in G.edges(data = True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, label_pos = 0.3, font_size = 14) #prints weight on all the edges
    nx.draw_networkx_nodes(G, pos,
                   node_color='#f45619',
                   node_size=500,
                   alpha=1)
    plt.savefig('Johnson_img/aGraph_BellmanFord2.png', format="PNG")
def createGraph():#takes input from the file and creates a weighted graph
    wtMatrix=[]
    G = nx.DiGraph()
    f = open('johnson.txt')
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
def DrawGraph(G):

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
    
    plt.savefig('Johnson_img/0Graph_initiale.png', format="PNG")

