# rassasié predateur
# rassasié proie
# probleme sur appetit 2



from re import A, I
from tkinter import *
from random import randrange
import random
from turtle import xcor
import matplotlib.pyplot as plt
import numpy as np
import sys


sys.setrecursionlimit(10000)

haut = 60  # hauteur du tableau
larg = 60  # largeur du tableau
cote = 10  # cote d'une cellule
flag = 0
fruit=1



maxFourmis=0
listePopulationDesFourmilières=[]

listeFourmilière=[]
listeCourbe=[]
temps=[0]
tempsFruit=39

listeNourriture=["banane","tomate","pain"]
varNombreFourmilière = 8
nombreFourmis=20




'''for i in range (varNombreFourmilière):
    listePopulationDesFourmilières.append([nombreFourmis])
    newline, =ax.plot(temps, listePopulationDesFourmilières[i])
    listeCourbe.append(newLine)'''


def dessiner_population():
    global listeCourbe
    global maxFourmis
    global temps
    #Update each list of population of the anthill
    for i in range (varNombreFourmilière):
        #Update the max of the number of ants in the entire time for the plot
        if maxFourmis < listeFourmilière[i].nombreDeFourmis:
            maxFourmis= listeFourmilière[i].nombreDeFourmis
        ax.plot(temps,listePopulationDesFourmilières[i],color=listeFourmilière[i].color)
    plt.xlim(0,temps[-1]+1)
    plt.ylim(0,maxFourmis+1)
    figure.canvas.draw() 
    figure.canvas.flush_events()
'''        listePopulationDesFourmilières[i].append(listeFourmilière[i].nombreDeFourmis)
        listeCourbe[i].set_data(temps,listePopulationDesFourmilières[i])
'''








class Nourriture:
    def __init__(self,nom):
        dictionnaireFruit={"0":"Nothing", "banane":"#FFF300","tomate":"#FF3434","pain":"#D29A1E"}
        self.nom=str(nom)
        self.couleur=dictionnaireFruit[self.nom]
        self.pv=300

    def enleverBout(self):
        self.pv=self.pv-10

class Pheromone:
    def __init__(self,tribu):
        self.tribu=tribu
        self.age=0



class Valeur:

    def __init__(self,nomNourriture,*Fourmis):
        self.nourriture=Nourriture(nomNourriture)
        self.listeFourmis=[]
        self.listePheromone=[ [] for ligne in range (varNombreFourmilière)]
        for i in (Fourmis):
            self.listeFourmis.append(i)
    def nombreFourmis(self):
        return(len(self.listeFourmis))

    def ajouterFourmis(self,Fourmis):
        self.listeFourmis.append(Fourmis)

    def ajouterNourriture(self,nomNourriture):
        self.nourriture=Nourriture(nomNourriture)
    def ajouterPheromone(self,tribu,pheromone):
        self.listePheromone[tribu].append(pheromone)
    
    def possedeNourriture(self):
        if self.nourriture.nom =="0":
            return False
        else:
            return True
    def possedePheromone(self):
        ans=False
        i=0
        while i < (Fourmilière.nombreFourmilière) and ans==False:
            if len(self.listePheromone[i])>0:
                ans=True
            i=i+1
        return(ans)

    def nombrePheromone(self,numeroTribu):
        return(len(self.listePheromone[numeroTribu]))



class Fourmilière:
    nombreFourmilière=0

    def __init__(self,n,x,y):
        self.tribu=Fourmilière.nombreFourmilière
        Fourmilière.nombreFourmilière+=1
        self.nombreDeFourmis=n
        self.x=x
        self.y=y
        self.stockNourriture=0
        #Random color
        r = lambda: random.randint(0,255)
        self.color=('#%02X%02X%02X' % (r(),r(),r()))

    def ajouteNourriture(self):
        self.stockNourriture+=1
        if self.stockNourriture==5:
            self.stockNourriture=0
            self.nombreDeFourmis+=1
            spawnAnt(self.tribu)




