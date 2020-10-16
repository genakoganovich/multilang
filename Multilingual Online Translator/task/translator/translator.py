import requests
from bs4 import BeautifulSoup
print('Type "en" if you want to translate from French into English, '
      'or "fr" if you want to translate from English into French:')
language = 'french'
# language = input()
print('Type the word you want to translate:')
word = 'hello'
# word = input()
print('You chose "{}" as the language to translate "{}" to.'.format(language, word))
url = 'https://context.reverso.net/translation/english-{}/{}'.format(language, word)
headers = {'user-agent': 'my-app/0.0.1'}
response = requests.get(url, headers=headers)
print(response.status_code, 'OK')

soup = BeautifulSoup(response.content, 'html.parser')
found_words = [item.text.strip() for item in soup.find_all('a', {'class': 'translation'})][1:6]
print('\nContext examples:\n')
print('French Translations:')
print(*found_words, sep='\n')
print('\nFrench Examples:')
found_examples = soup.find_all('div', {'class': 'example'})
examples = list()
for item in found_examples:
    examples.append(item.text.strip().split('\n\n\n\n\n'))

for item in examples[:5]:
    print(*[i.strip() for i in item], sep='\n')
    print()
