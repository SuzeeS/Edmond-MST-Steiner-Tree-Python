import pdb
from collections import defaultdict, namedtuple
Arc = namedtuple('Arc', ('tail', 'weight', 'head'))             
def min_spanning_arborescence(arcs, sink):
    #print('\n\nMinimum Spanning Arborescence')
    good_arcs = []
    quotient_map = {arc.tail: arc.tail for arc in arcs}         #dictionary for tail(key) to tail(value) mapping of every arc
    quotient_map[sink] = sink                                   
    #print(quotient_map.values())
    while True:
        min_arc_by_tail_rep = {}                                #dictionary storing the minimum incoming arc(value) of every node(key) 
        successor_rep = {}                                      #dictionary storing the parent node of every node selected in min_arc_by_tail_rep
        for arc in arcs:                     
            if arc.tail == sink:                                #avoiding the arcs which have root as their tail
                continue
            tail_rep = quotient_map[arc.tail]            
            head_rep = quotient_map[arc.head]
            if tail_rep == head_rep:                            #avoiding self loops
                continue
            if tail_rep not in min_arc_by_tail_rep or min_arc_by_tail_rep[tail_rep].weight > arc.weight:   #selecting the minimum incoming arc for every node
                min_arc_by_tail_rep[tail_rep] = arc                                                        #updating the dictionary for the minimum incoming arc and the successor dictionary accordingly
                successor_rep[tail_rep] = head_rep
#        print('Successor1',successor_rep)        
        cycle_reps = find_cycle(successor_rep, sink)                                                       #detecting cycles amongst the arcs stored in min_arc_by_tail_rep 
#        print('Cycles found ', cycle_reps,'\n')
        if cycle_reps is None:
            good_arcs.extend(min_arc_by_tail_rep.values())                                                 #storing the minimum incoming arcs of every node before and after merging
#            print('Good Arcs',good_arcs)
            return spanning_arborescence(good_arcs, sink)                                               
        good_arcs.extend(min_arc_by_tail_rep[cycle_rep] for cycle_rep in cycle_reps)                       #keeping a track of the arcs forming a cycle
#        print('Good Arcs',good_arcs) 
        cycle_rep_set = set(cycle_reps)                                                                     
#        print('Set formed',cycle_rep_set)
        cycle_rep = cycle_rep_set.pop()                                                                    
#        print('Popped Element:',cycle_rep)
        quotient_map = {node: cycle_rep if node_rep in cycle_rep_set else node_rep for node, node_rep in quotient_map.items()}   #merging the nodes forming a cycle by updating their arc.tail values in the dictionary
#        print('QMap', quotient_map.items())
       
def max_spanning_arborescence(arcs, sink):
#    print('\n\nMaximum Spanning Arborescence')
    pdb.set_trace()
    good_arcs = []
    quotient_map = {arc.tail: arc.tail for arc in arcs}
    quotient_map[sink] = sink
#    print(quotient_map.values())
    while True:
        max_arc_by_tail_rep = {}                                                                            #dictionary storing the maximum incoming arc(value) of every node(key)  
        successor_rep = {}                                                                                  #dictionary storing the parent node of every node selected in max_arc_by_tail_rep
        for arc in arcs:
            if arc.tail == sink:
                continue
            tail_rep = quotient_map[arc.tail]
            head_rep = quotient_map[arc.head]
            if tail_rep == head_rep:
                continue
            if tail_rep not in max_arc_by_tail_rep or max_arc_by_tail_rep[tail_rep].weight < arc.weight:    #selecting the maximum incoming arc for every node
                max_arc_by_tail_rep[tail_rep] = arc                                                         #updating the dictionary for the maximum incoming arc and the successor dictionary accordingly

                successor_rep[tail_rep] = head_rep
#        print('Successor1',successor_rep)        
        cycle_reps = find_cycle(successor_rep, sink)
#        print('Cycles found ', cycle_reps,'\n')
        if cycle_reps is None:
            good_arcs.extend(max_arc_by_tail_rep.values())                                                  #storing the maximum incoming arcs of every node before and after merging
#            print('Good Arcs',good_arcs)
            return spanning_arborescence(good_arcs, sink)
        good_arcs.extend(max_arc_by_tail_rep[cycle_rep] for cycle_rep in cycle_reps)
#        print('Good Arcs',good_arcs) 
        cycle_rep_set = set(cycle_reps)
#        print('Set formed',cycle_rep_set)
        cycle_rep = cycle_rep_set.pop()
#        print('Popped Element:',cycle_rep)
        quotient_map = {node: cycle_rep if node_rep in cycle_rep_set else node_rep for node, node_rep in quotient_map.items()}#merging the nodes forming a cycle by updating their arc.tail values in the dictionary
