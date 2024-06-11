from datetime import datetime as dt

data_hr_atual = dt.now()
data_hr_str = "2024-10-24 10:20"
mascara_br = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"
# mascara = '%d/%m/%Y %H:%M'
# mascara = '%d/%m/%Y'

print(data_hr_atual.strftime(mascara_br))

data_convert = dt.strptime(data_hr_str, mascara_en)

print(data_convert)

print(type(data_convert))