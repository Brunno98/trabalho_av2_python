import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msb
from classes.aluno import Aluno
from banco import banco

# ========= CORES ==========

COR = {
	"fundo_escuro": "#3598db",
	"fundo_claro": "#f3f5f6",
	"inserir": "#3598db",
	"deletar": "#aa0b0b",
	"alterar": "#3598db",
	"filtrar": "#85d4dc",
	"limpar_filtro": "#dee1e3"
}


# =========== FRAME PRINCIPAL ============
root = tk.Tk()
root.title("Escola")
width = 800
height = 500
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x = (screen_w / 2) - (width / 2)
y = (screen_h / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg=COR["fundo_claro"])

# ============ FRAMES DE MARGEM =========== 
margem_topo = tk.Frame(root, height=20, bg=COR["fundo_claro"])
margem_topo.pack(side=tk.TOP, fill=tk.X)
margem_base = tk.Frame(root, height=20, bg=COR["fundo_claro"])
margem_base.pack(side=tk.BOTTOM, fill=tk.X)

# ============ VARIAVEIS ===========
id = None
nome = tk.StringVar()
materia = tk.StringVar()
av1 = tk.StringVar()
av2 = tk.StringVar()
av3 = tk.StringVar()
avd = tk.StringVar()
avds = tk.StringVar()
pesquisa = tk.StringVar()
valor_comboBox = tk.StringVar()
newWindow = None

# ============= MÉTODOS ==============

def inserir():
	if valida_campos():
		aluno = Aluno(
			nome.get(),
			materia.get(),
			av1.get().replace(',', '.'),
			av2.get().replace(',', '.'),
			av3.get().replace(',', '.'),
			avd.get().replace(',', '.'),
			avds.get().replace(',', '.')
		)
		banco.inserir(aluno)
		limpar_campos()
		newWindow.destroy()
		atualiza_treeView()

def alterar():
	if valida_campos():
		global id
		aluno = Aluno(
			nome.get(),
			materia.get(),
			av1.get(),
			av2.get(),
			av3.get(),
			avd.get(),
			avds.get()
		)
		banco.alterar(id, aluno)
		limpar_campos()
		atualiza_treeView()

def deletar():
	if not treeView.focus():
		msb.showwarning("Registro não selecionado", "Por favor, selecione um registro")
	else:
		item = treeView.focus()
		conteudo = treeView.item(item)
		selectedItem = conteudo["values"]
		resposta = msb.askquestion("Confirmar exclusão", "Tem certeza que deseja excluir este registro?", icon="warning")
		if resposta == "yes":
			banco.deletar(selectedItem[0])
			limpar_campos()
			atualiza_treeView()

def limpar_campos():
	nome.set(""),
	materia.set(""),
	av1.set(""),
	av2.set(""),
	av3.set(""),
	avd.set(""),
	avds.set("")

def filtrar():
	conteudo = banco.pesquisar(pesquisa.get().strip(), dropdown_situacao.get().replace("situação", ''))
	treeView.delete(*treeView.get_children())
	for registro in conteudo:
		treeView.insert('', "end", value=(registro))

def limpar_filtro():
	pesquisa.set("")
	dropdown_situacao.current(0)
	atualiza_treeView()

def onSelect(event):
	global id
	item = treeView.focus()
	conteudo = treeView.item(item)
	itemSelected = conteudo["values"]
	if not itemSelected:
		return
	id = itemSelected[0]
	limpar_campos()
	nome.set(itemSelected[1]),
	materia.set(itemSelected[2]),
	av1.set(itemSelected[3]),
	av2.set(itemSelected[4]),
	av3.set(itemSelected[5]),
	avd.set(itemSelected[6]),
	avds.set(itemSelected[7])
	abrirJanelaDeAtualiza()

