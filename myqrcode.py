import qrcode
from tkinter import *

meu_qrcode = qrcode.make(
    input('Digite o endereço que você quer usar como destino? '))
meu_qrcode.save("qrcode.png")

# abaixo criação de interface
janela = Tk()


janela.mainloop()  # diz ao python para manter a janela sendo exibida
