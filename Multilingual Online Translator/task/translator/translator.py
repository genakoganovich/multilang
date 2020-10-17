import requests
import sys
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


def print_translation(from_number, to_number, word):
    found_words, examples = translate(from_number, to_number, word)
    print_results(found_words, examples, to_number)
    original_stdout = sys.stdout
    with open(word + '.txt', 'a', encoding='utf-8') as f_out:
        sys.stdout = f_out
        print_results(found_words, examples, to_number)
        sys.stdout = original_stdout


def get_input():
    print("Hello, you're welcome to the translator. Translator supports:")
    for i in range(1, len(languages)):
        print('{}. {}'.format(i, languages[i]))

    print('Type the number of your language:')
    # from_number = int(input())
    from_number = 3
    print('Type the number of language you want to translate to:')
    # to_number = int(input())
    to_number = 0
    print('Type the word you want to translate:')
    # word = input()
    word = 'hello'
    return from_number, to_number, word


def run():
    if len(sys.argv) != 4:
        from_number, to_number, word = get_input()
    else:
        from_number, to_number, word = sys.argv[1:]
        from_number = languages.index(str(from_number).capitalize())
        if str(to_number).capitalize() in languages:
            to_number = languages.index(str(to_number).capitalize())
        else:
            to_number = 0

    if to_number:
        print_translation(from_number, to_number, word)
    else:
        for i in range(1, len(languages)):
            print_translation(from_number, i, word)


run()
