import requests
from bs4 import BeautifulSoup
languages = [None, 'Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew',
             'Japanese', 'Dutch', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish']
print("Hello, you're welcome to the translator. Translator supports:")
for i in range(1, len(languages)):
    print('{}. {}'.format(i, languages[i]))

print('Type the number of your language:')
from_number = int(input())
# from_number = 3
print('Type the number of language you want to translate to:')
to_number = int(input())
# to_number = 5
print('Type the word you want to translate:')
# word = 'hello'
word = input()
url = 'https://context.reverso.net/translation/{}-{}/{}'.\
    format(languages[from_number].lower(), languages[to_number].lower(), word)
headers = {'user-agent': 'my-app/0.0.1'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
found_words = [item.text.strip() for item in soup.find_all('a', {'class': 'translation'})][1:6]
print('\n{} Translations:'.format(languages[to_number]))
print(*found_words, sep='\n')
print('\n{} Examples:'.format(languages[to_number]))
found_examples = soup.find_all('div', {'class': 'example'})
examples = list()
for item in found_examples:
    examples.append(item.text.strip().split('\n\n\n\n\n'))

for item in examples[:5]:
    print(*[i.strip() for i in item], sep='\n')
    print()
