from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Çalışma tipi", "Gün sayısı"]
table.add_row(["Stajyer", 20])
table.add_row(["Tam zamanlı", 365])
table.add_row(["Stajyer", 30])
table.add_row(["Yarı zamanlı", 180])


print(table)

my_toyota = PrettyTable()
my_fiat = PrettyTable
#my_totoya and my_fiat are VARIABLES and each contains PrettyTable OBJECTS
