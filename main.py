# ------------------------------------------------- -----
# ---------------------- main.py ------------------- ----
# --------------------------------------------- ---------
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import (
    NavigationToolbar2QT as NavigationToolbar)
import matplotlib.font_manager as fm
import numpy as np
import pandas as pd
import random
import matplotlib
import random as rd
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
from os import listdir, path, rename
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDesktopWidget,QApplication,QMainWindow
import time




class MatplotlibWidget(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)
        loadUi("interfaz.ui", self)
        self.setWindowTitle("ACO")#cabecera de la interfaz
        self.setWindowIcon(QIcon('icono3.jpg'))
        self.pushButton1.clicked.connect(self.simular)
        self.pushButton2.clicked.connect(self.limpiar)
        self.comboBox.activated.connect(self.desactivar_checkbox)
        self.comboBox.clear()
        c = ['',
            'Arequipa',
            'Ayacucho',
            'Cajamarca',
            'Callao',
            'Chiclayo',
            'Chimbote',
            'Cuzco',
            'Huancayo',
            'Huanuco',
            'Huaraz',
            'Ica',
            'Iquitos',
            'Juliaca',
            'Lima',
            'Piura',
            'Pucallpa',
            'Sullana',
            'Tacna',
            'Trujillo']
        self.comboBox.addItems(c)
        #self.center() #llamar a la función

    #def center(self):

        # Obtener tamaño de pantalla
        #screen=QDesktopWidget().screenGeometry()
        # Obtener el tamaño de la ventana
        #size=self.geometry()
        # Mueva la ventana al centro de la pantalla
        #self.move((screen.width() - size.width()) /2,(screen.height() - size.height()) /2)

    def grafica(self, coordenadas, ruta):
        self.MplWidget.canvas.axes.clear()
        x = [float(coordenadas[i][1]) for i in ruta]
        x.append(x[0])
        y = [float(coordenadas[i][2]) for i in ruta]
        y.append(y[0])
        self.MplWidget.canvas.axes.plot(x, y, linewidth = 1, color='tab:blue')
        self.MplWidget.canvas.axes.scatter(x, y, s = 4 * math.pi, color = 'tab:green')# graficar puntos
        for i in ruta:
            c = (float(coordenadas[i][1]), float(coordenadas[i][2]))
            for j, k in enumerate(coordenadas):
                if i == j:
                    self.MplWidget.canvas.axes.annotate(k[0], c, size= 8)
        self.MplWidget.canvas.draw()

    def alertas(self, texto):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(texto)
        msgBox.setWindowTitle("AVISO")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.buttonClicked.connect(self.msgButtonClick)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')

    def msgButtonClick(self, i):
        print("Button clicked is:",i.text())

    def desactivar_checkbox(self):
        ciudad_1 = str(self.comboBox.currentText())
        #borrar luego de completar los if else

        if ciudad_1 == 'Arequipa':
            self.checkBox.setEnabled(False)
        elif ciudad_1 == 'Ayacucho':
            self.checkBox_5.setEnabled(False)
        elif ciudad_1 == 'Cajamarca':
            self.checkBox_4.setEnabled(False)
        elif ciudad_1 == 'Callao':
            self.checkBox_3.setEnabled(False)
        elif ciudad_1 == 'Chiclayo':
            self.checkBox_2.setEnabled(False)        
        elif ciudad_1 == 'Chimbote':
            self.checkBox_6.setEnabled(False)
        elif ciudad_1 == 'Cuzco':
            self.checkBox_8.setEnabled(False)
        elif ciudad_1 == 'Huancayo':
            self.checkBox_9.setEnabled(False)
        elif ciudad_1 == 'Huanuco':
            self.checkBox_10.setEnabled(False) 
        elif ciudad_1 == 'Huaraz':
            self.checkBox_11.setEnabled(False)
        elif ciudad_1 == 'Ica':
            self.checkBox_12.setEnabled(False) 
        elif ciudad_1 == 'Iquitos':
            self.checkBox_13.setEnabled(False)   
        elif ciudad_1 == 'Juliaca':
            self.checkBox_15.setEnabled(False)   
        elif ciudad_1 == 'Lima':
            self.checkBox_13.setEnabled(False)
        elif ciudad_1 == 'Piura':
            self.checkBox_19.setEnabled(False) 
        elif ciudad_1 == 'Pucallpa':
            self.checkBox_18.setEnabled(False)    
        elif ciudad_1 == 'Sullana':
            self.checkBox_16.setEnabled(False)
        elif ciudad_1 == 'Tacna':
            self.checkBox_20.setEnabled(False)                                                            
        else:
            self.checkBox_21.setEnabled(False)
            
    def limpiar(self):
        self.lineEdit_4.clear()
        self.doubleSpinBox_2.setValue(0)
        self.doubleSpinBox_3.setValue(0)
        self.doubleSpinBox_4.setValue(0)
        self.doubleSpinBox_5.setValue(0)
        self.spinBox.setValue(0)
        self.checkBox.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_6.setChecked(False)
        self.checkBox_8.setChecked(False)
        self.checkBox_9.setChecked(False)
        self.checkBox_10.setChecked(False)
        self.checkBox_11.setChecked(False)
        self.checkBox_12.setChecked(False)
        self.checkBox_14.setChecked(False)
        self.checkBox_15.setChecked(False)
        self.checkBox_13.setChecked(False)
        self.checkBox_19.setChecked(False)
        self.checkBox_18.setChecked(False)
        self.checkBox_16.setChecked(False)
        self.checkBox_20.setChecked(False)
        self.checkBox_21.setChecked(False)
        self.checkBox.setEnabled(True)
        self.checkBox_5.setEnabled(True)
        self.checkBox_4.setEnabled(True)
        self.checkBox_3.setEnabled(True)
        self.checkBox_2.setEnabled(True)
        self.checkBox_6.setEnabled(True)
        self.checkBox_8.setEnabled(True)
        self.checkBox_9.setEnabled(True)
        self.checkBox_10.setEnabled(True)
        self.checkBox_11.setEnabled(True)
        self.checkBox_12.setEnabled(True)
        self.checkBox_14.setEnabled(True)
        self.checkBox_15.setEnabled(True)
        self.checkBox_13.setEnabled(True)
        self.checkBox_19.setEnabled(True)
        self.checkBox_18.setEnabled(True)
        self.checkBox_16.setEnabled(True)
        self.checkBox_20.setEnabled(True)
        self.checkBox_21.setEnabled(True)
        self.lineEdit_5.clear()
        self.lineEdit_3.clear()
        self.lineEdit.clear()
        self.lineEdit_7.clear()
        self.textEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_6.clear()
        #self.comboBox.setCurrentIndex(0)
        self.comboBox.clear()
        c = ['',
        'Arequipa',
            'Ayacucho',
            'Cajamarca',
            'Callao',
            'Chiclayo',
            'Chimbote',
            'Cuzco',
            'Huancayo',
            'Huanuco',
            'Huaraz',
            'Ica',
            'Iquitos',
            'Juliaca',
            'Lima',
            'Piura',
            'Pucallpa',
            'Sullana',
            'Tacna',
            'Trujillo']
        self.comboBox.addItems(c)
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.draw()
        return 1

    def extraerCiudades(self):
        ciudad_1 = str(self.comboBox.currentText())
        print(ciudad_1)
        lista = [
        ['Arequipa',  self.checkBox.isChecked()],
        ['Ayacucho', self.checkBox_5.isChecked()],
        ['Cajamarca', self.checkBox_4.isChecked()],
        ['Callao', self.checkBox_3.isChecked()],
        ['Chiclayo', self.checkBox_2.isChecked()],
        ['Chimbote', self.checkBox_6.isChecked()],
        ['Cuzco', self.checkBox_8.isChecked()],
        ['Huancayo', self.checkBox_9.isChecked()],
        ['Huanuco', self.checkBox_10.isChecked()],
        ['Huaraz', self.checkBox_11.isChecked()],
        ['Ica', self.checkBox_12.isChecked()],
        ['Iquitos', self.checkBox_14.isChecked()],
        ['Juliaca', self.checkBox_15.isChecked()],
        ['Lima', self.checkBox_13.isChecked()],
        ['Piura', self.checkBox_19.isChecked()],
        ['Pucallpa', self.checkBox_18.isChecked()],
        ['Sullana', self.checkBox_16.isChecked()],
        ['Tacna', self.checkBox_20.isChecked()],
        ['Trujillo', self.checkBox_21.isChecked()],
        ]
        for i in range(len(lista)):#para descativar check de ciudad elegida

            if ciudad_1 == lista[i][0]:
                print(lista[i][0])
                lista[i][1] = False

        lista.insert(0, [ciudad_1, True])
        print(lista)
        return lista

    def simular(self):
        hormigas = self.lineEdit_4.text()
        if hormigas.isdigit():
            hormigas = int(hormigas)
            alfa = self.doubleSpinBox_2.text()
            beta = self.doubleSpinBox_3.text()
            rho = self.doubleSpinBox_4.text()
            iteracciones = self.spinBox.text()
            tao = self.doubleSpinBox_5.text()


            coordenadas_ciudades = self.leerExcel() # extrae todas las ciudades y coordenadas
            ciudades_elegidas = self.extraerCiudades()


            lista_ciudades = self.filtrarCiudades(coordenadas_ciudades, ciudades_elegidas)
            if len(lista_ciudades) >= hormigas:
                matriz_ciudades = self.matrizDistancia(lista_ciudades)
                distancia, lista_ruta, ruta = self.aco(lista_ciudades, matriz_ciudades, hormigas, alfa, beta, rho, iteracciones, tao)
                self.lineEdit_5.setText(distancia + ' Km')
                self.textEdit.setText(ruta)

                self.grafica(lista_ciudades, lista_ruta)
                self.lineEdit.setText(alfa)
                self.lineEdit_7.setText(beta)
                self.lineEdit_3.setText(rho)
                self.lineEdit_2.setText(iteracciones)
                self.lineEdit_6.setText(tao)

                #self.desactivar_checkbox()# prueba
                #self.grafica(coordenadas, ruta)
            else:
                self.alertas('Número de ciudades debe superar el número de hormigas')
                print('Error: Número de ciudades debe superar el número de hormigas')
        else:
            self.alertas('Ingresar número de hormigas correctas')
            print('Ingresar número de hormigas correctas')


        #print(coord)

    def leerExcel(self):
        df = pd.read_excel(r'C:\Users\Almendra\Documents\ACO\coordenadas.xlsx')
        global lista
        lista = []
        for i in df.index:
            lista.append((df['Ciudad'][i], df['Latitud'][i], df['Longitud'][i]))

        #print(lista)
        return lista

    def filtrarCiudades(self, coordenadas_ciudades, ciudades): #funcion que filtra solo las ciudades seleccionadas
        lista = []

        for ciudad in ciudades:
            if ciudad[1] == True:
                for i in coordenadas_ciudades:
                    if ciudad[0] == i[0]:
                        lista.append(i)

        #print('lista----',lista)
        return lista

    def distancia(self, lat1, lon1, lat2, lon2):

        """
        Obtiene la distancia y el angulo (acimut) entre entre dos puntos de
        coordenadas geograficas P1 a P2
        """

        #  Conversion de GMS a DEC y posteriormente a radianes
        lat1rad = math.radians(lat1)
        lon1rad = math.radians(lon1)

        lat2rad = math.radians(lat2)
        lon2rad = math.radians(lon2)


        #  Calculo de la distancia P1 a P2
        a = math.sin(lat1rad)*math.sin(lat2rad)
        b = math.cos(lat1rad)*math.cos(lat2rad)*math.cos(lon2rad - lon1rad)
        D = math.acos(a + b)  # Formula (2)

        d = 111.18*math.degrees(D)  # Formula (1)

        # Regresa distancia y angulo
        return round(d, 2)

    def matrizDistancia(self, lista):
        matriz = []
        for i in range(len(lista)):
            m = []
            for j in range(len(lista)):
                #print(lista[i], lista[j])
                if i == j:
                    d = 0.0
                else:
                    d = self.distancia(lista[i][1], lista[i][2], lista[j][1], lista[j][2])
                m.append(d)
            matriz.append(m)
        #print('matriz de distancias: ', matriz)
        return matriz

    def lengthCal(self, camino_hormiga, distmat):         #Calcular distancia
        length =[]
        dis = 0
        for i in range(len(camino_hormiga)):
            for j in range(len(camino_hormiga[i]) - 1):
                #print('valores', i, j)
                dis += distmat[camino_hormiga[i][j]][camino_hormiga[i][j + 1]]  #[2, 1 ]
                #print(dis)

            dis += distmat[camino_hormiga[i][-1]][camino_hormiga[i][0]]
            #print('dis' , dis)
            length.append(dis)
            dis = 0
            #print('tamaño', length)
        return length

    def aco(self,lista_ciudades , matriz_distancia, num_horm, alfa, beta, rho, iteracciones, tao):

        distmat = np.array(matriz_distancia)

        antNum = int(num_horm)                   # Número de hormiga
        alpha = int(float(alfa))                     #Factor de importancia de las feromonas
        beta = int(float(beta))                      # Factor de importancia de la función heurística
        pheEvaRate = float(rho)              # Tasa de evaporación de feromonas
        cityNum = distmat.shape[0]
        tao = np.asarray(tao, dtype='float64')
        pheromone = np.ones((cityNum,cityNum)) * tao      # Matriz de feromonas
        heuristic = 1 / (np.eye(cityNum) + distmat) - np.eye(cityNum)       # Matriz de información heurística, tome 1 / dismat
        iter = 1
        itermax = int(iteracciones)                       # Número de iteraciones


        while iter < itermax:
            antPath = np.zeros((antNum, cityNum)).astype(int) - 1# Camino de la hormiga
            first = self.comboBox.currentText()
            #print(first)
            firstCity = [0 for i in range(cityNum)]
            print('1',firstCity)
            #rd.shuffle(firstCity)          # Asigna aleatoriamente una ciudad de inicio para cada hormiga
            unvisted = []
            p = []
            pAccum = 0
            for i in range(len(antPath)):
                antPath[i][0] = firstCity[i]
            for i in range(len(antPath[0]) - 1):       # Actualiza gradualmente la próxima ciudad a la que irá cada hormiga
                for j in range(len(antPath)):
                    for k in range(cityNum):
                        if k not in antPath[j]:
                            unvisted.append(k)
                    for m in unvisted:
                        pAccum += pheromone[antPath[j][i]][m] ** alpha * heuristic[antPath[j][i]][m] ** beta
                    for n in unvisted:
                        p.append(pheromone[antPath[j][i]][n] ** alpha * heuristic[antPath[j][i]][n] ** beta / pAccum)
                    roulette = np.array(p).cumsum()               #Generar ruleta
                    r = rd.uniform(min(roulette), max(roulette))
                    for x in range(len(roulette)):
                        if roulette[x] >= r:                      #Utilice el método de la ruleta para elegir la próxima ciudad para ir
                            antPath[j][i + 1] = unvisted[x]
                            break
                    unvisted = []
                    p = []
                    pAccum = 0
            pheromone = (1 - pheEvaRate) * pheromone            # Feromonas volátiles
            length = self.lengthCal(antPath,distmat)
            for i in range(len(antPath)):
                for j in range(len(antPath[i]) - 1):
                    pheromone[antPath[i][j]][antPath[i][j + 1]] += 1 / length[i]     #Actualización de feromonas
                pheromone[antPath[i][-1]][antPath[i][0]] += 1 / length[i]
            iter += 1
        print("La distancia más corta es:")
        distancia = str(round(min(length), 2))

        print("El camino más corto es:")
        print(antPath[length.index(min(length))])

        ruta = list(antPath[length.index(min(length))])
        print('ruta',ruta )
        lista_ruta = [int(x) for x in ruta]
        ciudad_ruta = []
        ciudad_ruta1 = []
        for i in ruta:
            for j, k in enumerate(lista_ciudades):
                if i == j:
                    ciudad_ruta.append(str(k[0]))
                    #print('*****',lista_ciudades)
                    #print('----',ciudad_ruta)
        ciudad_ruta1 = ciudad_ruta.append(first)

        ciudad_ruta= ' - '.join(ciudad_ruta)
        print('rutaaa',ruta)

        res = (distancia, lista_ruta, ciudad_ruta)

        #print(res)
        return res

app = QApplication([])
window = MatplotlibWidget()
window.show()
app.exec_()

