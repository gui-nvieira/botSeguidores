import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def escolheComent(coment):
	num=random.randint(0,(len(coment))-1)
	return coment[num]

def sleep_for_period_of_time():
	limit = random.randint(11,19)
	print('-- Tempo de espera em segundos: ', limit)
	time.sleep(limit)

def sleep_for_period_of_time_short():
	limit = random.randint(5,8)
	time.sleep(limit)

class InstagramBot:
	try:
		def __init__(self,username,password,hashtag,interacoes,comentario):
			self.username = username
			self.password = password
			self.hashtag = hashtag
			self.int = interacoes
			self.comentario = comentario
			self.driver = webdriver.Firefox(executable_path='./geckodriver.exe')

		def login(self):
			print('----- Bot Iniciado -----')
			driver = self.driver
			driver.get('https://www.instagram.com/')
			sleep_for_period_of_time_short()
			user_element = driver.find_element(By.NAME,'username')
			user_element.clear()
			user_element.send_keys(self.username)
			pass_element = driver.find_element(By.NAME,'password')
			pass_element.clear()
			pass_element.send_keys(self.password)
			pass_element.send_keys(Keys.RETURN)
			sleep_for_period_of_time_short()
			onetap = WebDriverWait(self.driver,20).until(
					EC.element_to_be_clickable((By.XPATH, '//button[@class="_acan _acao _acas"]')))
			if onetap:
				sleep_for_period_of_time_short()
				onetap.send_keys(Keys.RETURN)
			print('----- Login Realizado -----')
			box_element = WebDriverWait(self.driver,20).until(
					EC.element_to_be_clickable((By.XPATH,'//button[@class="_a9-- _a9_1"]')))
			box_element.send_keys(Keys.RETURN)
			self.curtirFotos(self.hashtag)

		def curtirFotos(self,hashtag):
			try:
				#entrando na pagina da hashtag
				driver = self.driver
				driver.get('https://www.instagram.com/explore/tags/'+hashtag+'/')
				sleep_for_period_of_time_short()
				#acessando cada publicacao
				hrefs = WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH,
				                            "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div/div/div/div[1]/div[1]/a")))
				if hrefs:
					hrefs.click()
				else:
					hrefs = WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div/div/div/div[1]/div[1]/a')))
					hrefs.send_keys(Keys.RETURN)
				sleep_for_period_of_time_short()
				#auxiliar para passar posts
				next = WebDriverWait(self.driver,20).until(
					EC.element_to_be_clickable((By.XPATH,"//button//span//*[name()='svg' and @aria-label='Next']")))
				#loop das interacoes
				for i in range(0,self.int):
					sleep_for_period_of_time_short()
					WebDriverWait(self.driver,20).until(
						EC.element_to_be_clickable((By.XPATH,"//button//span//*[name()='svg' and @aria-label='Like']"))).click()
					sleep_for_period_of_time_short()
					if not self.comentario == []:
						comentar = WebDriverWait(self.driver,20).until(
							EC.element_to_be_clickable((By.XPATH,"//textarea[@class='_ablz _aaoc']")))
						comentar.click()
						comentar = WebDriverWait(self.driver,20).until(
							EC.element_to_be_clickable((By.XPATH,"//textarea[@class='_ablz _aaoc focus-visible']")))
						comentar.send_keys(escolheComent(self.comentario))
						comentar.send_keys(Keys.ENTER)
					print(f'----- Curtida/Comentário na foto {i+1} -----')
					sleep_for_period_of_time_short()
					if not i == (self.int - 1):
						next.click()
						sleep_for_period_of_time()
				print(f'----- Terminado -----')
				driver.close()

			except Exception as e:
				print(f'Não foi possível realizar as interações erro: {e}')
				self.driver.close()

	except Exception as e:
		print(e)
