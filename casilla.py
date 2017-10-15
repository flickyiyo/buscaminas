from juego import Juego
class Casilla:
  matriz_automata = [
    [1,3],
    [1,1],
    [2,0],
    [3,2] 
  ]
  estado_actual = 0
  number = -1
  button = None
  juego = None
  def __init__(self, number,numero_minas = 0, mina = False, button = None, juego = None):
    self.numero_minas = numero_minas
    self.mina = mina
    self.number = number
    self.button = button
    self.juego = juego


  def click_izq(self):
    self.estado_actual = self.matriz_automata[self.estado_actual][0]
    estado_boton = "abierta"
    self.button.config(text="abierta")
    if(self.mina):
      self.button.config(text="bomba")
      estado_boton="bomba"
    self.juego.on_text_change(estado_boton)
    return self.estado_actual

  def click_der(self):
    self.estado_actual = self.matriz_automata[self.estado_actual][1]
    a = "bandera"
    if(self.mina):
      if(self.estado_actual==3):
        self.button.config(text="bandera")
      elif self.estado_actual==0:
        self.button.config(text="cerrado")
        a = "cerrado"
      else:
        self.button.config(text="pregunta")
        a = "pregunta"
    self.juego.on_text_change(a)

    return self.estado_actual

