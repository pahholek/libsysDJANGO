def get_data(isbn, lib): #lib = BN - Biblioteka Narodowa, UJ - Biblioteka jagielońska
    import requests
    isbn = str(isbn)
    lib = str(lib)
    payload = {
        'kl': '',
        'al': '',
        'priority': '1',
        'uid': '',
        'dist': '2',
        'lok': 'all',
        'liczba': '5',
        'pubyearh': '',
        'pubyearl': '',
        'lang': 'pl',
        'bib': lib,
        'si': '1',
        'qt': 'F',
        'di': 'i' + isbn,
        'pp': '1',
        'detail': '3',
        'pm': 'm',
        'st1': 'ie' + isbn,
    }

    r = requests.get('https://karo.umk.pl/K_3.02/Exec/z2w_f.pl', params=payload)
    html = r.text
    print(r.url)
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, 'lxml')
    soup.find('table', {'class': 'fulltbl'})
    table_data = [[cell.text for cell in row("td")]
                  for row in soup("tr")]
    table_size = len(table_data)
    table_data_clean = []
    # junk off
    for i in range(table_size):
        try:
            int(table_data[i][0])
            table_data_clean.append(table_data[i])
        except:
            pass

    print(table_data)
    # check if data is present
    table_data_trimmed = []
    if not table_data_clean:
        return 'No_Data'
    else:
        # trim data
        for i in range(len(table_data_clean)):
                # ISBN 0
            if int(table_data_clean[i][0]) == 20:
                table_data_trimmed.append(table_data_clean[i])
                # TITLE 1
            if int(table_data_clean[i][0]) == 245:
                table_data_trimmed.append(table_data_clean[i])
                # PUBLISHER 2
            if int(table_data_clean[i][0]) == 260:
                table_data_trimmed.append(table_data_clean[i])
                # TIME OF CREATION 3
            if int(table_data_clean[i][0] == 388):
                table_data_trimmed.append(table_data_clean[i])
                #AUTHORS
            if int(table_data_clean[i][0]) == 700:
                table_data_trimmed.append(table_data_clean[i])
        # extract strings
        extracted_data = [[isbn, 'isbn']]

        def extract_Title(string):
            string = string.split('$c')[0]
            string = string.split('$a')[1]
            string = string.split('$b')[0] + string.split('$b')[1]
            return string
        extracted_data.append([extract_Title(table_data_trimmed[1][2]), 'title'])


        def extract_Authors(data):
            authors = []
            authors_string = ''
            for i in range(len(data)):
                if int(data[i][0]) == 700:
                    string = data[i][2]
                    string = string.split('$a')[1]
                    string = string.split('$')[0]
                    string = string.strip()
                    string = string.replace(',', '')
                    authors.append(string)
            for k in range(len(authors)):
                if k == len(authors)-1:
                    authors_string = authors_string + authors[k]
                else:
                    authors_string = authors_string + authors[k] + ', '
            return authors_string
        extracted_data.append([extract_Authors(table_data_trimmed), 'authors'])


        def extract_Publisher(string):
           string = string.split('$b')[1]
           string = string.split('$c')[0]
           string = string.replace(',', '')
           string = string.strip()
           return string
        extracted_data.append([extract_Publisher(table_data_trimmed[2][2]), 'Publisher'])

        for i in range(len(table_data_trimmed)):
            print(table_data_trimmed[i])
        return extracted_data
#BN - Biblioteka Narodowa, UJ - Biblioteka jagielońska
