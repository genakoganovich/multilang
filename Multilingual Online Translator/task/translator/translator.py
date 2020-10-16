import requests
from bs4 import BeautifulSoup

languages = [None, 'Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew',
             'Japanese', 'Dutch', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish']
headers = {'user-agent': 'my-app/0.0.1'}


def translate(from_num, to_num, w):
    url = 'https://context.reverso.net/translation/{}-{}/{}'.\
        format(languages[from_num].lower(), languages[to_num].lower(), w)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    found_words = [item.text.strip() for item in soup.find_all('a', {'class': 'translation'})][1:6]
    found_examples = soup.find_all('div', {'class': 'example'})
    examples = list()
    for item in found_examples:
        examples.append(item.text.strip().split('\n\n\n\n\n'))
    return found_words, examples


def print_results(found_words, examples, to_num):
    print('\n{} Translations:'.format(languages[to_num]))
    print(*found_words, sep='\n')
    print('\n{} Examples:'.format(languages[to_num]))
    for item in examples[:5]:
        print(*[i.strip() for i in item], sep='\n')
        print()


def run():
    print("Hello, you're welcome to the translator. Translator supports:")
    for i in range(1, len(languages)):
        print('{}. {}'.format(i, languages[i]))

    print('Type the number of your language:')
    # from_number = int(input())
    from_number = 3
    print('Type the number of language you want to translate to:')
    # to_number = int(input())
    to_number = 5
    print('Type the word you want to translate:')
    # word = input()
    word = 'hello'
    found_words, examples = translate(from_number, to_number, word)
    print_results(found_words, examples, to_number)


run()