def abrirJanelaDeAtualiza():
	updateWindow = tk.Toplevel(bg=COR["fundo_claro"])
	updateWindow.title("Atualizando registro.")
	width = 480
	height = 300
	sc_width = updateWindow.winfo_screenwidth()
	sc_height = updateWindow.winfo_screenheight()
	x = (sc_width / 2) - (width / 2)
	y = (sc_height / 2) - (height / 2)
	updateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
	updateWindow.resizable()

	formTitle = tk.Frame(updateWindow, bg=COR["fundo_escuro"])
	formTitle.pack(side=tk.TOP, fill=tk.X)

	lbl_title = tk.Label(formTitle, text="Atualizando registro", font=("Arial", 18), bg=COR["fundo_escuro"])
	lbl_title.pack(fill=tk.X, pady=10)

	frame_formulario = tk.Frame(updateWindow, bg=COR["fundo_claro"])
	frame_formulario.pack(side=tk.TOP, pady=10)

	lbl_nome = tk.Label(frame_formulario, text="Nome", bg=COR["fundo_claro"])
	lbl_materia = tk.Label(frame_formulario, text="Materia", bg=COR["fundo_claro"])
	lbl_av1 = tk.Label(frame_formulario, text="AV1", bg=COR["fundo_claro"])
	lbl_av2 = tk.Label(frame_formulario, text="AV2", bg=COR["fundo_claro"])
	lbl_av3 = tk.Label(frame_formulario, text="AV3", bg=COR["fundo_claro"])
	lbl_avd = tk.Label(frame_formulario, text="AVD", bg=COR["fundo_claro"])
	lbl_avds = tk.Label(frame_formulario, text="AVDS", bg=COR["fundo_claro"])

	lbl_nome.grid(row=0 , column=0)
	lbl_materia.grid(row=1 , column=0)
	lbl_av1.grid(row=2 , column=0)
	lbl_av2.grid(row=3 , column=0)
	lbl_av3.grid(row=4 , column=0)
	lbl_avd.grid(row=5 , column=0)
	lbl_avds.grid(row=6 , column=0)

	entry_nome = tk.Entry(frame_formulario, textvariable=nome )
	entry_materia = tk.Entry(frame_formulario, textvariable=materia )
	entry_av1 = tk.Entry(frame_formulario, textvariable=av1 )
	entry_av2 = tk.Entry(frame_formulario, textvariable=av2 )
	entry_av3 = tk.Entry(frame_formulario, textvariable=av3 )
	entry_avd = tk.Entry(frame_formulario, textvariable=avd )
	entry_avds = tk.Entry(frame_formulario, textvariable=avds )

	entry_nome.grid(row=0 ,column=1)
	entry_materia.grid(row=1 ,column=1)
	entry_av1.grid(row=2 ,column=1)
	entry_av2.grid(row=3 ,column=1)
	entry_av3.grid(row=4 ,column=1)
	entry_avd.grid(row=5 ,column=1)
	entry_avds.grid(row=6 ,column=1)

	bttn_alterar = tk.Button(frame_formulario, text="Alterar", width=30, command=alterar, bg=COR["alterar"])
	bttn_alterar.grid(row=7, columnspan=2, pady=10)

