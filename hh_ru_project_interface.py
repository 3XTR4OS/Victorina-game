import hh_ru_vacancy_finder as hh_project
import tkinter
from tkinter import ttk


def printer():
    hh_project.find_vacancy()


main = tkinter.Tk()
main.title('Поисковик вакансий')

form = ttk.Frame(main, padding=51)  # добавить "рамку", в которую можно засунуть надписи и кнопки
form.grid()  # "заспавнить" её [рамку]
ttk.Button(form, text='Найти вакансии', command=printer).grid(column=1, row=1)
main.mainloop()

#
# root = tkinter.Tk(screenName='tetr')
# form = tkinter.ttk.Frame(root, padding=51)
# form.grid()
#
# tkinter.ttk.Button(form, text='Я Олег', command=printer(1)).grid(column=1, row=0)
# tkinter.ttk.Button(form, text='Я не олег. Пока', command=printer(2)).grid(column=1, row=1)
#
# root.mainloop()
