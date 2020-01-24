

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
import networkx as nx
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import time
import os,subprocess,sys,shutil
from collections import defaultdict 
import string
from JohnsonAlgorithm import *
from floyd_warshall import *
from dijkstra import *
from Belmanford import *
from bellman import *




class Ui_Graph(QWidget):
    def __init__(self):
        super(Ui_Graph, self).__init__()
        loadUi("graphgui.ui", self)
        img_clean = QIcon('img/clean') 
        img_find = QIcon('img/find')
        self.btn_clear.clicked.connect(self.clear)
        
        self.OF.clicked.connect(self.open)
        self.find.clicked.connect(self.recherche)
        self.Dijsktra.toggled.connect(self.clear)
        self.Bellman.toggled.connect(self.clear)
        self.BellmanFord.toggled.connect(self.clear)
        self.Johnson.toggled.connect(self.clear)
        self.Floyd_Warshall.toggled.connect(self.clear)


        self.listgraph.show()
        self.listtableaux.show()
    
        self.showMaximized()

    

       


    def open(self):
        if sys.platform == "win32":
            if(self.Johnson.isChecked()):
                os.startfile('johnson.txt')
            if(self.Floyd_Warshall.isChecked()):
                os.startfile('floyd.txt')
            if(self.Dijsktra.isChecked()):
                os.startfile('dijkstra.txt')
            if(self.BellmanFord.isChecked()):
                os.startfile('bellmanford.txt')            
            if(self.Bellman.isChecked()):
                os.startfile('bellman.txt')

        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"

            if(self.Johnson.isChecked()):
                subprocess.call([opener, 'johnson.txt'])
            if(self.Floyd_Warshall.isChecked()):
                subprocess.call([opener, 'floyd.txt'])
            if(self.Dijsktra.isChecked()):
                subprocess.call([opener, 'dijkstra.txt'])
            if(self.BellmanFord.isChecked()):
                subprocess.call([opener, 'bellmanford.txt'])
            if(self.Bellman.isChecked()):
                subprocess.call([opener, 'bellman.txt'])

    def clear(self):
            self.listgraph.clear()
            self.listtableaux.clear()
    


    def sourced(self,b): #fonction qui permet d'appliquer dijksta sur la source choisie
        self.listgraph.clear()

        Alphebt= list(string.ascii_uppercase)
        G ,ma= createGraphd()
        DrawGraphd(G)

        srcs=[]
        for i in range(len(ma)):
                   
            srcs.append([Alphebt[i],i])
            
        ori=[x[1]  for x in srcs if x[0]==b.text()] #retourn la position de la source 

        src=ori[0] #source de départ

        path=[] 
        nbn=len(G)
        h=[]
        Dijkstrad(G, ma, src,h,path)
        drawDijksraTabled(h,nbn,path,src)
        DrawDijksraGraphd(path,ma,src)

        directoryt = r'Dijkstra_img' #le chamin du dossier ou se trouve les figures de graphes et taleaux générés
        for filename in os.listdir(directoryt): #parcours du dossier
            if filename.endswith(".png"):
                
                wi=QWidget()
                item = QListWidgetItem()
                layoutv = QVBoxLayout()
                imgg=QPixmap(os.path.join(directoryt, filename))
                labg=QLabel()
                labg.setPixmap(imgg)
                layoutv.addWidget(labg)
                wi.setLayout(layoutv)
                item.setSizeHint(wi.sizeHint())
                if filename=="Table.png":
                    self.listtableaux.addItem(item)  
                    self.listtableaux.setItemWidget(item,wi)
                    
                else:
                    self.listgraph.addItem(item)  
                    self.listgraph.setItemWidget(item,wi) 
    def sourcebf(self,b): #fonction qui permet d'appliquer bellman_ford sur la source choisie
        self.listgraph.clear()

        Alphebt= list(string.ascii_uppercase)
        G ,ma= createGraphbf()
        DrawGraphbf(G)

        srcs=[]
        for i in range(len(ma)):
                   
            srcs.append([Alphebt[i],i])
            
        ori=[x[1]  for x in srcs if x[0]==b.text()] #retourn la position de la source 

        src=ori[0] #source de départ

         
        nbn=len(G)
        h=[]
        mw= BellmanFordbf(ma,h,src) 

        drawBellmanFordTablebf(h,len(ma),src)
        DrawbfGraphdbf(G,mw,ma,src)

        

        directoryt = r'Bellf_img' #le chamin du dossier ou se trouve les figures de graphes et tableaux générés
        for filename in os.listdir(directoryt): #parcours du dossier
            if filename.endswith(".png"):
                
                wi=QWidget()
                item = QListWidgetItem()
                layoutv = QVBoxLayout()
                imgg=QPixmap(os.path.join(directoryt, filename))
                labg=QLabel()
                labg.setPixmap(imgg)
                layoutv.addWidget(labg)
                wi.setLayout(layoutv)
                item.setSizeHint(wi.sizeHint())
                if filename=="Table.png":
                    self.listtableaux.addItem(item)  
                    self.listtableaux.setItemWidget(item,wi)
                    
                else:
                    self.listgraph.addItem(item)  
                    self.listgraph.setItemWidget(item,wi) 
    def sourcebl(self,b): #fonction qui permet d'appliquer bellman sur la source choisie
        self.listgraph.clear()

        Alphebt= list(string.ascii_uppercase)
        G ,ma= createGraphbl()
        DrawGraphbl(G)

        srcs=[]
        for i in range(len(ma)):
                   
            srcs.append([Alphebt[i],i])
            
        ori=[x[1]  for x in srcs if x[0]==b.text()] #retourn la position de la source 

        src=ori[0] #source de départ

         
        nbn=len(G)
        

        algo=Bellman(G,ma,src)

        if algo==False:
            QMessageBox.critical(self, "Erreur", "Le sommet "+b.text()+" a des prédecesseurs")
        else:

        

            directoryt = r'Bell_img' #le chamin du dossier ou se trouve les figures de graphes et tableaux générés
            for filename in os.listdir(directoryt): #parcours du dossier
                if filename.endswith(".png"):
                    
                    wi=QWidget()
                    item = QListWidgetItem()
                    layoutv = QVBoxLayout()
                    imgg=QPixmap(os.path.join(directoryt, filename))
                    labg=QLabel()
                    labg.setPixmap(imgg)
                    layoutv.addWidget(labg)
                    wi.setLayout(layoutv)
                    item.setSizeHint(wi.sizeHint())
                    if filename=="Table.png":
                        self.listtableaux.addItem(item)  
                        self.listtableaux.setItemWidget(item,wi)
                        
                    else:
                        self.listgraph.addItem(item)  
                        self.listgraph.setItemWidget(item,wi) 


    def recherche(self):
       
        self.listgraph.clear()
        self.listtableaux.clear()
        plt.figure()


        if(self.Johnson.isChecked()):
            
            folder = r'Johnson_img'
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Erreur de suppression %s. Raison: %s' % (file_path, e))


               
            G ,ma= createGraph()
            if (G==None and ma == None):
                QMessageBox.critical(self, "Erreur", "La matrice d'adjacence est incorrecte")
            else:
                ma1=JohnsonAlgorithm(ma)
                DrawGraph(G)
                G1=createBellmanFordGraph1(ma1,ma)
                DrawBellmanFordGraph1(G1)
                G2=createBellmanFordGraph(ma,ma)
                DrawBellmanFordGraph(G2,ma)

                ln=['aTable_BellmanFord.png']

                for x in range(len(ma)):
                    ln.append('Table_'+str(x)+'.png')

                directoryt = r'Johnson_img' #le chamin du dossier ou se trouve les figures de graphes et taleaux générés
                for filename in os.listdir(directoryt): #parcours du dossier
                    if filename.endswith(".png"):
                        
                        wi=QWidget()
                        item = QListWidgetItem()
                        layoutv = QVBoxLayout()
                        imgg=QPixmap(os.path.join(directoryt, filename))
                        labg=QLabel()
                        labg.setPixmap(imgg)
                        layoutv.addWidget(labg)
                        wi.setLayout(layoutv)
                        item.setSizeHint(wi.sizeHint())
                        if filename in ln:
                            self.listtableaux.addItem(item)  
                            self.listtableaux.setItemWidget(item,wi) 
                        else:
                            self.listgraph.addItem(item)  
                            self.listgraph.setItemWidget(item,wi) 

                    else:
                        continue
            
                
            return
        


        if(self.Floyd_Warshall.isChecked()):
            folder = r'Floyd_img'
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Erreur de suppression %s. Raison: %s' % (file_path, e))


            try: 
                n=FloydWarshall()

                
               
                ln=['ainitFloyd.png']
                for x in range(n):
                    ln.append('FloydGraph'+str(x)+'.png')

                directoryt = r'Floyd_img' #le chamin du dossier ou se trouve les figures de graphes et taleaux générés
                for filename in os.listdir(directoryt): #parcours du dossier
                    if filename.endswith(".png"):
                        
                        wi=QWidget()
                        item = QListWidgetItem()
                        layoutv = QVBoxLayout()
                        imgg=QPixmap(os.path.join(directoryt, filename))
                        labg=QLabel()
                        labg.setPixmap(imgg)
                        layoutv.addWidget(labg)
                        wi.setLayout(layoutv)
                        item.setSizeHint(wi.sizeHint())
                        if filename in ln:
                            
                            self.listgraph.addItem(item)  
                            self.listgraph.setItemWidget(item,wi) 
                        else:
                            self.listtableaux.addItem(item)  
                            self.listtableaux.setItemWidget(item,wi) 

                    else:
                        continue
            except :
                QMessageBox.critical(self, "Erreur", "La matrice d'adjacence est incorrecte")

            
        if(self.Dijsktra.isChecked()):
            folder = r'Dijkstra_img'
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Erreur de suppression %s. Raison: %s' % (file_path, e))

            G ,ma= createGraphd()
            if (G==None and ma == None):
                QMessageBox.critical(self, "Erreur", "La matrice d'adjacence est incorrecte")
            else:

                DrawGraphd(G)
                
                

                directoryt = r'Dijkstra_img' #le chamin du dossier ou se trouve les figures de graphes et taleaux générés
                for filename in os.listdir(directoryt): #parcours du dossier
                    if filename.endswith(".png"):
                        
                        wi=QWidget()
                        item = QListWidgetItem()
                        layoutv = QVBoxLayout()
                        imgg=QPixmap(os.path.join(directoryt, filename))
                        labg=QLabel()
                        labg.setPixmap(imgg)
                        layoutv.addWidget(labg)
                        wi.setLayout(layoutv)
                        item.setSizeHint(wi.sizeHint())
                        if filename=="0Graph_initiale.png":
                            self.listgraph.addItem(item)  
                            self.listgraph.setItemWidget(item,wi) 
                             
                Alphebt= list(string.ascii_uppercase)
                

                msgBox = QMessageBox()

                msgBox.setWindowTitle("Choisir l'origine")
                msgBox.setWindowIcon(QIcon('img/letter-o-32.png'))
                msgBox.setIconPixmap(QPixmap("img/origine.png"))
                msgBox.setWindowFlags(Qt.FramelessWindowHint)
                msgBox.setStyleSheet("background-color: darkgray;")
                msgBox.setText('Le graphe contient '+str(len(ma))+' sommets')
                msgBox.setInformativeText("Choisissez l'origine du pcc ")

              

                for i in range(len(ma)):
                    b=QPushButton()
                    
                    b.setStyleSheet("color: white;"
                                    "background-color: #ff6600;"
                                    "font: bold 14px;"
                                    "border-width: 2px;"
                                    "min-width: 2em;"
                                    "border-radius: -50px;")
                    b.setText(Alphebt[i])

                    msgBox.addButton(b,QMessageBox.YesRole)
                    

                msgBox.buttonClicked.connect(self.sourced)

                

                msgBox.exec_()

        if(self.BellmanFord.isChecked()):
            folder = r'Bellf_img'
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Erreur de suppression %s. Raison: %s' % (file_path, e))

            G ,ma= createGraphbf()
            if (G==None and ma == None):
                QMessageBox.critical(self, "Erreur", "La matrice d'adjacence est incorrecte")
            else:

                DrawGraphbf(G)
                
                

                directoryt = r'Bellf_img' #le chamin du dossier ou se trouve les figures de graphes et taleaux générés
                for filename in os.listdir(directoryt): #parcours du dossier
                    if filename.endswith(".png"):
                        
                        wi=QWidget()
                        item = QListWidgetItem()
                        layoutv = QVBoxLayout()
                        imgg=QPixmap(os.path.join(directoryt, filename))
                        labg=QLabel()
                        labg.setPixmap(imgg)
                        layoutv.addWidget(labg)
                        wi.setLayout(layoutv)
                        item.setSizeHint(wi.sizeHint())
                        if filename=="0Graph_initiale.png":
                            self.listgraph.addItem(item)  
                            self.listgraph.setItemWidget(item,wi) 
                             
                Alphebt= list(string.ascii_uppercase)
                

                msgBox = QMessageBox()

                msgBox.setWindowTitle("Choisir l'origine")
                msgBox.setWindowIcon(QIcon('img/letter-o-32.png'))
                msgBox.setIconPixmap(QPixmap("img/origine.png"))
                msgBox.setWindowFlags(Qt.FramelessWindowHint)
                msgBox.setStyleSheet("background-color: darkgray;")
                msgBox.setText('Le graphe contient '+str(len(ma))+' sommets')
                msgBox.setInformativeText("Choisissez l'origine du pcc ")

              

                for i in range(len(ma)):
                    b=QPushButton()
                    
                    b.setStyleSheet("color: white;"
                                    "background-color: #ff6600;"
                                    "font: bold 14px;"
                                    "border-width: 2px;"
                                    "min-width: 2em;"
                                    "border-radius: -50px;")
                    b.setText(Alphebt[i])

                    msgBox.addButton(b,QMessageBox.YesRole)
                    

                msgBox.buttonClicked.connect(self.sourcebf)

                

                msgBox.exec_()
    
        if(self.Bellman.isChecked()):
            folder = r'Bell_img'
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Erreur de suppression %s. Raison: %s' % (file_path, e))

            G ,ma= createGraphbl()
            if (G==None and ma == None):
                QMessageBox.critical(self, "Erreur", "La matrice d'adjacence est incorrecte")
            else:
                cir=verifier_circuit(G)

                if cir!=None:
                    drawcircuit(G,cir)
                    directoryt = r'Bell_img' #le chamin du dossier ou se trouve les figures de graphes et taleaux générés
                    for filename in os.listdir(directoryt): #parcours du dossier
                        if filename.endswith(".png"):
                            
                            wi=QWidget()
                            item = QListWidgetItem()
                            layoutv = QVBoxLayout()
                            imgg=QPixmap(os.path.join(directoryt, filename))
                            labg=QLabel()
                            labg.setPixmap(imgg)
                            layoutv.addWidget(labg)
                            wi.setLayout(layoutv)
                            item.setSizeHint(wi.sizeHint())
                            if filename=="0Graph_initiale.png":
                                self.listgraph.addItem(item)  
                                self.listgraph.setItemWidget(item,wi) 
                    QMessageBox.critical(self, "Erreur circuit", "Le graphe contient un circuit")
                else:
                    DrawGraphbl(G)
                

                    directoryt = r'Bellf_img' #le chamin du dossier ou se trouve les figures de graphes et taleaux générés
                    for filename in os.listdir(directoryt): #parcours du dossier
                        if filename.endswith(".png"):
                            
                            wi=QWidget()
                            item = QListWidgetItem()
                            layoutv = QVBoxLayout()
                            imgg=QPixmap(os.path.join(directoryt, filename))
                            labg=QLabel()
                            labg.setPixmap(imgg)
                            layoutv.addWidget(labg)
                            wi.setLayout(layoutv)
                            item.setSizeHint(wi.sizeHint())
                            if filename=="0Graph_initiale.png":
                                self.listgraph.addItem(item)  
                                self.listgraph.setItemWidget(item,wi) 
                                 
                    Alphebt= list(string.ascii_uppercase)
                    

                    msgBox = QMessageBox()

                    msgBox.setWindowTitle("Choisir l'origine")
                    msgBox.setWindowIcon(QIcon('img/letter-o-32.png'))
                    msgBox.setIconPixmap(QPixmap("img/origine.png"))
                    msgBox.setWindowFlags(Qt.FramelessWindowHint)
                    msgBox.setStyleSheet("background-color: darkgray;")
                    msgBox.setText('Le graphe contient '+str(len(ma))+' sommets')
                    msgBox.setInformativeText("Choisissez l'origine du pcc ")

                  

                    for i in range(len(ma)):
                        b=QPushButton()
                        
                        b.setStyleSheet("color: white;"
                                        "background-color: #ff6600;"
                                        "font: bold 14px;"
                                        "border-width: 2px;"
                                        "min-width: 2em;"
                                        "border-radius: -50px;")
                        b.setText(Alphebt[i])

                        msgBox.addButton(b,QMessageBox.YesRole)
                        

                    msgBox.buttonClicked.connect(self.sourcebl)

                    

                    msgBox.exec_()


                
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    myapp = Ui_Graph()
    myapp.show()
    sys.exit(app.exec_())