def abrirJanelaDeInserir():
	limpar_campos()
	global newWindow
	newWindow = tk.Toplevel(bg=COR["fundo_claro"])
	newWindow.title("Inserindo registro.")
	width = 480
	height = 300
	sc_width = newWindow.winfo_screenwidth()
	sc_height = newWindow.winfo_screenheight()
	x = (sc_width / 2) - (width / 2)
	y = (sc_height / 2) - (height / 2)
	newWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
	newWindow.resizable()

	formTitle = tk.Frame(newWindow, bg=COR["fundo_escuro"])
	formTitle.pack(side=tk.TOP, fill=tk.X)

	lbl_title = tk.Label(formTitle, text="Inserindo novo registro", font=("Arial", 18), bg=COR["fundo_escuro"])
	lbl_title.pack(fill=tk.X, pady=10)

	frame_formulario = tk.Frame(newWindow, bg=COR["fundo_claro"])
	frame_formulario.pack(side=tk.TOP, pady=10)

	lbl_nome = tk.Label(frame_formulario, text="Nome", bg=COR["fundo_claro"])
	lbl_materia = tk.Label(frame_formulario, text="Materia", bg=COR["fundo_claro"])
	lbl_av1 = tk.Label(frame_formulario, text="AV1", bg=COR["fundo_claro"])
	lbl_av2 = tk.Label(frame_formulario, text="AV2", bg=COR["fundo_claro"])
	lbl_av3 = tk.Label(frame_formulario, text="AV3", bg=COR["fundo_claro"])
	lbl_avd = tk.Label(frame_formulario, text="AVD", bg=COR["fundo_claro"])
	lbl_avds = tk.Label(frame_formulario, text="AVDS", bg=COR["fundo_claro"])

	lbl_nome.grid(row=0 , column=0)
	lbl_materia.grid(row=1 , column=0)
	lbl_av1.grid(row=2 , column=0)
	lbl_av2.grid(row=3 , column=0)
	lbl_av3.grid(row=4 , column=0)
	lbl_avd.grid(row=5 , column=0)
	lbl_avds.grid(row=6 , column=0)

	entry_nome = tk.Entry(frame_formulario, textvariable=nome )
	entry_materia = tk.Entry(frame_formulario, textvariable=materia )
	entry_av1 = tk.Entry(frame_formulario, textvariable=av1 )
	entry_av2 = tk.Entry(frame_formulario, textvariable=av2 )
	entry_av3 = tk.Entry(frame_formulario, textvariable=av3 )
	entry_avd = tk.Entry(frame_formulario, textvariable=avd )
	entry_avds = tk.Entry(frame_formulario, textvariable=avds )

	entry_nome.grid(row=0 ,column=1)
	entry_materia.grid(row=1 ,column=1)
	entry_av1.grid(row=2 ,column=1)
	entry_av2.grid(row=3 ,column=1)
	entry_av3.grid(row=4 ,column=1)
	entry_avd.grid(row=5 ,column=1)
	entry_avds.grid(row=6 ,column=1)

	bttn_inserir = tk.Button(frame_formulario, text="Inserir", width=30, command=inserir, bg=COR["inserir"])
	bttn_inserir.grid(row=7, columnspan=2, pady=10)

def valida_campos():
	# verifica se há campo vazio
	if (nome.get() == "" or materia.get() == "" or av1.get() == "" or
	av2.get() == "" or av3.get() == "" or avd.get() == "" or
	avds.get() == ""):
		msb.showwarning("Dados inválidos", "Por favor, preencha todos os campos")
		return False

	# verifica se a nota é um valor valido
	try:
		float(av1.get().replace(',', '.'))
		float(av2.get().replace(',', '.'))
		float(av3.get().replace(',', '.'))
		float(avd.get().replace(',', '.'))
		float(avds.get().replace(',', '.'))
	except ValueError:
		msb.showwarning("Nota inválida", "Por favor, insira apenas valores numéricos nos campos de nota.")

	# verifica se a nota está entre 0 e 10
	if not (
		0 <= float(av1.get().replace(',', '.')) <= 10 and
		0 <= float(av2.get().replace(',', '.')) <= 10 and
		0 <= float(av3.get().replace(',', '.')) <= 10 and
		0 <= float(avd.get().replace(',', '.')) <= 10 and
		0 <= float(avds.get().replace(',', '.')) <= 10
	):
		msb.showwarning("Notas inválidas", "Por favor, preencha as notas sendo maior ou igual a 0 e menor ou igual a 10.")
		return False
	return True

def atualiza_treeView():
	treeView.delete(*treeView.get_children())
	registros = banco.verTodos()
	for registro in registros:
		treeView.insert('', "end", values=(registro))


# ============ FRAME BOTÕES ===========

frame_botoes = tk.Frame(root, bg=COR["fundo_claro"])
frame_botoes.pack(side=tk.BOTTOM)

bttn_abrirJanelaInserir = tk.Button(frame_botoes, text="Inserir novo registro", command=abrirJanelaDeInserir, bg=COR["inserir"])
bttn_deletar = tk.Button(frame_botoes, text="Deletar", command=deletar, bg=COR["deletar"], foreground="white")

