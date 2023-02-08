### Importando bibliotecas
import tkinter as tk
import datetime

###criando a tela
class TelaPrincipal:
    def __init__(self, master):
        self.nossaTela = master
        self.lblRelogio= tk.Label(
            self.nossaTela, font=('Calibri', 40), fg = 'Blue')
        self.lblRelogio.pack(pady=30, padx=30)
        self.alteracao()

    def alteracao(self):
        now = datetime.datetime.now()
        self.lblRelogio['text'] = now.strftime('%H:%M:%S')
        self.nossaTela.after(1000, self.alteracao)

### inteface do usuário
janelaRaiz = tk.Tk()
TelaPrincipal(janelaRaiz)
janelaRaiz.mainloop()
