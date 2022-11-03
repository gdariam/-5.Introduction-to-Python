from user_interface import get_data

def create():
    style = 'style="font-size:18px;"'
    html = '<html>\n <head><head>\n <body>\n'
    html += '   <p {}>Фамилия: {} <p>\n'\
        .format(style, get_data())
    html += '   <p {}>Имя: {} <p>\n'\
        .format(style, get_data())
    html += '   <p {}>Телефон: {} <p>\n'\
        .format(style, get_data())
    html += '   <p {}>Описание: {} <p>\n'\
        .format(style, get_data())
    html += ' </body>\n</html>'

    with open('Phonebook.html', 'a') as page:
        page.write(html)
    return html