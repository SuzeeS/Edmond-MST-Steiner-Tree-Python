
#Implementation of Steiner Tree Problem on a directed graph for finding out the maximum weighted spanning subtree of a given directed graph in graphml format

import networkx as nx
import threading
import os
import random
import operator
import pandas as pd
from collections import namedtuple
Arc = namedtuple('Arc',('tail', 'weight', 'head'))   #namedtuple for storing the destination, edge weight and source of every arc  
os.chdir('C:/Users/Soma/Desktop/Weights/W1')                     
a=list(os.listdir())                                 #listing down the pathnames of the graphml files
subgraph=[]                                          #list for storing the path,list of selected nodes,edge sequence and total weight of the maximum spanning subtree
graph=[]                                             #list for storing the path,edge sequence and total weight of the maximum spanning arborescence
ch=0


#Function submax removes a list of conflicting nodes and their adjacent edges from the original graph  using an ad hoc method in order to form a maximum spanning subtree.
#A conflicting node is one having the same chunk number as the node and whose starting or ending position indices overlap with that node.
#The ad hoc method refers to the attributes(namely chunk number, position id and length of the word) of every node of a particular graphml file

def submax(G,paths):
    node_list=list(G.nodes())
    len_d=len(node_list)
    #Extracting the attributes from the graphml file
    dy=nx.get_node_attributes(G,'chunk_no')   
    ds=nx.get_node_attributes(G,'position')
    dt=nx.get_node_attributes(G,'length_word')
    #calcuating the final position index of every node
    df={key:(ds[key]+dt[key]-1) for key in ds} 
    #Extracting the weight of every edge
    w=nx.get_edge_attributes(G,'weight')                       
    arcs=[]
    for (u,v) in G.edges():
       y=G[u][v]['weight']
       u=int(u)
       v=int(v)
       arcs.append(Arc(v,y,u))   #the list arcs stores the destination, edge weight and source of every arc as a named tuple
    bestInEdge={}                #dictionary  mapping every node to its maximum weighted incoming arc
    z={}
    temp=[]
    #looking for the maximum weighted incoming arc for every node
    for i in range(0,len_d):
        temp.clear()
        n=int(node_list[i])
        for arc in arcs:
            if arc.tail==n:
                temp.append(arc)   #storing all the incoming arcs of every node
        z[n]=temp
        if  len(z[n])!=0:
            bestInEdge[n]=max(z[n])        #storing the maximum weighted incoming arc of every node
    d = sorted(bestInEdge.values(), key=operator.itemgetter(1))            #sorting the nodes on the basis of their maximum weighted incomimg arc
    contradict={}                                      #dictionary mapping every node to a list of conflicting nodes.
    for n in node_list:
        c=dy[str(n)]
        s=ds[str(n)]
        f=df[str(n)]
        for node in node_list:
             c1=dy[str(node)]
             s1=ds[str(node)]
             f1=df[str(node)]
             if node!=n and c==c1 :                                        #identifying the conflicting nodes
                if (s1>=s and s1<=f) or (f1>=s and f1<=f):                 #A conflicting node is one having the same chunk number as the node and whose starting or ending position indices overlap with that node.
                    contradict.setdefault(int(n),[]).append(int(node))     #appending a list of conflicting nodes corresponding to every node of the graph
    for k in node_list:
        if int(k) not in contradict:
            contradict[int(k)]=[]                     
    key_list=[]
    #list storing the nodes in the descending order of their maximum weighted incoming arc 
    for arc in d:
        key_list.append(arc.tail)      
    key_list.reverse()
    #removing the conflicting nodes from the contradict dictionary
    for i in key_list:
        if i in contradict:
            b=contradict[i]
            for x in b:
                if x in contradict:
                    del contradict[x]         #removing all the conflicting nodes corresponding to a particular node from the Contradict dictionary
    spanned=[i for i in contradict.keys()]       #storing a list of all the non-conflicting nodes                              
    rem=[]
    for i in node_list:
        if int(i) not in spanned:
            rem.append(int(i))        #storing a list of conflicting nodes
    #Creating a subgraph from the non-conflicting nodes
    X=nx.DiGraph()                                      
    X=G
    for i in rem:
        X.remove_node(str(i))         #removing the conflicting nodes and their adjacent edges from the original graph to form the subgraph
                                                                        
    try:
        H=nx.maximum_spanning_arborescence(X)  #forming a maximum spanning arborescence from the subgraph
        s=0
        p=[]
        #calculating the weight of the maximum spanning subtree
        for (u,v) in H.edges(): 
            w=H[u][v]['weight']
            s=s+w
            p.append((u,v,w))
        subgraph.append((paths,spanned,p,s))   #storing the path,edge sequence and total weight of the maximum spanning subtree                             
    except:
        D=nx.Graph()
        D=X.to_undirected()
        l=sorted(nx.connected_components(D), key = len, reverse=True)  #Storing the connected components of the disconnected graphs formed using the non conflicting nodes
        #Selecting the connected component with greater number of nodes
        k=list(l[0])                                                    
        if(len(k)!=0):
            for i in spanned:
                if str(i) not in  k:
                    X.remove_node(str(i))      #removing the nodes of the disconnected components  
        H=nx.maximum_spanning_arborescence(X)  #forming a maximum spanning arborescence from the subgraph
        s=0
        p=[]
        #calculating the weight of the maximum spanning subtree
        for (u,v) in H.edges(): 
            w=H[u][v]['weight']
            s=s+w
            p.append((u,v,w))
        subgraph.append((paths,k,p,s))   #storing the path,edge sequence and total weight of the maximum spanning subtree   
        return
 