class Fourmis:
    def __init__(self,faim,age,tribu,x,y):
        self.faim=faim
        self.age=age
        self.tribu=tribu
        self.x=x
        self.y=y
        self.hp=100

        self.tempsRechercheNourriture=randrange(200)
        self.possedeNourriture=False
        self.chemin=[]

    def deplacer(self,*deplacementForce):
        global matriceValeurTemp
        #If the ant have a specific path let her go
        if len(deplacementForce) >0:
            deplacement=deplacementForce[0]
        elif self.tempsRechercheNourriture> 200 and (self.x!= listeFourmilière[self.tribu].x or self.y!= listeFourmilière[self.tribu].y):
            self.chemin=pathFinding(self)
            deplacement="retourBaseSansPheromon"
        #Else choose a random path around her with more probability according to the pheromone number
        else:
            choixDeplacement=[0,1,2,3,4]
            #If there is pheromon
            #Evaluate the normbetween the new cell and the anthill so an ant can't be influenced by pheromon that will lead her to go to the anthill
            if matriceValeur[self.x-1][self.y].listePheromone[self.tribu]!=[]:
                norm=(((self.x-listeFourmilière[self.tribu].x)**2+(self.y-listeFourmilière[self.tribu].y)**2)**0.5)
                newNorm=((((self.x-1)-listeFourmilière[self.tribu].x)**2+(self.y-listeFourmilière[self.tribu].y)**2)**0.5)
                if newNorm > norm:
                    for i in range  (3*(matriceValeur[self.x-1][self.y].nombrePheromone(self.tribu))):
                        choixDeplacement.append(1)


            if matriceValeur[self.x][self.y-1].listePheromone[self.tribu]!=[]:
                norm=(((self.x-listeFourmilière[self.tribu].x)**2+(self.y-listeFourmilière[self.tribu].y)**2)**0.5)
                newNorm=(((self.x-listeFourmilière[self.tribu].x)**2+((self.y-1)-listeFourmilière[self.tribu].y)**2)**0.5)
                if newNorm > norm:
                    for i in range  (3*(matriceValeur[self.x][self.y-1].nombrePheromone(self.tribu))): 
                        choixDeplacement.append(2)

            if matriceValeur[self.x+1][self.y].listePheromone[self.tribu]!=[]:
                norm=(((self.x-listeFourmilière[self.tribu].x)**2+(self.y-listeFourmilière[self.tribu].y)**2)**0.5)
                newNorm=((((self.x+1)-listeFourmilière[self.tribu].x)**2+(self.y-listeFourmilière[self.tribu].y)**2)**0.5)
                if newNorm > norm:
                    for i in range  (9*(matriceValeur[self.x+1][self.y].nombrePheromone(self.tribu))):
                        choixDeplacement.append(3)

            if matriceValeur[self.x][self.y+1].listePheromone[self.tribu]!=[]:
                norm=(((self.x-listeFourmilière[self.tribu].x)**2+(self.y-listeFourmilière[self.tribu].y)**2)**0.5)
                newNorm=(((self.x-listeFourmilière[self.tribu].x)**2+((self.y+1)-listeFourmilière[self.tribu].y)**2)**0.5)
                if newNorm > norm:
                    for i in range  (9*(matriceValeur[self.x][self.y+1].nombrePheromone(self.tribu))):
                        choixDeplacement.append(4)


            deplacement=random.choice(choixDeplacement)

        

        match deplacement:
            case 0:
                matriceValeurTemp[self.x][self.y].ajouterFourmis(self)
                self.tempsRechercheNourriture+=1
                
            case 1:
                if (self.x-1)!=-1:
                    matriceValeurTemp[self.x-1][self.y].ajouterFourmis(self)
                    self.x=self.x-1
                    self.tempsRechercheNourriture+=1
                else:
                    matriceValeurTemp[self.x][self.y].ajouterFourmis(self)
                    self.tempsRechercheNourriture+=1
                    
            
            case 2:
                if (self.y-1) !=-1:
                    matriceValeurTemp[self.x][self.y-1].ajouterFourmis(self)
                    self.y=self.y-1
                    self.tempsRechercheNourriture+=1
                else:
                    matriceValeurTemp[self.x][self.y].ajouterFourmis(self)
                    self.tempsRechercheNourriture+=1
                    
            
            case 3:
                if (self.x+1)!=larg-1:
                    matriceValeurTemp[self.x+1][self.y].ajouterFourmis(self)
                    self.x=self.x+1
                    self.tempsRechercheNourriture+=1
                else:
                    matriceValeurTemp[self.x][self.y].ajouterFourmis(self)
                    self.tempsRechercheNourriture+=1
                    
            case 4:
                if (self.y+1)!=haut-1:
                    matriceValeurTemp[self.x][self.y+1].ajouterFourmis(self)
                    self.y=self.y+1
                    self.tempsRechercheNourriture+=1
                else:
                    matriceValeurTemp[self.x][self.y].ajouterFourmis(self)
                    self.tempsRechercheNourriture+=1
            case "retourBase":
                self.tempsRechercheNourriture=0
                #On rajoute a la matrice temporaire l'ancience liste de pheromone tout en ajoutant la nouvelle avec la bonne tribu et sa durabilité
                pheromone=60
                #On rajoute un pheromone à la liste
                matriceValeur[self.x][self.y].ajouterPheromone(self.tribu,pheromone)
                nextX=self.chemin[0][0]
                nextY=self.chemin[0][1]
                matriceValeurTemp[nextX][nextY].ajouterFourmis(self)
                self.x=nextX
                self.y=nextY
                self.chemin.pop(0)
                if len(self.chemin) ==0:
                    listeFourmilière[self.tribu].ajouteNourriture()
                    self.possedeNourriture=False
            case "retourBaseSansPheromon":
                self.tempsRechercheNourriture=0
                #On rajoute un pheromone à la liste
                nextX=self.chemin[0][0]
                nextY=self.chemin[0][1]
                matriceValeurTemp[nextX][nextY].ajouterFourmis(self)
                self.x=nextX
                self.y=nextY
                self.chemin.pop(0)



    def fight(self,caseFourmis,fourmis,nombreFourmis):
        attack=False
        j=0
        while j < nombreFourmis and attack==False:
            if caseFourmis.listeFourmis[j].tribu != fourmis.tribu:
                attack=True
                #The ant will deal damage between 5 and 20
                degat=randrange(5,20)
                caseFourmis.listeFourmis[j].hp-=degat
                #If her hp are below 0 then she die
            j=j+1
        return(attack)
        


    def survis():
        pass
    







