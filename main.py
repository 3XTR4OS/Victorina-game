import requests


def check_for_none(param):
    """Function replacing None with 0. Needed to avoid errors"""
    if param is None:
        return 0
    return param


def get_vacancy_parameters(row): 
    name = check_for_none(row['name'])
    url = check_for_none(row['alternate_url'])

    if row['salary'] is not None:
        salary_from = check_for_none(row['salary']['from'])
        salary_to = check_for_none(row['salary']['to'])
    else:
        salary_from = 0
        salary_to = 0

    if row['schedule']['id'] == 'remote':
        remote = 'Возможна удалённая работа'
    else:
        remote = 'Удалённая работа не возможна'

    return name, url, [salary_from, salary_to], remote


URL = 'https://api.hh.ru/vacancies'


# Максимально доступное количество вакансий за один запрос = 100
def find_vacancy(pages=100):
    searching_text = input('Введите ключевые слова искомой вакансии: ')
    remote = input('Только удалённые вакансии? ДА/НЕТ: ')
    with_salary = input('Только с указанной зп? ДА/НЕТ: ')

    par = {'text': searching_text, 'per_page': pages}

    if remote.lower() == 'да':
        par['schedule'] = 'remote'

    if with_salary.lower() == 'да':
        par['only_with_salary'] = True

    request = requests.get(URL, params=par).json()
    for item in request['items']:
        print(*get_vacancy_parameters(item))


if __name__ == '__main__':
    find_vacancy()
