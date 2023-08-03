from pprint import pprint
from datetime import datetime

import vk_api
from vk_api.exceptions import ApiError
from config import acces_token



class VkTools:
    def __init__(self, acces_token):
       self.vkapi = vk_api.VkApi(token=acces_token)

    def _bdate_toyear(self, bdate):
        user_year = bdate.split('.')[2]
        now = datetime.now().year
        return now - int(user_year) if bdate else None

    def get_profile_info(self, user_id):

        info, = self.api.method('users.get',
                            {'user_id': user_id,
                            'fields': 'city,bdate,sex,relation,home_town'
                            }
                            )[0]
        except ApiError as e:
            info = {}
            print(f'error = {e}')


        result = {'name': (info['first_name'] + ' ' + info['last_name']) if
                    'first_name' in info and 'last_name' in info else None,
                    'sex': info.get('sex'),
                    'city': info.get('city')['title'] if info.get ('city') is not None else None,
                    'year': self._bdate_toyear(info.get('bdate')),
                    'home_town': info['home_town'],
                    'bdate': info['bdate'] if 'bdate' in info else None,
                    }
        return result


def request_user_input(self, fields, user_info):
    for field in fields:
        message = f'Введите значение '{field}': '
        response = self.send_message(message)
        user_input = response['text']

        if field == 'bdate':
            if is_valid_date(user_input):
                user_info[field] = format_date(user_input)
            else:
                self.send_message("Неверный формат даты. Повторите.")
                self.request_user_input([field], user_info)
        elif field == 'city':
            city_id = get_city_id(user_input)
            if city_id:
                user_info[field] = city_id
            else:
                self.send_message("Город не найден. Повторите.")
                self.request_user_input([field], user_info)
        else:
            user_info[field] = user_input

        # def send_message(self, message, user_id):
        #     result_1 = self.api.method('messages.send', {
        #         'user_id': user_id,
        #         'random_id': datetime.datetime.now().timestamp(),
        #         'message': message
        #     })
        #     return result_1
        def search_worksheet(self, params, offset):
            try:
                users = self.vkapi.method('users.search',
                                        {'count': 10,
                                         'offset': offset,
                                         'hometown': params['city'],
                                         'sex': 1 if params[sex] == 2 else 2,
                                         'has_photo': True,
                                         'age_from': params['year'] - 3,
                                         'age_to': params['year'] + 3,
                                         }
                                        )
    except ApiError as e:
        users = []
    print(f'error = {e}')

    result = [{
        'name': item['first_name']+ ' ' + item ['last_name'],
        'id': item['id']
        } for item in users['items'] if item['is_closed'] is False
        ]
    return result


def get_photos(self, id):
    try:
        photos = self.vkapi.method('photos.get',
                                {'owner_id': id,
                                 'album_id': 'profile',
                                 'extended': 1                                 }
                                )

    except ApiError as e:
        photos = {}
        print(f'error = {e}')

    result = [{'owner_id': item['owner_id'],
               'id': item['id'],
               'likes': item['likes']['count'],
               'comments': item['comments','count']
    } for item in photos['items']
    ]
'''Сортировка по лайкам и коментам'''
    return result[:3]

if __name__ == '__main__':
    user_id = 801289758
    tools = VkTools(acces_token)
    params = tools.get_profile_info(user_id)
    worksheets = tools.search_worksheet(params, 10)
    worksheet - worksheets.pop()
    photos = tools.get_photos(worksheet['id'])

    pprint(worksheet)
























