# Задача 105 Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input('Введите текст: ')     # Привет забвение меня зимбабве зовут незабвен Незнайка
text = text.split(' ')
new_text = ' '.join([item for item in text if 'абв' not in item])    
print(new_text)
