import urllib.request
import re
from collections import Counter

from lxml import etree

import lxml

# region get text
import functools

url = 'https://uk.wikipedia.org/wiki/%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B0'
response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')
# endregion

# region get list of words
root = etree.HTML(data)
content = ' '.join(root.xpath("//a/text()") + root.xpath("//p/text()"))

years = set(re.findall('([12]\d{3})', text))

print(years)

names = set(map(str.lower, re.findall('\w{2,}[^.]+([А-ЯІЇҐЄ]\w+)', content)))
print(names)

words = list(map(str.lower, re.findall('[\w\']+', content, flags=re.IGNORECASE)))
result = sorted(Counter(words).items(), key=lambda x: x[1], reverse=True)
only_names = list(filter(lambda x: x[0] in names, result))
only_not_names = list(filter(lambda x: x[0] not in names, result))

print(only_names[0][0])
print(only_names[-1][0])
print()
print(only_not_names[0][0])
print(only_not_names[-1][0])
print()
print(result)
# endregion



# body = re.findall('<body.*?>(.*?)</body>', text, re.DOTALL)
# words = list(filter(lambda t: re.match('[\w]+', t, flags=re.IGNORECASE),
#                     (' '.join(filter(bool, re.findall('>(.*?)<', body[0])))).split(sep=)))