matriceValeur=[[Valeur(0) for ligne in range (haut)] for colonne in range (larg)]
matriceValeurTemp=[[Valeur(0) for ligne in range (haut)] for colonne in range (larg)]
matriceAfficher=[[0 for ligne in range (haut)] for colonne in range (larg)]





def tableau():
    global flag
    global temps
    global fruit
    temps.append(len(temps))
    if fruit:
        spawnFruit()
    etapeSuivante()
    dessiner_ecosysteme()
    '''dessiner_population()'''
    if flag==1:
        fenetre.after(50, tableau)
    else:
        flag=0



def init():
    global matriceValeur
    global matriceValeurTemp
    #Demander nombre fourmilière
    global listeFourmilière
    #Initialization of the anthil
    for numeroTribu in range(varNombreFourmilière):
        spawnAnthill()
        for j in range(listeFourmilière[numeroTribu].nombreDeFourmis):
            spawnAnt(numeroTribu)
    #Initialization of the Matrix that will be shown to the user
    for x in range(haut):
        for y in range(larg):
            matriceAfficher[x][y] = canvas.create_rectangle((x*cote, y*cote, (x+1)*cote, (y+1)*cote), outline="#44FF61", fill="#44FF61")
    matriceValeur=list.copy(matriceValeurTemp)
        


def dessiner_ecosysteme():
    for x in range(larg):
        for y in range(haut):
            if matriceValeur[x][y].nombreFourmis()==0 and (matriceValeur[x][y].nourriture).nom=="0":
                coul = "#44FF61"
            elif matriceValeur[x][y].nombreFourmis()!=0:
                coul =listeFourmilière[(matriceValeur[x][y].listeFourmis[0]).tribu].color
            else:
                coul = (matriceValeur[x][y].nourriture).couleur
            
            canvas.itemconfig(matriceAfficher[x][y], fill=coul)
 
    for i in range(Fourmilière.nombreFourmilière):
        x=listeFourmilière[i].x
        y=listeFourmilière[i].y
        canvas.itemconfig(matriceAfficher[x][y], fill="black")
        canvas.itemconfig(matriceAfficher[x][y-2], fill="#F7B519")
        canvas.itemconfig(matriceAfficher[x-1][y-1], fill="#F7B519")
        canvas.itemconfig(matriceAfficher[x][y-1], fill="#F7B519")
        canvas.itemconfig(matriceAfficher[x+1][y-1], fill="#F7B519")
        canvas.itemconfig(matriceAfficher[x-2][y], fill="#F7B519")
        canvas.itemconfig(matriceAfficher[x-1][y], fill="#F7B519")
        canvas.itemconfig(matriceAfficher[x+1][y], fill="#F7B519")
        canvas.itemconfig(matriceAfficher[x+2][y], fill="#F7B519")
        canvas.itemconfig(matriceAfficher[x-1][y+1], fill="#F7B519")
        canvas.itemconfig(matriceAfficher[x][y+1], fill="#F7B519")
        canvas.itemconfig(matriceAfficher[x+1][y+1], fill="#F7B519")
        canvas.itemconfig(matriceAfficher[x][y+2], fill="#F7B519")











