from tkinter import *
from banco import banco
from classes.aluno import Aluno


selected_tuple = None

def get_aluno():
    aluno = Aluno(
        nome.get(),
        materia.get(),
        av1.get(),
        av2.get(),
        av3.get(),
        avd.get(),
        avds.get(),
    )
    return aluno

def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])
    e5.delete(0, END)
    e5.insert(END, selected_tuple[5])
    e6.delete(0, END)
    e6.insert(END, selected_tuple[6])
    e7.delete(0, END)
    e7.insert(END, selected_tuple[7])



def view_command():
    list1.delete(0, END)
    for row in banco.verTodos():
        list1.insert(END, row)


def search_command():
    pass
    list1.delete(0, END)
    aluno = get_aluno()
    for row in backend.search(titulo.get(), autor.get(), ano.get(), isbn.get()):
        list1.insert(END, row)


def add_command():
    aluno = get_aluno()
    banco.inserir(aluno)
    list1.delete(0, END)
    list1.insert(END, (aluno.nome, aluno.materia, aluno.av1,
                    aluno.av2, aluno.av3, aluno.avd, aluno.avds,
                    aluno.media, aluno.situacao))
    # Limpando as informações na entry
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)

    view_command()

def delete_command():
    #backend.delete(selected_tuple[0])
    banco.deletar(selected_tuple[0])
    # Limpando as informações na entry
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    view_command()

def update_command():
    #backend.update(selected_tuple[0], titulo.get(
    #), autor.get(), ano.get(), isbn.get())
    aluno = get_aluno()
    banco.alterar(selected_tuple[0], aluno)
    # Limpando as informações na entry
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    view_command()

root = Tk()
root.title("**** ESCOLA *****")
width = 920
height = 300
# colectando informacoes do monitor
sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)
# tamanho da janela principal
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(1, 1)
root.config(bg='light sky blue')

l1 = Label(root, text="Aluno", bg='light sky blue', fg='#6006ff')
l1.grid(row=0, column=0)
l2 = Label(root, text="Materia", bg='light sky blue', fg='#6006ff')
l2.grid(row=1, column=0)
l3 = Label(root, text="AV1", bg='light sky blue', fg='#6006ff')
l3.grid(row=0, column=2)
l4 = Label(root, text="AV2", bg='light sky blue', fg='#6006ff')
l4.grid(row=1, column=2)
l4 = Label(root, text="AV3", bg='light sky blue', fg='#6006ff')
l4.grid(row=2, column=2)
l4 = Label(root, text="AVD", bg='light sky blue', fg='#6006ff')
l4.grid(row=3, column=2)
l4 = Label(root, text="AVDS", bg='light sky blue', fg='#6006ff')
l4.grid(row=4, column=2)


nome = StringVar()
e1 = Entry(root, textvariable=nome)
e1.grid(row=0, column=1)

materia = StringVar()
e2 = Entry(root, textvariable=materia)
e2.grid(row=1, column=1)

av1 = StringVar()
e3 = Entry(root, textvariable=av1)
e3.grid(row=0, column=3)

av2 = StringVar()
e4 = Entry(root, textvariable=av2)
e4.grid(row=1, column=3)

av3 = StringVar()
e5 = Entry(root, textvariable=av3)
e5.grid(row=2, column=3)

avd = StringVar()
e6 = Entry(root, textvariable=avd)
e6.grid(row=3, column=3)

avds = StringVar()
e7 = Entry(root, textvariable=avds)
e7.grid(row=4, column=3)


list1 = Listbox(root, height=8, width=55)
list1.grid(row=6, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(root)
sb1.grid(row=6, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(root, text="Exibir todos", width=22,
            bg="snow", command=view_command)
b1.grid(row=9, column=3)

"""b2 = Button(root, text="Pesquisar", width=22, command=search_command)
b2.grid(row=5, column=4)"""

b3 = Button(root, text="Incluir", width=22, bg="#4169e1", command=add_command)
b3.grid(row=10, column=3)

b4 = Button(root, text="Atualizar Selecionado",
            width=22, bg="snow", command=update_command)
b4.grid(row=9, column=4)

b5 = Button(root, text="Deletar Selecionado",
            bg="firebrick4", width=22, command=delete_command)
b5.grid(row=10, column=4)

b6 = Button(root, text="Fechar", width=22, bg="red", command=root.destroy)
b6.grid(row=12, column=4)

root.mainloop()
