import requests


def check_for_none(param):
    """Функция, заменяющая None на 0. Нужно для предотвращения ошибок"""
    if param is None:
        return 0
    return param


def get_parameters(row):  # v means vacancy
    v_name = check_for_none(row['name'])
    v_url = check_for_none(row['alternate_url'])

    if row['salary'] is not None:
        v_from = check_for_none(row['salary']['from'])
        v_to = check_for_none(row['salary']['to'])
    else:
        v_from = 0
        v_to = 0

    if row['schedule']['id'] == 'remote':
        v_remote = 'Возможна удалённая работа'
    else:
        v_remote = 'Удалённая работа не возможна'

    return v_name, v_url, [v_from, v_to], v_remote


URL = 'https://api.hh.ru/vacancies'


# Максимально доступное количество вакансий за один запрос = 100
def find_vacancy(pages=100, remote=True):
    searching_text = input('Введите ключевые слова искомой вакансии: ')
    par = {'text': searching_text, 'per_page': pages}

    if remote:
        par['schedule'] = 'remote'

    request = requests.get(URL, params=par).json()
    for item in request['items']:
        print(*get_parameters(item))


if __name__ == '__main__':
    find_vacancy()
