import Tkinter as tk
from random import randint
from casilla import Casilla
from custom_button import CustomButton
from juego import Juego



class MainFrame(tk.Frame):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.parent.title("Buscaminas")
		self.parent.grid_rowconfigure(1,weight=1)
		self.parent.grid_columnconfigure(1, weight=1)

		self.frame = tk.Frame(self.parent)
		self.frame.pack(fill=tk.X,padx=5, pady=5)

		casillas = []
		botones = []
		x = int(raw_input("X:"))
		self.x = x
		y = int(raw_input("Y:"))
		self.y =y
		minas = int(raw_input("Minas: "))
		contador_minas = 0
		for i in range(y):
			casillas.append([])
			botones.append([])
			for j in range(x):
				rnd = randint(0,100)
				casilla_tmp = Casilla(rnd, juego = Juego())
				if rnd <=50 and contador_minas<minas:
					casilla_tmp.mina=True
					contador_minas=contador_minas+1
				casillas[i].append(casilla_tmp)
				button = tk.Button(self.frame, text="a", command=casillas[i][j].click_izq)
				casillas[i][j].button = button
				button.grid(row=j, column=i)
				botones[i].append(button)
		self.botones = botones
		self.casillas = casillas
	
	def asignar_numeros(self):
		for i in range(self.y):
			for j in range(self.x):
				casilla = self.casillas[i][j]
				if casilla.mina:
					continue
				boton = self.botones[i][j]
				anterior_x = j-1
				anterior_y = i-1
				siguiente_x = j+1
				siguiente_y = i+1
				contador_minas = 0
						

if __name__ == '__main__':
	root = tk.Tk()
	app = MainFrame(root)
	root.mainloop()

