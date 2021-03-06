import requests
from urllib.parse import urlencode
import time
import collections

class VKTimeError(Exception):
    def __init__(self, message, errors, user_id):
        super().__init__(message)
        self.message = message
        self.errors = errors
        self.user_id = user_id


def get_token_user(user_get):
    oauth_url = 'https://oauth.vk.com/authorize'
    auth_data = {
        'client_id': user_get,
        'display': 'page',
        'redirect_uri': 'https://oauth.vk.com/blank.html',
        'scope': 'friends,photos ,audio,video,docs,notes,pages,status,wall,groups,notifications,offline',
        'response_type': 'token',
        'v': 5.95
    }
    print('?'.join((oauth_url, urlencode(auth_data))))

# def get_info_user(params_user): поиск интересов пользователя, для которого ищем людей

def get_info_user(user_id, params_user):
    url_user_info = 'https://api.vk.com/method/users.get'
    url_user_groups = 'https://api.vk.com/method/groups.get'
    response_info_user = requests.get(url_user_info, params_user)
    response_user_groups = requests.get(url_user_groups, params_user)
    data_user_info = response_info_user.json()
    data_user_groups = response_user_groups.json()
    user_music = data_user_info["response"][0]["music"]
    user_books = data_user_info["response"][0]["books"]
    user_movies = data_user_info["response"][0]["movies"]
    user_interests = data_user_info["response"][0]["interests"]
    user_groups = data_user_groups["response"]["items"]
    user_info = {user_id: [user_music, user_books, user_movies, user_interests, user_groups]}
    return user_info


# def get_found_users_info(): поиск людей определенного диапазона
def get_found_users_info(params_search):
    search_user = 'https://api.vk.com/method/users.search'
    response_search = requests.get(search_user, params_search)
    data_search = response_search.json()
    dict_id_books = {}
    dict_id_music = {}
    dict_id_movies = {}
    dict_id_interests = {}
    list_id_users = []
    dict_groups_users = {}
    info_index = 0
    while info_index < len(data_search["response"]["items"]):
        search_id = data_search["response"]["items"][info_index]["id"]
        try:
            search_books = data_search["response"]["items"][info_index]["books"]
            search_music = data_search["response"]["items"][info_index]["music"]
            search_movies = data_search["response"]["items"][info_index]["movies"]
            search_interests = data_search["response"]["items"][info_index]["interests"]
        except KeyError:
            None
        else:
            dict_id_books.update({search_id: search_books})
            dict_id_music.update({search_id: search_music})
            dict_id_movies.update({search_id: search_movies})
            dict_id_interests.update({search_id: search_interests})
            list_id_users.extend([search_id])
        info_index += 1
    for user in list_id_users:
        url_group = 'https://api.vk.com/method/groups.get'
        params_users = {
            'v': '5.95',
            'access_token': TOKEN,
            'user_id': user
        }
        response_group_found_users = requests.get(url_group, params_users)
        try:
            groups_users = response_group_found_users.json()
            time.sleep(1)
            if DEBUG_MODE:
                print(groups_users)
            if 'error' in groups_users and 'error_code' in groups_users['error']:
                raise VKTimeError(groups_users['error']['error_code'], groups_users['error']['error_msg'], user)
        except VKTimeError as e:
            if e.message == 6:
                dict_groups_users.update({user: groups_users["response"]["items"]})
                time.sleep(1)
            if e.message == 7:
                None
            if e.message == 18:
                None
            if DEBUG_MODE:
                print("\t Код ошибки: {0} | Ошибка: {1} | USER_ID: {2}\n".format(e.message, e.errors, e.user_id))
        else:
            return dict_groups_users


# other_user == users
# def not_the_same(user, other_user):
#     return user["id"] != other_user["id"]
#
# def not_friends(user, other_user):
#     return all(not_the_same(user, other_user)
#                for friend in user["friends"])
# список id друзей пользователя user
# def friends_of_friends_ids(user):
#     return collections.Counter(foaf["id"]
#                                for friend in user["friends"]
#                                for foaf in friend["friends"]
#                                if not_the_same(user, foaf)
#                                and not_friends(user, foaf))
# по количеству общих друзей смотреть , если больше нуля - то выбирать этого пользователя?
#
# функция одинаковых интересов у пользователя и найденных пользователей
# def same_interests(target_interest):
#     return [user_id
#             for user_id, user_interest in interests
#             if user_interest == target_interest]



if __name__ == '__main__':
    DEBUG_MODE = False
    TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
    user_id = '171691064'
    params_user = {
            'v': '5.95',
            'access_token': TOKEN,
            'user_id': user_id,
            'fields': 'books, music, movies, interests'
        }
    params_search = {
        'v': '5.95',
        'sex': '2',
        'age_from': '50',
        'age_to': '65',
        'count': '100',
        'city': '1',
        'country': '1',
        'sort': '0',
        'access_token': TOKEN,
        'user_id': user_id,
        'fields': 'books, music, movies, interests'
    }
    get_info_user(user_id, params_user)
