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
    initState=State(init,self.goal,[])
    InitNode=Node(initState,None,0,tickets)
    openList=[InitNode]
    SolutionNode=searchSolution(InitNode,openList,self.goal,self.model)


    return []

def searchSolution(Node,openList,goal,model):
  if(stateFinal(Node)==True):
    return Node
  
  state=Node.getState().getPos()
  lstaux=[]
  for i in state:
    lstaux=lstaux+model[i]

  lstaux=list(product(*lstaux))     #cria todas as combinacoes possiveis
  
  lstComb=[]
  for i in lstaux:
    lstComb=lstComb+[list(i)]       #converte os tuplos para lista para depois se puder eliminar o elemnto
  
  lstEliminateStates=eliminateStates(lstComb)          #elimina estados onde pelo menos 2 policias vao para o mesmo vertice


    

def eliminateStates(lstComb):
  q=0;
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
      else:
          z=z+1
          
                  
  return lstComb


def stateFinal(Node,goal):
  if(Node.getState().getPos()==goal):
    return True
  return False
  

class Node:
  def __init__(self,state,parent,g,tickets):
    self.state=state
    self.sucessores=[]
    self.parent=parent
    self.tickets=tickets
    self.g=g
    self.h=1
    self.f=self.h+self.g
  
  def getTickets():
    return self.tickets

  def setSucessores(lst):
    self.sucessores=lst

  def getSucessores():
    return sucessores
  
  def setParent(parent):
    self.parent=parent
  
  def getParent():
    return self.parent
  
  def setG(g):
    self.g=g

  def getg(G):
    return self.g

  def setH(h):
    self.h=h
  
  def getH(h):
    return self.h

  def setF():
    self.f=self.g+self.h
  
  def setSucessores(list):
    self.sucessores=list
  
  def getState():
    return self.state




class Policia:
  def __init__(self,inic,tickets):
    self.pos_inic=inic
    self.actual_pos=inic
    
  
  
  def setPosition(new_position):
    self.actual_pos=new_posi

  def getActualPosition():
    return self.actual_pos


class State:
  def __init__(self,pos,goal,trans):
    self.pos=pos
    self.trans=trans
    self.goal=goal
    
  
  def setPos(lst):
    self.pos=lst
  
  def getPos():
    return self.pos
  
  def getTrans():
    return self.trans
  
  


  
  