#        print('QMap', quotient_map.items())        

def find_cycle(successor, sink):
#    print('Successor=',successor)
    visited = {sink}
    for node in successor:
#        print('Node =',node,'\n' )
        cycle = []
        while node not in visited:
            visited.add(node)                                                                                 #keeping a track of the traversed nodes
            cycle.append(node)                                                               
            node = successor[node]                                                                            #if the node's parent is present in the list 'cycle',it verifies the presence of a cycle 
        if node in cycle:
            return cycle[cycle.index(node):]
    return None


def spanning_arborescence(arcs, sink):                                                     #arcs stores the list of arcs in good_arcs                                                
    arcs_by_head = defaultdict(list)                                                         
    for arc in arcs:                                                                        
        if arc.tail == sink:
            continue   
        arcs_by_head[arc.head].append(arc)                                                  #dictionary mapping  every arc.head to its corresponding arc  
#    print('Arc by heads',arcs_by_head)    
    solution_arc_by_tail = {}
    stack = arcs_by_head[sink]                                                              #selecting the arc starting from the root node
#    print('StackValues',stack)
    while stack:
        arc = stack.pop(0)                                                                  #popping the elements from the beginning of the list 'stack'
        if arc.tail in solution_arc_by_tail:
            continue
        solution_arc_by_tail[arc.tail] = arc                                                #storing the final selected arc for every node                                                
        stack.extend(arcs_by_head[arc.tail])                                                #tracking the head of the selected node in order to move forward in the graph 
#        print('StackValues',stack)
   # print ('Solution:\n',solution_arc_by_tail)

def options(arcs,sink):
    q_map1=[ arc.head for arc in arcs]                                                   #detecting the graphs which have atleast one non-root node with no incoming egde
    a=set(q_map1)
    #print('heads',a)
    q_map2=[arc.tail for arc in arcs]
    b=set(q_map2)
    #print('tails',b)    
    k=1
    for x in a:
        if x in a and x not in b and x is not sink :
            #print('Graph does not have an arborescence')
            k=0
    if k==1:
       # print('\n1.Minimum Spanning Tree\n2.Maximum Spanning Tree')
        #min_spanning_arborescence(arcs,sink)
        max_spanning_arborescence(arcs,sink)        
        
        
    
    
options([Arc(1,1,0),Arc(2,2,0),Arc(3,3,0),Arc(2,4,1),Arc(3,1,2),Arc(4,7,3),Arc(3,6,4),Arc(1,5,2)],0)              #Graph 1 :Graph with more than one cycles 
#options([Arc(1,5,0),Arc(2,1,0),Arc(3,1,0),Arc(2,11,1),Arc(3,4,1),Arc(3,5,2),Arc(1,10,2),Arc(1,9,3),Arc(2,8,3)],0) #Graph 2:Graph with more than one cycles        
#options([Arc(2 ,1,1),Arc(3,3,2),Arc(5,4,3),Arc(6,3,5),Arc(5,2,4),Arc(5,1,2),Arc(4,1,7),Arc(1,2,4),Arc(4,1,3)],7)  #Graph 3:Changing the root node of Graph 1 gives us a different spanning arborescence          
#options([Arc(2,5,1),Arc(1,-2,2),Arc(2,-3,3),Arc(4,-4,1),Arc(2,7 ,4),Arc(4,9,3),Arc(3,8,1),Arc(1,6,0),Arc(3,7,0)],0)#Graph 4:Graph with negative edges
#options([Arc(1, 9, 0), Arc(2, 10, 0), Arc(3, 9, 0), Arc(2, 20, 1), Arc(3, 3, 1), Arc(1, 30, 2), Arc(3, 11, 2), Arc(2, 0, 3), Arc(1,30, 3)], 0)#Graph 5:On reversing all the edges of the graph we do not get a spanning arborescence
#options([Arc(1,5,0),Arc(2,5,0),Arc(3,5,0),Arc(4,5,0),Arc(0,6,1),Arc(2,6,1),Arc(3,6,1),Arc(4,6,1),Arc(0,7,2),Arc(1,7,2),Arc(3,7,2),Arc(4,7,2),Arc(0,8,3),Arc(1,8,3),Arc(2,8,3),Arc(4,8,3),Arc(0,9,4),Arc(1,9,4),Arc(2,9,4),Arc(3,9,4)],0) #Graph 5 : Complete graph of 5 nodes              
#options([Arc(0,10,0),Arc(1,9,1),Arc(2,10,2)],0)                                                                    #Graph 6 : Fails to give an arborescence for a null or disconnected graph
