# Program for automation of monitoring and accompaniment of quices.
# Made by Santiago Neusa.
# More information in https://github.com/sneusar/Computational-Thinking-NFI

import os
import sys
import shutil
import datetime
import subprocess
import pandas as pd

print('\nBienvenido al programa de automatización de seguimiento de quices.')

# asking for the monitor data
group_name = input('\nEscriba el código del grupo al que le desea realizar el seguimiento: ')
monitor_name = input('\nIngrese su nombre: ')
print('\nIngrese el quiz que desea revisar copiando la letra q y luego el número.\nSi ingresa \'q3\' se revisaría solo el quiz 3.')
print('Si ingresa \'q4 q5\' se revisarían quiz 4 y 5.')
quices_list = input('Ingrese el quiz: ').upper().split()

quices = [f'Quiz 0{quiz[1]}' for quiz in quices_list]
quices_names = ''
for quiz in quices: quices_names += f' {quiz}'

folder_path = os.getcwd()
file_list = os.listdir(folder_path)
group_name_folder = f'Grupo {group_name} -{quices_names}'
os.makedirs(group_name_folder, exist_ok = True)

feedback_txt_file = f'Mensajes Grupo {group_name} -{quices_names}.txt'
results_path = group_name_folder + '/'

dataframe = pd.read_csv(os.path.join(folder_path, (group_name + '.csv')), sep = ';')

# writing the Feedback.txt file
original_stdout = sys.stdout
with open(feedback_txt_file, 'w', encoding='utf-8') as f:

    sys.stdout = f
    print(f'            -- GRUPO {group_name} --\n')

    for column in dataframe.columns:
        if column == 'Nombre' or column == 'Apellido(s)' or column == 'Dirección de correo': continue
        elif any(quiz in column for quiz in quices):
            activity_name = column[13:-7]
            activity_name = activity_name[:9].replace(' -', ':') + activity_name[9:]
            activity_name = activity_name.replace(' -', '')
            dataframe = dataframe.rename(columns = {column: activity_name})
        else: del dataframe[column]
    students = {}

    row_counter = 3
    for index, row in dataframe.iterrows():
        name = row[0]
        lastname = row[1]
        email = row[2]
        unsent_activities = []

        for grade in row[3:]:
            if grade == '-' or float(grade) < 4:
                unsent_activities.append((dataframe.columns[row_counter], grade))
            row_counter += 1
        row_counter = 3

        if len(unsent_activities) > 0: students[name + ' ' + lastname] = (email, unsent_activities)
        else: dataframe = dataframe.drop(index)

    # txt file messages
    for student, data in students.items():
        print('Correo:', data[0])
        print(f'Hola {student.split()[0].capitalize()}, ¿Cómo estás?\nEstaba revisando Moodle y vi que:\n')
    
        for activity in data[1]:
            print(f'     {activity[0]}')
            if activity[1] == '-': print('     Nota: No enviado')
            else: print('     Nota:', activity[1])
   
        print(f'\nAsí que quería saber si tienes dudas sobre esos temas, y si es así, podemos reunirnos, de forma presencial o virtual.')
        print(f'Cordial saludo, {monitor_name}.\n\n')
    
    # creating xlsx file
    now = str(datetime.datetime.now())
    dataframe.insert(loc = 3, column = 'Fec Reporte', value = now[:10])
    dataframe.insert(loc = 4, column = 'Grupo', value = group_name)
    dataframe.insert(dataframe.shape[1], 'Fecha de contacto', '')
    dataframe.insert(dataframe.shape[1], 'Comentario', '')
    dataframe.insert(dataframe.shape[1], 'Hubo Asesoría', '')

    feedback_xlsx_file = f'Seguimiento {feedback_txt_file[8:-4]}.xlsx'
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
