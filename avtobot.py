import vk_api
import time
import random


class Login():
    """return login on api vk"""

    def LogOn():  # <- GET LOGIN AND PASS
        return vk_api.VkApi(login='89197106221', password='rootprava12')


class GoPaste(Login):
    """paste in the groups"""
    mes = open('INFORMATION.txt', 'r').read()

    def __init__(self):
        self.id_club = [-51095782, -8398919, -10521881, -76335378]
        self.vk = Login.LogOn()

    def Go_to(self):
        self.vk.auth()
        flagForSleep = 0
        while True:
            for self.i in self.id_club:
                try:
                    self.vk.method('wall.post', {
                        'owner_id': self.i,
                        'message': self.mes
                    }
                    )
                    print("Успех")
                except Exception as e:
                    print("Exception", e)
                    print("в группе с данным id не выложился пост", self.i)
                    time.sleep(random.randint(44, 122))

            flagForSleep += 1
            if (flagForSleep <= 4):
                time.sleep(random.randint(2*60*60, 3*60*60))
            else:
                time.sleep(random.randint(8*60*60, 9*60*60))
                flagForSleep = 0

time.sleep(8*60*60)
GoPaste().Go_to()
