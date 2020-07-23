from bs4 import BeautifulSoup

# To keep things simple and also reproducible, consider the following HTML code
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; their names:
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<b class="boldest">Extremely bold</b>
<blockquote class="boldest">Extremely bold</blockquote>
<b id="1">Test 1</b>
<b another-attribute="1" id="verybold">Test 2</b>
"""

# Write the html file
# with open('index.html', 'w') as f:
#         f.write(html_doc)

# Create BeautifulSoup content
soup = BeautifulSoup(html_doc, 'html.parser')

# Print out the nicely formatted html
# print(soup.prettify())
# print("\n")

# =============== Tags ===============
# Find the first occurrence of usage for a "b" bold tag
# print(soup.b)

# Same by using the find function
# print(soup.find('b'))
# print("\n")

# To find all the elements with the same tag, we use find_all function
# print(soup.find_all('b'))
# print("\n")

# =============== Names ===============
# Every tag contains a name, like b, and we can change it
#tag = soup.b
# print(tag)
#tag.name = "blockQuote"
# print(tag)

# =============== Attributes ===============
# tag = soup.find_all('b')[2]
# print(tag)
# print(tag['id'])

# tag = soup.find_all('b')[3]
# print(tag)
# print(tag['id'])
# print(tag['another-attribute'])

# # To print all the attributes, we can use attrs
# print(tag.attrs)

# # Also, we can change the value of the attributes
# tag['another-attribute'] = '2'
# print(tag.attrs)

# Use Python's del command for lists to remove attributes
# tag = soup.find_all('b')[3]
# print(tag)
# del tag['id']
# del tag['another-attribute']
# print(tag)

# =============== String ===============
tag = soup.find_all('b')[3]
print(tag)
print(tag.string)
tag.string.replace_with("Test 3")
print(tag.string)