def smst(G,x):  
    g=[]
    M=nx.maximum_spanning_arborescence(G)  #Finding out a maximum spanning arborescence from a directed and weighted graph
    sum=0
    for (u,v) in M.edges():
         w=M[u][v]['weight']
         u=int(u)
         v=int(v)
         sum=sum+w
         g.append((u,v,w))
    graph.append((x,g,sum))     

def weighted_graph(G):
    score=[]
    #assigning weights to the edges of the graph
    for (u,v) in G.edges():
        w=random.randint(1,25)           
        score.append(tuple([u,v,w])) 
    G.add_weighted_edges_from(score)  #adding weight as an attribute to the graph   
    return(G)


def working(start,end):
    l=a[start:end]          #storing a list of pathnames of the graphml files
    for i in range(0,len(l)):    
        x=l[i]
        G=nx.read_graphml(x)   #reading a graph in graphml file from the path x
        G=weighted_graph(G)
        print(i)
        ch=1
        if(ch==0):
            smst(G,x)  #finds a maximum spanning arborescence
        elif(ch==1):
            submax(G,x)  #finds a maximum spanning subtree using an ad hoc method
            
def create_table1():
    #storing the path,edge sequence and total weight of the maximum spanning arborescence in a CSV
    df=pd.DataFrame(columns= ['Graphs','Edge Sequence(Source,Destination,Weight)','Total Weight']) 
    for i in range(0,len(graph)):
        df.loc[i]=[graph[i][0],graph[i][1],graph[i][2]]
    df.to_csv("graph.csv")                
def create_table2():
    #storing the path,list of selected nodes,edge sequence and total weight of the maximum spanning subtree in a CSV
    df=pd.DataFrame(columns= ['Graphs','Selected Nodes','Edge Sequence(Source,Destination,Weight)','Total Weight'])
    for i in range(0,len(subgraph)):
        df.loc[i]=[subgraph[i][0],subgraph[i][1],subgraph[i][2],subgraph[i][3]]
    df.to_csv("sub.csv")  
def myfunct():
    start=0
    end=250
    i=0
    #implementation of threads 
    #parallelly executing 20 sets of 250graphml files for faster execution 
    for i in range(0,4):
        for t in range(0,10):
            t=threading.Thread(target=working,args=(start,end))
            start=end
            end=start+250
            t.start()
        t.join()
        

#ch=input('Enter your choice:\n0->Maximum Spanning Arborescence\n1->Maximum Spanning Subtree using an Ad hoc method')    
myfunct()
create_table1()
create_table2()
