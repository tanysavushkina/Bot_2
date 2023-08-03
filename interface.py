# импорты
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

from config import comunity_token, acces_token
from core import VkTools

class BotInterface():

    def __init__(self,comunity_token, acces_token):
        self.vk = vk_api.VkApi(token=comunity_token)
        self.longpoll = VkLongPoll(self.vk)
        self.vk_tools = vkTools(acces_token)
        self.params = {}
        self.worksheets = []
        self.offset = 0

    def message_send(self, user_id, message, attachment=None):
        self.vk.method('messages.send',
                       {'user_id': user_id,
                        'message': message,
                        'attachment': attachment,
                        'random_id': get_random_id()
                        }
                        )
    # обработка событий / получение событий
    def event_handler(self):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                if event.text.lower() == 'привет':
                    '''Логика для получения данных о пользователях'''
                    self.params = self.vk_tools.get_profile_info(
                        event.user_id)
                    self.message_send(event.user_id,
                    f'Приветствую! {self.params["name"]}')
                elif event.text.lower() == 'поиск':

                    '''Логика для поиска анкет'''
                    self.message_send(
                        event.user_id, 'Начнем!')
                    if self.worksheets:
                        worksheet = self.worksheets.pop()
                        photos = get.vk_tools.get_photos(worksheet['id'])
                        photo_string = ''
                        for photo in photos:
                            photo_string += f'photo{photo["owner_id"]}_{photo["id"]},'
                    else:
                        self.worksheets = self.vk_tools.search_worksheet (self.params, self.offset)
                        worksheet = self.worksheets.pop()
                        photos = get.vk_tools.get_photos(worksheet['id'])
                        photo_string = ''
                        for photo in photos:
                            photo_string += f'photo{photo["owner_id"]}_{photo["id"]},'
                        self.offset +=10
                    self.photo(user_id, 'Фото с максимальными лайками')
                    self.message_send(event.user_id, f'имя: {worksheet["name"]} ссылка: vk.com/{worksheet["id"]}',
                    attachment=photo_string
                    )
                elif event.text.lower() == 'покa':
                    self.message_send(event.user_id, 'До скорой встречи!
                else:
                self.message_send(event.user_id, 'Команда не опознана!')





if __name__ == '__main__':
    bot_interface = BotInterface(comunity_token, acces_token)
    bot_interface.event_handler()

            

