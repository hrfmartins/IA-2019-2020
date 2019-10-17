import math
import pickle
import time

  
class SearchProblem:

  def __init__(self, goal, model, auxheur = []):
    self.goal=goal
    self.model=model
    self.auxheur=auxheur
    pass

  def search(self, init, limitexp = 2000, limitdepth = 10, tickets = [math.inf,math.inf,math.inf]):
    Policia1=Policia(init[0],tickets)
    openList=[]
    InitNode=node(init[0],None)
    openList=openList+[InitNode]
    lastNode=searchSolution(InitNode,openList,self.goal,self.model)


    return []

def searchSolution(Node,openList,goal,model):
  if(Node.vertex==goal[0]):
    return Node;
  for i in model[Node.vertex]
  

class node:
  def __init__(self,vertex,parent,g):
    self.vertex=vertex
    self.sucessores=[]
    self.parent=parent
    self.g=g
    self.h=1
    self.f=g+self.h
  
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




class Policia:
  def __init__(self,inic,tickets):
    self.pos_inic=inic
    self.actual_pos=inic
    
  
  
  def setPosition(new_position):
    self.actual_pos=new_posi

  def getActualPosition():
    return self.actual_pos


class State:
  def __init__(self):
    lstState=[]
  
  def setState(lst):
    lstState=lst
  
  def getState():
    return lstState