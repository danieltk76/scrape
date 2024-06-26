from bs4 import BeautifulSoup

# allows us to open the file
with open('testFile.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    # soup.find will take the html tag and return all tags of the example given, h1 below
    tags = soup.find('h1')
    # soup.find_all will take the html tag and return every instance of that tag, h2 below
    # tags_all = soup.find_all('h2')
    # below we iterated through and printed out each h2 (tags_all) out in a readable format
    # for x in tags_all:
        # print(x.text)
    # print(tags_all)
    example_search = soup.find_all('div', class_='product')
    for search in example_search:
        search_Name = search.h3.text
        search_price = search.p
        print(f'{search_Name} costs {search_price}')