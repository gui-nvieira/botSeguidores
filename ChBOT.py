import PySimpleGUI as sg
import botInstagram
import webbrowser

def ChBot():
	# validador para o código não aceitar campos vazios
	def Validacao(valores):
		vazio = False
		for x in values:
			if valores[x] == '':
				print(f'O campo {x} está vazio')
				vazio = True
		if vazio:
			return False
		return True

	# layout Tab Facebook
	layoutFB = [
		[sg.Text('Em Breve',size=15)]
	]
	layoutTikTok = [
		[sg.Text('Em Breve',size=15)]
	]
	layoutTwitter = [
		[sg.Text('Em Breve',size=15)]
	]
	# layout Tab IG
	layoutIG = [
		[sg.Text('Usuário',size=8),sg.Input(size=(30,0),key='IG_Usuario')],
		[sg.Text('Senha',size=8),sg.Input(size=(30,0),password_char='•',key='IG_Senha')],
		[sg.Text('Hashtag',size=8),sg.Input(size=(30,0),key='IG_Hashtag')],
		[sg.Text('Interações',size=8),sg.Combo(values=[5,10,20,50,75,100,150,200],default_value=5,key='IG_Interacoes')],
		[sg.Text('Fazer comentários?',size=15),sg.Checkbox('Sim', default=True, key='IG_fazer_comentarios')],
		[sg.Text("Lista de comentários: ", tooltip='Insira um arquivo de texto com seus comentários')
			,sg.FileBrowse(button_text='Selecione',key='IG_Texto_Comentarios',file_types=(("TEXTO","*.txt"),))]
	]
	# layout Tabs
	tab_group = [
		[sg.Image('CHicon.png'), sg.Text('CHBot v0.1.1', font='Helvetica 15')],
		[sg.TabGroup(
			[[
				sg.Tab('Instagram',layoutIG),
				sg.Tab('Facebook',layoutFB),
				sg.Tab('TikTok',layoutTikTok),
				sg.Tab('Twitter',layoutTwitter),
			]],
			tab_location='centertop',
			key='Plataforma'

		)]
	]
	# layout console
	tab_group += [
		[sg.Button('Iniciar BOT',font='Helvetica 15', button_color='#5F9EA0',auto_size_button=True)],
		[sg.Multiline(size=(60,15),font='Helvetica 8',expand_x=True,expand_y=True,write_only=True,
		              reroute_stdout=True,reroute_stderr=True,echo_stdout_stderr=True,autoscroll=True,
		              auto_refresh=True)],
		[sg.Text('Site Oficial - Tutorial', key= 'link', enable_events=True, tooltip='Clique e acesse o site oficial')]
	]
	# janela
	janela = sg.Window('CHBOT v0.1.1',element_justification='c',icon='CHicon.ico').layout(tab_group)

	while True:
		# Extraindo dados da tela
		event,values = janela.Read()

		if event == sg.WIN_CLOSED:
			break
		if event == 'Iniciar BOT':

			if not values['IG_fazer_comentarios']:
				values.pop('IG_Texto_Comentarios')

			if Validacao(values):
				print(values)
				palavras = []
				if values['IG_fazer_comentarios']:
					with open(values['IG_Texto_Comentarios'],'r',encoding='UTF-8') as lista:
						for cadaPalavra in lista:
							palavras.append(cadaPalavra.rstrip())
					lista.close()
				print(palavras)
				bot = botInstagram.InstagramBot(values['IG_Usuario'],values['IG_Senha'],values['IG_Hashtag'],int(values['IG_Interacoes']),palavras)
				janela.perform_long_operation(bot.login,"Finalizado")

		elif event in 'link':
			webbrowser.open('https://google.com')

		elif event == "Finalizado":
			sg.popup('Terminado!')

	janela.close()


ChBot()