bttn_abrirJanelaInserir.grid(row=0, column=0)
bttn_deletar.grid(row=0, column=1, pady=10, padx=5)


# =========== FRAME REGISTROS E FILTROS ========

frame_registros = tk.Frame(root, bg=COR["fundo_claro"])
frame_registros.pack()

frame_filtros = tk.Frame(frame_registros, bg=COR["fundo_claro"])
frame_filtros.pack(pady=5)

lbl_pesquisar = tk.Label(frame_filtros, text="Filtrar nome/matéria:", bg=COR["fundo_claro"])
lbl_pesquisar.grid(row=0, column=0)
entry_pesquisar = tk.Entry(frame_filtros, textvariable=pesquisa)
entry_pesquisar.grid(row=0, column=1)
dropdown_situacao = ttk.Combobox(frame_filtros)
dropdown_situacao["values"] = ("situação", "aprovado", "reprovado")
dropdown_situacao.current(0)
dropdown_situacao["state"] = "readonly"
dropdown_situacao.grid(row=0, column=2)
bttn_filtrar = tk.Button(frame_filtros, text="Filtrar", command=filtrar, bg=COR["filtrar"])
bttn_filtrar.grid(row=0, column=3)
bttn_limpar_filtro = tk.Button(frame_filtros, text="Limpar filtro", command=limpar_filtro, bg=COR["limpar_filtro"])
bttn_limpar_filtro.grid(row=0, column=4)


frame_tabela = tk.Frame(frame_registros, bg=COR["fundo_claro"])
frame_tabela.pack(side=tk.BOTTOM, fill=tk.X)

scroolbar_y = tk.Scrollbar(frame_tabela, orient=tk.VERTICAL)
scroolbar_x = tk.Scrollbar(frame_tabela, orient=tk.HORIZONTAL)

treeView = ttk.Treeview(frame_tabela, height=400, selectmode="extended",
        yscrollcommand=scroolbar_y.set, xscrollcommand=scroolbar_x.set,
        columns=("id", "nome", "materia", "av1", "av2", "av3", "avd", "avds", "media", "situacao"))

scroolbar_y.config(command=treeView.yview)
scroolbar_x.config(command=treeView.xview)
scroolbar_y.pack(side=tk.RIGHT , fill=tk.Y)
scroolbar_x.pack(side=tk.BOTTOM , fill=tk.X)

treeView.heading("id", text="ID" ,anchor=tk.W)
treeView.heading("nome", text="Nome" ,anchor=tk.W)
treeView.heading("materia", text="Materia" ,anchor=tk.W)
treeView.heading("av1", text="AV1" ,anchor=tk.W)
treeView.heading("av2", text="AV2" ,anchor=tk.W)
treeView.heading("av3", text="AV3" ,anchor=tk.W)
treeView.heading("avd", text="AVD" ,anchor=tk.W)
treeView.heading("avds", text="AVDS" ,anchor=tk.W)
treeView.heading("media", text="Média" ,anchor=tk.W)
treeView.heading("situacao", text="Situação" ,anchor=tk.W)
treeView.column("#0", stretch=tk.NO, minwidth=0, width=0)
treeView.column("#1", stretch=tk.NO, minwidth=0, width=50)
treeView.column("#2", stretch=tk.NO, minwidth=0, width=100)
treeView.column("#3", stretch=tk.NO, minwidth=0, width=100)
treeView.column("#4", stretch=tk.NO, minwidth=0, width=50)
treeView.column("#5", stretch=tk.NO, minwidth=0, width=50)
treeView.column("#6", stretch=tk.NO, minwidth=0, width=50)
treeView.column("#7", stretch=tk.NO, minwidth=0, width=50)
treeView.column("#8", stretch=tk.NO, minwidth=0, width=50)
treeView.column("#9", stretch=tk.NO, minwidth=0, width=70)
treeView.column("#10", stretch=tk.NO, minwidth=0, width=100)

treeView.pack()
treeView.bind("<Double-Button-1>", onSelect)


atualiza_treeView()
root.mainloop()
