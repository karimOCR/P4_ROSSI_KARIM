# **Projet 4 - Application Webscraping**
:point_down:    :point_down:    :point_down:

![GitHub Logo](image_echecs.jpeg)


###### Application Python pour la gestion des tournois d'échecs avec le système de "TOURNOI SUISSE"
## **Préambule**
###### Ce readme.md a pour objectif de décrire comment créer et activer l'environnement virtuel, cloner l'application présent sur un dépôt distant puis exécuter le code d'application ;

### **Pré-requis**

##### Pour commencer ce projet, il est essentiel d’avoir accès aux outils suivants :

- OS Linux
- Terminal linux
- Python et IDE PyCharm
- GitHub et GIT
- Navigateur web

***
## **Installation de l’environnement virtuel**
###### Les étapes suivantes définissent la création et l’activation de l’environnement virtuel necessaire au fonctionnement de l’application python.
###### Avant tout commencer par cloner ce repository dans le nouveau repertoire P4_ROSSI_KARIM

_$ cd /P4_ROSSI_KARIM_

_$ git clone https://github.com/karimOCR/P4_ROSSI_KARIM.git_

_$ python3 –m venv env_

_$ source venv/bin/activate_

_$ pip install –r requirements.txt_

_$ deactivate (une fois l'execution de l'application fini)
***
## **Autre méthode pour récupérer l’application de gestion de tournoi d'echecs**
##### Ce programme a été réalisé et testé sous __UBUNTU 20.04.2 LTS__ et __PYTHON 3__
Pour cela, Commençons par initialiser le dépôt local et ensuite procédons par le clonage du dépôt distant.

_$ git init

_$ git remote add OC https://github.com/karimOCR/P4_ROSSI_KARIM.git

_$ git branch -M main

_$ git pull OC main


## **Execution du code d’application**
###### Aller dans le Terminal, se placer sous le repertoire /P4_ROSSI_KARIM et executer le script main.py

_$ cd P4_ROSSI_KARIM

_$ python main.py

***





















