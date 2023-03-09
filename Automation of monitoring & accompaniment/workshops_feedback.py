# Program for automation of monitoring and accompaniment.
# Made by Santiago Neusa.
# More information in https://github.com/sneusar/Computational-Thinking-NFI

import os
import sys
import shutil
import datetime
import subprocess
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

# asking for the monitor data
group_name = input('\nEscriba el código del grupo al que le desea realizar el seguimiento: ')
monitor_name = input('\nIngrese su nombre: ')
print('\nIngrese el taller que desea revisar copiando la letra t y luego el número.\nSi ingresa \'t8\' se revisaría solo el taller 8.')
workshops = input('Ingrese el taller: ').upper()
print('\nLa fecha debe ir en el formato \'nombre día mes\', por ejemplo \'domingo 5 de marzo\'.')
end_date = input('Ingrese la fecha final de entrega del taller: ')

# creating the new folder
folder_path = os.getcwd()
file_list = os.listdir(folder_path)
group_name_folder = 'Resultados ' + group_name
os.makedirs(group_name_folder, exist_ok = True)

# creating the Feedback file
feedback_txt_file = f'Feedback Grupo {group_name} - taller {workshops}.txt'
results_path = group_name_folder + '/'

# creating the dataframe
dataframe = pd.read_csv(os.path.join(folder_path, (group_name + '.csv')), sep = ';')

# writing the Feedback file
original_stdout = sys.stdout
with open(feedback_txt_file, 'w', encoding='utf-8') as f:

    sys.stdout = f

    print(f'            -- GRUPO {group_name} --\n')

    for column in dataframe.columns:
        if column == 'Nombre' or column == 'Apellido(s)' or column == 'Dirección de correo': continue
        if column.find(workshops) == -1: dataframe = dataframe.drop(column, axis = 1)
        dataframe = dataframe.rename(columns = {column: column[36:]})

    students = {}

    row_counter = 3
    for index, row in dataframe.iterrows():
        name = row[0]
        lastname = row[1]
        email = row[2]
        unsent_activities = []

        for grade in row[3:]:
            if grade == '-' or (float(grade) >= 0 and float(grade) < 100):
                unsent_activities.append((dataframe.columns[row_counter], grade))
            row_counter += 1
        row_counter = 3

        if len(unsent_activities) > 0: students[name + ' ' + lastname] = (email, unsent_activities)
        else: dataframe = dataframe.drop(index)

    for student, data in students.items():
        print('Correo:', data[0])
        print(f'Hola {student.split()[0].capitalize()}, ¿Cómo estás?\nEstaba revisando Moodle y vi que:\n')
    
        for activity in data[1]:
            print('     Actividad:', activity[0])
            if activity[1] == '-': print('     Nota: No enviado')
            else: print('     Nota:', activity[1])
   
        print(f'\nAsí que quería recordarte que la fecha de entrega es el {end_date}. Además, decirte que si tienes dudas, podemos reunirnos, de forma presencial o virtual.')
        print(f'Cordial saludo, {monitor_name}.\n\n')
        
    dataframe.insert(loc = 3, column = 'Grupo', value = group_name)
    now = str(datetime.datetime.now())
    dataframe.insert(loc = 4, column = 'Fec Reporte', value = now[:10])
    dataframe.insert(dataframe.shape[1], 'Fecha de envío de mensaje', '')
    dataframe.insert(dataframe.shape[1], 'Respuesta del estudiante', '')

    feedback_xlsx_file = feedback_txt_file[:-4] + '.xlsx'
    dataframe.to_excel((results_path + feedback_xlsx_file), index = False)
    

sys.stdout = original_stdout
shutil.copy(feedback_txt_file, results_path)
os.remove(feedback_txt_file)

print(f'\nLos mensajes para los estudiantes del grupo {group_name} se encuentran en \'{feedback_txt_file}\'')
print(f'El documento para llevar el seguimiento de los estudiantes es \'{feedback_xlsx_file}\'')

if os.name == 'nt':
    os.startfile(group_name_folder)
else:
    subprocess.run(['xdg-open', group_name_folder]) 

