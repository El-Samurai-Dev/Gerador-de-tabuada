
from tkinter import *
import math

janela = Tk()

janela.title("Gerador de Tabuada")
janela.config(bg='black')
#janela.geometry("300x400")

## Função ####################################################################################################
##############################################################################################################

def on_enter(event):
    event.widget.config(bg='Cyan2')

def on_leave(event):
    event.widget.config(bg='Cyan')

##############################################################################################################
def multiplicar():
    try:
        numero = float(entrada_numero.get())
        x = 1
        mostrar_resultado = ""
        while x <= 10:
            resultado = numero * x 
            mostrar_resultado += f'{x} X {numero} = {resultado}\n'
            print(mostrar_resultado)
            x += 1

            if x > 11-1:
                break     
        
        numero_re.config(text=f'Tabuada de Multiplicação {numero} \n{mostrar_resultado}')

    except ValueError:
        numero_re.config(text="Por favor, insira um número válido.")
##############################################################################################################
def dividir():
    try:
        numero = float(entrada_numero.get())
        x = 1
        mostrar_resultado = ""
        while x <= 10:
            resultado = numero / x 
            mostrar_resultado += f'{x} / {numero} = {resultado:.2f}\n'
            print(mostrar_resultado)
            x += 1

            if x > 11-1:
                break     
        
        numero_re.config(text=f'Tabuada de Divisão {numero} \n{mostrar_resultado}')

    except ValueError:
        numero_re.config(text="Por favor, insira um número válido.")
##############################################################################################################
def raiz_quadrada():
    try:
        numero = float(entrada_numero.get())
        if numero > 0:
            mostrar_resultado = math.sqrt(numero) 
            
            numero_re.config(text=f'Raiz Quadrada de {numero} = {mostrar_resultado}')
            
        else:
            numero_re.config(text="Por favor, insira um número válido.")
            print(mostrar_resultado)    

    except ValueError:
        numero_re.config(text="Por favor, insira um número válido.")
    
## Texto #####################################################################################################
##############################################################################################################

texto_tabuada = Label(
    janela,
    bg='black',
    fg='DeepPink', 
    text= "Gerador de Tabuada", 
    font=('Arial 15', 15, 'bold'), 
    anchor=W
)

texto_tabuada.pack(
    pady=10
)

frame_input = Frame(janela)
frame_input.pack(pady=2)

## Label #####################################################################################################
##############################################################################################################

numero = Label(
    janela,
    bg='black', 
    fg='DeepPink',
    text="Digite um número:", 
    font=('Arial', 10)
)

numero.pack( 
   
    side=LEFT,
    anchor=W,
    
)

## Entrada ###################################################################################################
##############################################################################################################

entrada_numero = Entry(
    janela,
    width=5,
    font=('Arial', 15)
    )

entrada_numero.pack(
    side=LEFT,
    pady=1
)

## Respostas ###################################################################################################
################################################################################################################

numero_re = Label(
    janela, 
    width=30,
    bg='black',
    fg='DeepPink', 
    font=('Arial', 10, 'bold'),
    text= "", 
    anchor='center',
    justify='center'
)

numero_re.pack( 
    
    pady=5
)

## Botão Multiplicar ###########################################################################################
################################################################################################################

botao_multiplicar = Button(
    
    text='Tabuada Multiplicação',
    font=('verdana', 8, 'bold'),
    command=multiplicar,
    fg='Blue4',
    bd=4, 
    width=18, 
    height=2, 
    relief='raised', 
 )
botao_multiplicar.pack(
     
    padx=3,
    pady=1,
    anchor=W 
)

botao_multiplicar.bind("<Enter>", on_enter)
botao_multiplicar.bind("<Leave>", on_leave)

## Botão Dividir ###############################################################################################
################################################################################################################

botao_dividir = Button( 
    text='Tabuada Divisão',
    font=('verdana', 8, 'bold'),
    command=dividir,
    fg='Blue4',
    bd=4, 
    width=18, 
    height=2, 
    relief='raised', 
)
botao_dividir.pack(
    padx=3,
    pady=1,
    anchor=W

)
botao_dividir.bind("<Enter>", on_enter)
botao_dividir.bind("<Leave>", on_leave)

## Botão Raiz_Quadrada #########################################################################################
################################################################################################################

botao_raiz_quadrada = Button( 
    text='Raiz Quadrada',
    font=('verdana', 8, 'bold'),
    command=raiz_quadrada,
    fg='Blue4',
    bd=4, 
    width=18, 
    height=2, 
    relief='raised', 
)
botao_raiz_quadrada.pack(
    padx=3,
    pady=1,
    anchor=W

)
botao_raiz_quadrada.bind("<Enter>", on_enter)
botao_raiz_quadrada.bind("<Leave>", on_leave)

################################################################################################################
################################################################################################################

janela.mainloop()