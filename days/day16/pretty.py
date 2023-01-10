from prettytable import PrettyTable

table = PrettyTable() 
table.add_column('City Name', ["Viena", "Brasilia"], align="l") 
table.add_column('Population', [1_897_000, 2_786_684])


print(table)