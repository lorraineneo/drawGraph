# https://github.com/lorraineneo/drawGraph.git
import graphviz

def generateTree(tree):
  
  def listtree(tree):
    '''
       Generates a list structure that represents the binary tree
       E.g.
           
             a
           /    \
         b       c
        / \     / \
       d   e   f   g
       
       ['a', ['b', ['d'], ['e']], ['c', ['f'], ['g']] ]
    '''
    sVal = []
    if tree:
        sVal.append(str(tree.getRootVal()))
        if tree.getLeft() != None:
          sVal.append(listtree(tree.getLeft()))

        if tree.getRight() != None:
          sVal.append(listtree(tree.getRight()))
    return sVal

  def add_edge(graph, source, dest):
    graph.edge(source, dest)
    

  def first_flat(tree):
    if isinstance(tree, list):
      return first_flat(tree[0])
    else:
      return tree

  def find_edges(graph, tree):
    if isinstance(tree, list):
      source = tree[0]
      graph.node(source)
      for dest in tree[1:]:
        add_edge(graph,source, first_flat(dest))
        find_edges(graph, dest)

  if tree:
    exptree = listtree(tree) #converts Binary Tree to a list structure first
    graph = graphviz.Digraph()
    find_edges(graph, exptree)
    return graph
  else:
    return graphviz.Digraph()