def etapeSuivante():


    global matriceValeur
    global matriceValeurTemp
    matriceValeurTemp=[[Valeur(0) for ligne in range (haut)] for colonne in range (larg)]
    for x in range (larg):
        for y in range (haut):
            
            caseActuel=matriceValeur[x][y]
            if caseActuel.nombreFourmis() != 0:
                comportementFourmis(x,y)
            if caseActuel.nourriture.nom !="0":
                comportementNourriture(x,y)
            if caseActuel.possedePheromone():
                for i in range (Fourmilière.nombreFourmilière):
                    numberOfNullPheromone=0
                    for j in range (matriceValeur[x][y].nombrePheromone(i)):
                        if caseActuel.listePheromone[i][j]!=0:
                            caseActuel.listePheromone[i][j]-=1
                        else:
                            numberOfNullPheromone+=1
                    for j in range(numberOfNullPheromone):
                        caseActuel.listePheromone[i].remove(0)
                matriceValeurTemp[x][y].listePheromone=caseActuel.listePheromone
    supprFourmisBelow0Hp()
    mettreAjourValeurCourbe()
    matriceValeur=list.copy(matriceValeurTemp)



def mettreAjourValeurCourbe():
    global listePopulationDesFourmilières
    for numeroFourmilière in range(len(listeFourmilière)):
        listePopulationDesFourmilières[numeroFourmilière].append(listeFourmilière[numeroFourmilière].nombreDeFourmis)



def supprFourmisBelow0Hp():
    for x in range (larg):
        for y in range (haut):
            newAntList=[]
            for fourmis in matriceValeurTemp[x][y].listeFourmis:
                if(fourmis.hp)>0:
                    newAntList.append(fourmis)
                else:
                   listeFourmilière[fourmis.tribu].nombreDeFourmis-=1
            matriceValeurTemp[x][y].listeFourmis=newAntList.copy()
            '''matriceValeurTemp[x][y].listeFourmis[:] = [fourmis for fourmis in matriceValeurTemp[x][y].listeFourmis if(fourmis.hp>0)]'''








def comportementFourmis(x,y):
    caseFourmis=matriceValeur[x][y]
    nombreFourmis=caseFourmis.nombreFourmis()
    listeFourmisTemporaire=[]
    for fourmis in  caseFourmis.listeFourmis:
        
        #If she is in pathFinding don't verify if there is food
        if not fourmis.chemin:
            #Verify if she can attack
            if fourmis.fight(caseFourmis,fourmis,nombreFourmis):
                fourmis.deplacer(0)
            #Verify if there is food
            elif caseFourmis.possedeNourriture():
                caseFourmis.nourriture.enleverBout()
                fourmis.possedeNourriture=True
                fourmis.deplacer(0)
                fourmis.chemin=pathFinding(fourmis)
                if caseFourmis.nourriture.pv <=0:
                    caseFourmis.nourriture.nom="0"
            else:
                fourmis.deplacer()
        else:
            if fourmis.possedeNourriture:
                fourmis.deplacer("retourBase")
            else:
                fourmis.deplacer("retourBaseSansPheromon")
    #Update of the list without the ant below 0hp






def comportementNourriture(x,y):
    matriceValeurTemp[x][y].nourriture=matriceValeur[x][y].nourriture
    


def spawnFruit():
    
    global tempsFruit
    tempsFruit+=1
    if tempsFruit/60==1:
        
        tempsFruit=0
        global listeNourriture
        nourriture=listeNourriture[randrange(len(listeNourriture))]
        x=randrange(3,larg-4)
        y=randrange(3,haut-4)
        if nourriture == "tomate":
            matriceValeur[x-1][y-1].ajouterNourriture("tomate")
            matriceValeur[x][y-1].ajouterNourriture("tomate")
            matriceValeur[x+1][y-1].ajouterNourriture("tomate")
            matriceValeur[x-1][y].ajouterNourriture("tomate")
            matriceValeur[x][y].ajouterNourriture("tomate")
            matriceValeur[x-1][y+1].ajouterNourriture("tomate")
            matriceValeur[x][y+1].ajouterNourriture("tomate")
            matriceValeur[x+1][y+1].ajouterNourriture("tomate")
        if nourriture == "banane":
            matriceValeur[x-1][y-2].ajouterNourriture("banane")
            matriceValeur[x][y-1].ajouterNourriture("banane")
            matriceValeur[x][y].ajouterNourriture("banane")
            matriceValeur[x-1][y+1].ajouterNourriture("banane")
        if nourriture == "pain":
            matriceValeur[x][y-1].ajouterNourriture("pain")
            matriceValeur[x+1][y-1].ajouterNourriture("pain")
            matriceValeur[x-1][y].ajouterNourriture("pain")
            matriceValeur[x][y].ajouterNourriture("pain")
            matriceValeur[x+1][y].ajouterNourriture("pain")
            matriceValeur[x-2][y+1].ajouterNourriture("pain")
            matriceValeur[x-1][y+1].ajouterNourriture("pain")
            matriceValeur[x][y+1].ajouterNourriture("pain")
            matriceValeur[x-2][y+2].ajouterNourriture("pain")
            matriceValeur[x-1][y+2].ajouterNourriture("pain")


