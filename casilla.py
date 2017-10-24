from juego import Juego
class Casilla:
  matriz_automata = [
    [1,3],#cerrado
    [1,1],#abierto
    [2,0],#?
    [3,2] #bandera
  ]
  estados_text = ['C', 'B', '?', 'F']
  estado_actual = 0
  number = -1
  button = None
  juego = None
  def __init__(self, number,numero_minas = 0, mina = False, button = None, callback=None):
    self.numero_minas = numero_minas
    self.mina = mina
    self.number = number
    self.button = button
    self.observer = callback

  def set_numero_minas(self, value):
    self.numero_minas = value

  def abrir_casilla(self):
    self.estado_actual = self.matriz_automata[self.estado_actual][0]
    self.button.config(text=self.numero_minas)#"abierta")
    if(self.mina):
      self.button.config(text=self.estados_text[self.estado_actual])

  def click_izq(self, event):
    self.abrir_casilla()
    if(self.mina):
      self.observer()
    return self.estado_actual

  def click_der(self, event):
    self.estado_actual = self.matriz_automata[self.estado_actual][1]
    if self.estado_actual!=1:
      self.button.config(text=self.estados_text[self.estado_actual])
    '''if(self.mina):
      if(self.estado_actual==3):
        self.button.config(text="bandera")
      elif self.estado_actual==0:
        self.button.config(text="cerrado")
      else:
        self.button.config(text="?")'''

    return self.estado_actual

