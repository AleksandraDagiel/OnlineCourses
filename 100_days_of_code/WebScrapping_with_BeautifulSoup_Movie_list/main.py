from bs4 import BeautifulSoup
# import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup)
print(soup.prettify())

# First paragraph (only)
print(soup.a)

# Find all
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)
for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
print(f"Anchor in paragraph element: {company_url}")
# element with name "#"
name = soup.select_one(selector="#name")
print(f"Name: {name}")
# element with class of heading "."
headings = soup.select(selector=".heading")
print(f"Headings: {headings}")
