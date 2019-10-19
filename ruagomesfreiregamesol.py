import math
import pickle
import time
from itertools import product



class Lista:
  def __init__(self):
    self.myList=[]

seradesta=Lista()
class Node:
  def __init__(self, state, parent, g, tickets):
    self.state=state
    self.parent=parent
    self.tickets=tickets
    self.g=g
    self.h=1
    self.f=self.h+self.g
  
  def getTickets(self):
    return self.tickets

  
  def setParent(self, parent):
    self.parent=parent
  
  def getParent(self):
    return self.parent
  
  def setG(self, g):
    self.g=g

  def getG(self):
    return self.g
  
  def getF(self):
    return self.f
  
  def setH(self, h):
    self.h=h
  
  def getH(self, h):
    return self.h

  def setF(self):
    self.f=self.g+self.h
  
  def getState(self):
    return self.state

class State:
  def __init__(self,pos,goal,trans):
    self.pos=pos
    self.trans=trans
    self.goal=goal
    
  
  def setPos(self, lst):
    self.pos=lst
  
  def getPos(self):
    return self.pos
  
  def getTrans(self):
    return self.trans
  
  

class SearchProblem:

  def __init__(self, goal, model, auxheur = []):
    self.goal=goal
    self.model=model
    self.auxheur=auxheur
  
    


  def search(self, init, limitexp = 2000, limitdepth = 10, tickets = [math.inf,math.inf,math.inf]):
    n_agentes=len(init)
    initState=State(init,self.goal,[])
    InitNode=Node(initState,None,0,tickets)
    openList=[InitNode]
    searchSolution(n_agentes,InitNode,openList,self.goal,self.model)
      
    return seradesta.myList

def searchSolution(nagente,node,openList,goal,model):
  if(stateFinal(node,goal)==True):
    iterNode=node
    while(iterNode.getParent()!=None):
      seradesta.myList=seradesta.myList+[[iterNode.getState().getTrans(),iterNode.getState().getPos()]]
      iterNode=iterNode.getParent()
    return
  state=node.getState().getPos()
  lstaux=[]
  
  tickets=node.getTickets()
  if(nagente==3):
    for i in state:
      lstaux=lstaux+[model[i]]
    lstaux=list(product(*lstaux))     #cria todas as combinacoes possiveis
    listFinal = []
    for i in lstaux:
      listFinal=listFinal+[list(i)]  #converte os tuplos para lista para depois se puder eliminar o elemnto
    listFinal=eliminateStates(listFinal)  #elimina estados onde pelo menos 2 policias vao para o mesmo vertice
    
  else:
    listFinal = []
    for i in model[state[0]]:
      listFinal.append([i])
    
  if (tickets[0] != math.inf):
    listFinal=eliminateTickets(tickets,listFinal)
  
  openList.remove(node)
  for el in listFinal:
    pos=[]
    transport = []
    tickets = [-1]*(3)
    for element in el:
      pos=pos+[element[1]]
      transport = transport + [element[0]]  
      tic = node.getTickets()
      tickets[element[0]] = tic[element[0]] - 1 #lista de tickets utilizada
    state=State(pos,goal,transport)
    new_g=node.getG() + 1
    
    nNode = Node(state, node, new_g, tickets)
    openList.append(nNode)
    verify=stateFinal(nNode,goal)
    
    if(verify==True):
      iterNode=nNode
      while(iterNode.getParent()!=None):
          seradesta.myList=seradesta.myList+[[iterNode.getState().getTrans(),iterNode.getState().getPos()]]
          iterNode=iterNode.getParent()
      seradesta.myList=seradesta.myList+[[iterNode.getState().getTrans(),iterNode.getState().getPos()]]
      seradesta.myList.reverse()
      return
    
  
  minimo = openList[0].getF()
  minNode = openList[0]
  for nodeEval in openList:
    if (nodeEval.getF() < minimo):
      minNode = nodeEval
  
  searchSolution(nagente,minNode,openList,goal,model)

  

                 #elimina estados se nao houver bilhetes suficientes
def eliminateTickets(tickets,lst):
  z = 0
  while z<len(lst):
    auxTickets = tickets.copy()
    flag = 0
    for element in lst[z]:
      if(auxTickets[element[0]] > 0):
        auxTickets[element[0]] =  auxTickets[element[0]] - 1
      else:
        del lst[z]
        flag = 1
        break
    if (flag == 0):
      z = z + 1
  return lst

def eliminateStates(lstComb):
  z=0
  while z<len(lstComb):
      flag=0
      i=lstComb[z]
      for j in range(len(i)):
        for k in range(len(i)):
            if (k==j):
                continue
            else:
                if(i[k][1]==i[j][1]):
                    del lstComb[z]
                    flag=1
                    break

        if(flag==1):
          break
      if(flag == 0):
        z=z+1
          
                  
  return lstComb


def stateFinal(node,goal):

  if(node.getState().getPos()==goal):
    return True
  else:
    return False
  



  
  
