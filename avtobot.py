import vk_api
import time
import random

class Login():
	"""return login on api vk"""
	def LogOn(number = 'ХХХХХХХХХ', passw= 'ХХХХХХХХХ'): # <- GET LOGIN AND PASS
		return vk_api.VkApi(login=number, password=passw)
		

class GoPaste(Login):
	"""paste in the groups"""
	mes = open('INFORMATION.txt', 'r').read()

	def __init__(self):
		self.id_club = [-51095782, -8398919, -10521881, -76335378]
		self.vk = Login.LogOn()
	def Go_to(self):
		self.vk.auth()
		while True:
			for self.i in self.id_club:
				try:
					self.vk.method('wall.post', {
						'owner_id':self.i,
						'message':self.mes
						}
						)
					print("Успех")
				except Exception as e:
					print("Exception", e)
					print("в группе с данным id не выложился пост", self.i)
					time.sleep(random.randint(44, 122))
			time.sleep(7200)

GoPaste().Go_to()