def spawnAnt(tribu):
    anthill=listeFourmilière[tribu]
    faimFourmis=randrange(20)
    ageFourmis=randrange(20)
    nouvelleFourmis=Fourmis(faimFourmis,ageFourmis,tribu,anthill.x,anthill.y)
    matriceValeurTemp[anthill.x][anthill.y].ajouterFourmis(nouvelleFourmis)


def spawnAnthill():
    xAnthill=randrange(2,larg-3)
    yAnthill=randrange(2,haut-3)
    nouvelleFourmilière=Fourmilière(nombreFourmis,xAnthill,yAnthill)
    listeFourmilière.append(nouvelleFourmilière)
    listePopulationDesFourmilières.append([nombreFourmis])



# arret de l'animation"
def stop():
    global flag
    flag=0

#démarrage de l'animation"
def start():
    global flag
    if flag==0:
        flag=1
    tableau()


#animation pas à pas
def pasapas():
    global flag
    flag=2
    tableau()




def pathFinding(fourmis):
    fourmiliere=listeFourmilière[fourmis.tribu]
    xFourmis=fourmis.x
    yFourmis=fourmis.y
    xFourmiliere=fourmiliere.x
    yFourmiliere=fourmiliere.y
    ans=[]
    randomNumber=0
    while xFourmis != xFourmiliere or yFourmis != yFourmiliere:
        if xFourmis == xFourmiliere:
            if yFourmis > yFourmiliere:
                yFourmis-=1
                ans.append((xFourmis,yFourmis))
            else:
                yFourmis+=1
                ans.append((xFourmis,yFourmis))
        elif yFourmis == yFourmiliere:
            if xFourmis > xFourmiliere:
                xFourmis-=1
                ans.append((xFourmis,yFourmis))
            else:
                xFourmis+=1
                ans.append((xFourmis,yFourmis))

        else:
            randomNumber=randrange(2)
            if randomNumber==0:
                if yFourmis > yFourmiliere:
                    yFourmis-=1
                    ans.append((xFourmis,yFourmis))
                else:
                    yFourmis+=1
                    ans.append((xFourmis,yFourmis))
            else:
                    if xFourmis > xFourmiliere:
                        xFourmis-=1
                        ans.append((xFourmis,yFourmis))
                    else:
                        xFourmis+=1
                        ans.append((xFourmis,yFourmis))
    return(ans)




# Lancement du programme

fenetre = Tk()
fenetre.title("Simulation ecosysteme")
canvas = Canvas(fenetre, width=cote*larg, height=cote*haut, highlightthickness=0)
canvas.pack()
bou1 = Button(fenetre,text='Quitter', width=8, command=fenetre.destroy)
bou1.pack(side=RIGHT)
bou2 = Button(fenetre, text='Démarrer', width=8, command=start)
bou2.pack(side=LEFT)
bou3 = Button(fenetre, text='Arrêter', width=8, command=stop)
bou3.pack(side=LEFT)
bou4 = Button(fenetre, text='Pas à  pas', width=8, command=pasapas)
bou4.pack(side=LEFT)
init()
tableau()


fenetre.mainloop()





plt.ion()

plt.figure()

plt.xlabel('Temps')
plt.ylabel('Population des tribus')
maxFourmis=0



#Update each list of population of the anthill
for i in range (varNombreFourmilière):
    maxOfList=max(listePopulationDesFourmilières[i])
    if maxFourmis<maxOfList:
        maxFourmis=maxOfList
    #Update the max of the number of ants in the entire time for the plot
    plt.plot(temps,listePopulationDesFourmilières[i],color=listeFourmilière[i].color)
print(maxFourmis)
plt.xlim(0,temps[-1]+1)
plt.ylim(0,maxFourmis+1)
plt.show(block=True)
