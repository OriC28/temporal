import re

fecha = '8/8/2024 9:50 pm' # Ejemplo con múltiples espacios

  # Usando \s+ para permitir uno o más espacios entre la fecha y la hora
if re.match(r'^\d{1,2}/\d{1,2}/\d{4}\s+\d{1,2}:\d{2}\s+[ap]m$', fecha, re.IGNORECASE):
    print(fecha)
