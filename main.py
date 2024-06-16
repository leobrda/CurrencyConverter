from tkinter import *
from tkinter import Tk, ttk

# Importando pillow
from PIL import Image, ImageTk, ImageOps, ImageDraw
import requests
import json
import string

# Cores
cor0 = '#ffffff' # branca
cor1 = '#333333'  # preta
cor2 = '#38576b'  # azul escuro
cor3 = '#00FF7F'  # cor verde

# Configurando a janela
janela = Tk()
janela.geometry('300x320')
janela.title('Conversor de moeda')
janela.configure(bg=cor0)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use('clam')

# Dividindo a janela
frame_cima = Frame(janela, width=300, height=60, padx=0, pady=0, bg=cor2, relief=FLAT)
frame_cima.grid(row=0, column=0, columnspan=2)

frame_baixo = Frame(janela, width=300, height=260, padx=0, pady=5, bg=cor0, relief=FLAT)
frame_baixo.grid(row=1, column=0, stick=NSEW)


# Função para converter as moedas
def converter():
    moeda_de = combo_de.get()
    moeda_para = combo_para.get()
    valor_entrada = valor_converter.get()

    response = requests.get('https://api.exchangerate-api.com/v4/latest/{}'.format(moeda_de))
    dados = json.loads(response.text)
    cambio = dados['rates'][moeda_para]
    resultado = float(valor_entrada) * float(cambio)
    print(dados)
    print(cambio)
    print(resultado)

    # Dólar americano
    if moeda_para == 'USD':
        simbolo = '$'
    # Euro
    elif moeda_para == 'EUR':
        simbolo = '€'
    # Iene japonês
    elif moeda_para == 'JPY':
        simbolo = '¥'
    # Libra esterlina
    elif moeda_para == 'GBP':
        simbolo = '£'
    # Real brasileiro
    else:
        simbolo = 'R$'

    moeda_equivalente = simbolo + '{:,.2f}'.format(resultado)
    app_resultado['text'] = moeda_equivalente


# Configurando frame cima
imagem = Image.open('Imagem/moeda.png')
imagem = imagem.resize((40, 40), Image.LANCZOS)
imagem = ImageTk.PhotoImage(imagem)

app_nome = Label(frame_cima, image=imagem, compound=LEFT, text='CONVERSOR DE MOEDA      ', height=5, pady=30, padx=13,
                 relief=RAISED, anchor=CENTER, font='Arial 13 bold', bg=cor2, fg=cor0)
app_nome.place(x=0, y=0)

# Configurando frame baixo
app_resultado = Label(frame_baixo, text='', width=16, height=2, relief=SOLID, anchor=CENTER, font='Ivi 15 bold',
                      bg=cor0, fg=cor1)
app_resultado.place(x=50, y=10)

# Moedas do projeto/Adicionar mais
moeda = ['BRL', 'USD', 'EUR', 'JPY', 'GBP']

# Configurando a parte DE
app_de = Label(frame_baixo, text='De',width=8, height=1, relief=FLAT, anchor=NW, font='Ivi 10 bold', bg=cor0, fg=cor1)
app_de.place(x=48, y=90)
combo_de = ttk.Combobox(frame_baixo, width=8, justify=CENTER, font='Ivi 12 bold')
combo_de.place(x=50, y=115)
combo_de['values'] = moeda

# Configurando a parte PARA
app_para = Label(frame_baixo, text='Para', width=8, height=1, relief=FLAT, anchor=NW, font='Ivi 10 bold',
                 bg=cor0, fg=cor1)
app_para.place(x=156, y=90)
combo_para = ttk.Combobox(frame_baixo, width=8, justify=CENTER, font='Ivi 12 bold')
combo_para.place(x=158, y=115)
combo_para['values'] = moeda

# Configurando a parte CONVERTER
valor_converter = Entry(frame_baixo, width=22, justify=CENTER, font='Ivi 12 bold', relief=SOLID)
valor_converter.place(x=49, y=165)

botao_converter = Button(frame_baixo, command=converter, text='CONVERTER', width=19, padx=5, height=1,
                         bg=cor2, fg=cor0, font='Ivi 12 bold', relief=RAISED, overrelief=RIDGE)
botao_converter.place(x=49, y=210)

janela.mainloop()
