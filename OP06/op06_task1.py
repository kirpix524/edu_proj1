#Напишите скрипт, который запрашивает у пользователя текст, а затем записывает этот текст в файл `user_data.txt`.
from modules import inputs

def save_to_file(file_name, text_to_save, rewrite):
    if rewrite:
        par_rew = "w"
    else:
        par_rew = "a"
        text_to_save = text_to_save+"\n"
    with open(file_name, par_rew) as file:
        file.write(text_to_save)

question = "Введите имя файла (без расширения): "
file_name=inputs.safe_input_file_name(question)+".txt"
text = str(input("Введите текст, который хотите записать в файл: "))
print("Перезаписать файл? (Y/N) Если выбрать N, текст допишется в конец файла с переносом строки")
fl_rewrite = (str(input(": "))=="Y")

save_to_file(file_name, text, fl_rewrite)


