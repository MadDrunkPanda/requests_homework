import requests

url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
response = requests.get(url)
data_list = response.json()


# def create_searching_list():           ## необязательный код для создания списка имен для сравнения,
#     list_of_hers = []                  ## может быть аргументом для сравивающей функции
#     while True:
#         name_hers = str(input('Введи имя для сравнения: '))
#         if name_hers == 'end':
#             False
#             break
#         list_of_hers.append(name_hers)
#     return list_of_hers

def who_is_the_boss(data_l,list_of):
    dict_verdict = {}
    for personage in data_l:
        for name in list_of:
            if name == personage['name']:
                dict_verdict[name] = personage['powerstats']['intelligence']
    return f'Самый умный {max(dict_verdict)}'

if __name__ == '__main__':

    searcing_personages = ['Hulk', 'Captain America', 'Thanos']
    print(who_is_the_boss(data_list, searcing_personages))