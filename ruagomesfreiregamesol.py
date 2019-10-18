import math
import pickle
import time
from itertools import product
  
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
    SolutionNode=searchSolution(n_agentes,InitNode,openList,self.goal,self.model)

    return []

def searchSolution( nagente,Node,openList,goal,model):
  if(stateFinal(Node,goal)==True):
    return Node
  
  state=Node.getState().getPos()
  lstaux=[]
  
  tickets=Node.getTickets()
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
    
  if (tickets[0] == math.inf):
    listFinal=eliminateTickets(tickets,listFinal)
  
  openList.remove(Node)
  for el in listFinal:
    state=[]
    transport = []
    tickets = []
    for element in el:
      state=state+element[1]
      transport = transport + element[0]  #lista de tickets utilizada
      tic = Node.getTickets()
      tickets = tic[element[0]] - 1
    nNode = Node(state, Node, Node.getg() + 1, tickets)
    openList.add(nNode)

  minimo = openList[0].getf()
  minNode = openList[0]
  for nodeEval in openList:
    if (nodeEval).getg() < minimo):
      minNode = nodeEval
    

  


     

    
  

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


def stateFinal(Node,goal):
  if(Node.getState().getPos()==goal):
    return True
  return False
  

class Node:
  def __init__(self, state, parent, g, tickets):
    self.state=state
    self.sucessores=[]
    self.parent=parent
    self.tickets=tickets
    self.g=g
    self.h=1
    self.f=self.h+self.g
  
  def getTickets(self):
    return self.tickets

  def setSucessores(self, lst):
    self.sucessores=lst

  def getSucessores(self):
    return self.sucessores
  
  def setParent(self, parent):
    self.parent=parent
  
  def getParent(self):
    return self.parent
  
  def setG(self, g):
    self.g=g

  def getg(self, G):
    return self.g

  def setH(self, h):
    self.h=h
  
  def getH(self, h):
    return self.h

  def setF(self):
    self.f=self.g+self.h
  
  def getState(self):
    return self.state




class Policia:
  def __init__(self, inic, tickets):
    self.pos_inic=inic
    self.actual_pos=inic
    
  
  
  def setPosition(self, newPos):
    self.actual_pos=newPos

  def getActualPosition(self):
    return self.actual_pos


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
  
  


  
  
