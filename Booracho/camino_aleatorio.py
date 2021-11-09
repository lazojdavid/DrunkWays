from bokeh.models.annotations import Legend
from borracho import BorrachoTradicional 
from coordenada import Coordenada 
from bokeh.plotting import show, figure

path_x = [0]
path_y = [0]

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)
    for _ in range(pasos):
        campo.mover_borracho(borracho)
    return inicio.distancia(campo.obtener_coordenada(borracho))

def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre='David')
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borrachos(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))

    return distancias


def graficar(x,y):
    grafica = figure(title="ROADMAP- lazojdavid", x_axis_label ="pasos", y_axis_label="distancia" )
    grafica.line(x,y, legend="DRUNKS", line_color = "red")
    grafica.legend.border_line_alpha = 0.8
    grafica.legend.background_fill_color = "navy"
    grafica.legend.background_fill_alpha = 0.2
    grafica.legend.border_line_width = 3
    grafica.legend.border_line_color = "navy"



    show(grafica)

def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    distancias_media_por_caminata = []

    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}')
    
    #graficar(distancias_de_caminata, distancias_media_por_caminata)
    graficar(path_x, path_y)
#campo.py
class Campo:
  def __init__(self):
    self.coordenadas_de_borrachos = {}

  def anadir_borrachos(self,borracho,coordenada):
    self.coordenadas_de_borrachos[borracho]=coordenada
  
  def mover_borracho(self,borracho):
    delta_x, delta_y = borracho.camina()
    #append new steps
    path_x.append(path_x[-1] + delta_x)
    path_y.append(path_y[-1] + delta_y)
    coordenada_actual = self.coordenadas_de_borrachos[borracho]
    nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

    self.coordenadas_de_borrachos[borracho] = nueva_coordenada

  def obtener_coordenada(self,borracho):
    return self.coordenadas_de_borrachos[borracho]
    
if __name__ == '__main__':
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 1
    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)
    