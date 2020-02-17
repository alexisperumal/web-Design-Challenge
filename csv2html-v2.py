# Alexis Perumal, 2/16/20
# Source: https://www.google.com/search?safe=active&sxsrf=ACYBGNSepv-EToTYgoEd2nddzACgxcYzDA%3A1581925012976&ei=lEJKXteaO47Y-wSagZaoDA&q=how+to+convert+csv+to+html+table+in+python&oq=how+to+convert+csv+to+html+table+in+python&gs_l=psy-ab.3..0j0i22i30.6088.7200..7588...0.2..0.97.923.10......0....1..gws-wiz.......0i71.QfIN1WksO7E&ved=0ahUKEwjXtNbzidjnAhUO7J4KHZqABcUQ4dUDCAs&uact=5#kpvalbx=_nkJKXpqzC82e-gTn7YqABQ23
# Source: http://zetcode.com/python/prettytable/
from prettytable import PrettyTable

csv_file = open('Data/weather.csv', 'r')
csv_file = csv_file.readlines()

x = PrettyTable()
x.field_names = csv_file[0].split(',')

for row in range(1, len(csv_file)):
    x.add_row(csv_file[row].split(','))

html_code = x.get_html_string()
html_file = open('Data/weather.html', 'w')
html_file = html_file.write(html_code)
