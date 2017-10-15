class Juego:
  matriz_automata = [
    [0,2,0,0],
    [0,0,0,0],
    [2,2,2,2]
  ]
  estado_actual = 0

  def on_text_change(self, text):
    if(text=="abierta"):
      self.estado_actual = self.matriz_automata[self.estado_actual][0]
    elif text=="bomba":
      self.estado_actual = self.matriz_automata[self.estado_actual][2]
    elif text=="pregunta":
      self.estado_actual = self.matriz_automata[self.estado_actual][3]
    elif text=="bandera":
      self.estado_actual = self.matriz_automata[self.estado_actual][2]
    return self.estado_actual
