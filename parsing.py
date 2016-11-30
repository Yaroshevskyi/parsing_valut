"""
Програма для парсигу курсів валют з чотирьох банків
"""
from tkinter import *
from tkinter.messagebox import *
from parsing_aval import *
from parsing_oshchadbank import *
from parsing_privatbank import *
from parsing_pumb import *
import csv
from tkinter.filedialog import *
import fileinput

class Aval:
    """
    Клас для взаємодіЇ з модулем parsing_aval та виведенням конкретних курсів валют
    """
    def __init__(self):
        self.aval = ParsingAval()
        self.a = self.aval.get_value()

        self.aval_usd_case = self.a[0].get('case')
        self.aval_usd_sale = self.a[0].get('sale')
        self.aval_eur_case = self.a[1].get('case')
        self.aval_eur_sale = self.a[1].get('sale')
        self.aval_rur_case = self.a[2].get('case')
        self.aval_rur_sale = self.a[2].get('sale')

        

class Oshchad:
    """
    Клас для взаємодіЇ з модулем parsing_oshchad та виведенням конкретних курсів валют
    """
    def __init__(self):
        self.oshchad = ParsingOshchadbank()
        self.b = self.oshchad.get_value()
        self.oshchad_usd_case = self.b[0].get('case')
        self.oshchad_usd_sale = self.b[0].get('sale')
        self.oshchad_eur_case = self.b[1].get('case')
        self.oshchad_eur_sale = self.b[1].get('sale')
        self.oshchad_rur_case = self.b[2].get('case')
        self.oshchad_rur_sale = self.b[2].get('sale')

class Privat:
    """
    Клас для взаємодіЇ з модулем parsing_privat та виведенням конкретних курсів валют
    """
    def __init__(self):
        self.privat = ParsingPrivatbank()
        self.c = self.privat.get_value()
        self.privat_usd_case = self.c[0].get('case') 
        self.privat_usd_sale = self.c[0].get('sale')
        self.privat_eur_case = self.c[1].get('case')
        self.privat_eur_sale = self.c[1].get('sale')
        self.privat_rur_case = self.c[2].get('case')
        self.privat_rur_sale = self.c[2].get('sale')


class Pumb:
    """
    Клас для взаємодіЇ з модулем parsing_pumb та виведенням конкретних курсів валют
    """
    def __init__(self):
        self.pumb = ParsingPumbBank()
        self.d = self.pumb.get_value()
        self.pumb_usd_case = self.d[0].get('case')
        self.pumb_usd_sale = self.d[0].get('sale')
        self.pumb_eur_case = self.d[1].get('case')
        self.pumb_eur_sale = self.d[1].get('sale')
        self.pumb_rur_case = self.d[2].get('case')
        self.pumb_rur_sale = self.d[2].get('sale')


class MainMenu:
    """
    Клас для виведення головного вікна та стрічки меню
    """
    def __init__(self):
        """
        Приймає параметри класу ValutaBank
        """
        self.val = ValutaBank()

    
    def menu(self):
        """
        Функція для вивведення головного вікна із стрічкою меню
        """

        root.title('ProCourse')# Задає титульну назву головного вікна
        root.minsize(width=500, height=400)# Задає Мінімальний розмір головного вікна
        root.wm_iconbitmap('@icon.xbm') # Виводить іконку головного вікна
        self.m = Menu(root)
        root.config(menu=self.m)

        self.valuta = Menu(self.m)
        self.m.add_cascade(label='Валюта', menu=self.valuta)
        self.valuta.add_command(label='Долар США', command = self.val.valuta_usd)
        self.valuta.add_command(label='Євро', command = self.val.valuta_eur)
        self.valuta.add_command(label='Російський рубль', command = self.val.valuta_rur)
    
        self.bank = Menu(self.m)
        self.m.add_cascade(label='Банки', menu=self.bank)
        self.bank.add_command(label='Приватбанк', command = self.val.bank_privat)
        self.bank.add_command(label='Ощадбанк', command = self.val.bank_oshchad)
        self.bank.add_command(label='Аваль', command = self.val.bank_aval)
        self.bank.add_command(label='ПУМБ Банк', command = self.val.bank_pumb)
        
        self.export = Menu(self.m)
        self.m.add_cascade(label='Експорт', menu=self.export)
        self.export.add_command(label='Експорт в CSV', command=self.val.save_csv)

        self.auction = Menu(self.m)
        self.m.add_cascade(label='Аукціон', menu=self.auction)
        self.auction.add_command(label='Перейти в аукціон')

        self.about = Menu(self.m)
        self.m.add_cascade(label='Допомога', menu=self.about)
        self.about.add_command(label='Версія',command = self.val.version)
        self.about.add_command(label='Вихід', command = self.val.close_win)
        
class ValutaBank:
    """
    Клас для виведення всіх значень із стрічки меню
    """
    def __init__(self):
        """
        Модуль для взаємодії з класами парсингу валют і виведенням обʼєкта Canvas
        """
        self.aval_obj = Aval()
        self.oshchad_obj = Oshchad()
        self.privat_obj = Privat()
        self.pumb_obj = Pumb()
        self.canv = Canvas(root, width=500, height=400)
    def clean(self):
        """
        Модуль очистки віна від попереднього виведення значення
        """
        self.canv.delete('all')
        
    def create_lines(self):
        """
        Модуль виведення горизонтальних ліній для відображення курсів
        """
        x = y = 50
        while x <= 250:
            self.canv.create_line(5,x,495,y,width=1,fill="grey")
            x += 50
            y +=50
        return

        
    def valuta_view(self):
        """
        Модуль виведення значень курсів валют по валютах
        """
        self.create_lines()
        self.canv.create_text(50,45,text="Купівля", tag='title')
        self.canv.create_text(200,45,text="Продаж", tag='title')
        self.canv.create_text(350,45,text="Назва банку", tag='title')

        self.aval_case = self.canv.create_text(50,95, tag='col')
        self.aval_sale = self.canv.create_text(200,95,tag='col')
        self.canv.create_text(350,95,text="Банк Аваль", tag='col')

        self.oshchad_case = self.canv.create_text(50,145,tag='col')
        self.oshchad_sale = self.canv.create_text(200,145,tag='col')
        self.canv.create_text(350,145,text="Ощадбанк", tag='col')

        self.privat_case = self.canv.create_text(50,195, tag='col')
        self.privat_sale = self.canv.create_text(200,195, tag='col')
        self.canv.create_text(350,195,text="Приватбанк", tag='col')

        self.pumb_case = self.canv.create_text(50,245, tag='col')
        self.pumb_sale = self.canv.create_text(200,245, tag='col')
        self.canv.create_text(350,245,text="ПУМБ банк", tag='col')


        self.canv.itemconfig('title', font='Verdana 14', anchor="sw",justify=CENTER,fill="black")
        self.canv.itemconfig('col', font="Verdana 12",anchor="sw",justify=CENTER,fill="grey")
        return
    
    def bank_view(self):
        """
        Модуль виведення значень курсів валют по банках
        """
        self.create_lines()
        self.title_bank = self.canv.create_text(50,45, tag='head_title')
        
        self.canv.create_text(50,95,text="Купівля", tag='title')
        self.canv.create_text(200,95,text="Продаж", tag='title')
        self.canv.create_text(350,95,text="Назва валюти", tag='title')

        self.bank_usd_case = self.canv.create_text(50,145,tag='col')
        self.bank_usd_sale = self.canv.create_text(200,145,tag='col')
        self.canv.create_text(350,145,text="USD", tag='col')

        self.bank_eur_case = self.canv.create_text(50,195, tag='col')
        self.bank_eur_sale = self.canv.create_text(200,195, tag='col')
        self.canv.create_text(350,195,text="EUR", tag='col')

        self.bank_rur_case = self.canv.create_text(50,245, tag='col')
        self.bank_rur_sale = self.canv.create_text(200,245, tag='col')
        self.canv.create_text(350,245,text="RUR", tag='col')

        self.canv.itemconfig('head_title', font='Verdana 16', anchor="sw",justify=CENTER,fill="black")
        self.canv.itemconfig('title', font='Verdana 14', anchor="sw",justify=CENTER,fill="black")
        self.canv.itemconfig('col', font="Verdana 12",anchor="sw",justify=CENTER,fill="grey")
        return
        
    def valuta_usd(self):       
        """
        Модуль виведення значень курсів доллара
        """
        self.clean()
        self.valuta_view()
        self.canv.itemconfig(self.aval_case, text=self.aval_obj.aval_usd_case)
        self.canv.itemconfig(self.aval_sale, text=self.aval_obj.aval_usd_sale)
        self.canv.itemconfig(self.oshchad_case, text=self.oshchad_obj.oshchad_usd_case)
        self.canv.itemconfig(self.oshchad_sale, text=self.oshchad_obj.oshchad_usd_sale)
        self.canv.itemconfig(self.privat_case, text=self.privat_obj.privat_usd_case)
        self.canv.itemconfig(self.privat_sale, text=self.privat_obj.privat_usd_sale)
        self.canv.itemconfig(self.pumb_case, text=self.pumb_obj.pumb_usd_case)
        self.canv.itemconfig(self.pumb_sale, text=self.pumb_obj.pumb_usd_sale)
        self.canv.pack()
        
        

    def valuta_eur(self):
        """
        Модуль виведення значень курсів євро
        """       
        self.clean()
        self.valuta_view()
        self.canv.itemconfig(self.aval_case, text=self.aval_obj.aval_eur_case)
        self.canv.itemconfig(self.aval_sale, text=self.aval_obj.aval_eur_sale)
        self.canv.itemconfig(self.oshchad_case, text=self.oshchad_obj.oshchad_eur_case)
        self.canv.itemconfig(self.oshchad_sale, text=self.oshchad_obj.oshchad_eur_sale)
        self.canv.itemconfig(self.privat_case, text=self.privat_obj.privat_eur_case)
        self.canv.itemconfig(self.privat_sale, text=self.privat_obj.privat_eur_sale)
        self.canv.itemconfig(self.pumb_case, text=self.pumb_obj.pumb_eur_case)
        self.canv.itemconfig(self.pumb_sale, text=self.pumb_obj.pumb_eur_sale)
        self.canv.pack()
        
    def valuta_rur(self):
        """
        Модуль виведення значень курсів російського рубля
        """
        self.clean()
        self.valuta_view()        
        self.canv.itemconfig(self.aval_case, text=self.aval_obj.aval_rur_case)
        self.canv.itemconfig(self.aval_sale, text=self.aval_obj.aval_rur_sale)
        self.canv.itemconfig(self.oshchad_case, text=self.oshchad_obj.oshchad_rur_case)
        self.canv.itemconfig(self.oshchad_sale, text=self.oshchad_obj.oshchad_rur_sale)
        self.canv.itemconfig(self.privat_case, text=self.privat_obj.privat_rur_case)
        self.canv.itemconfig(self.privat_sale, text=self.privat_obj.privat_rur_sale)
        self.canv.itemconfig(self.pumb_case, text=self.pumb_obj.pumb_rur_case)
        self.canv.itemconfig(self.pumb_sale, text=self.pumb_obj.pumb_rur_sale)
        self.canv.pack()
 
    def bank_privat(self):
        """
        Модуль виведення значень курсів валют по Приватбанку
        """
        self.clean()
        self.bank_view()
        self.canv.itemconfig(self.title_bank, text='Курс валют в Приватбанку')
        self.canv.itemconfig(self.bank_usd_case, text=self.privat_obj.privat_usd_case)
        self.canv.itemconfig(self.bank_usd_sale, text=self.privat_obj.privat_usd_sale)
        self.canv.itemconfig(self.bank_eur_case, text=self.privat_obj.privat_eur_case)
        self.canv.itemconfig(self.bank_eur_sale, text=self.privat_obj.privat_eur_sale)        
        self.canv.itemconfig(self.bank_rur_case, text=self.privat_obj.privat_rur_case)
        self.canv.itemconfig(self.bank_rur_sale, text=self.privat_obj.privat_rur_sale)
        self.canv.pack()
        
        

    def bank_oshchad(self):
        """
        Модуль виведення значень курсів валют по Ощадбанку
        """
        self.clean()
        self.bank_view()      
        self.canv.itemconfig(self.title_bank, text='Курс валют в Ощадбанку')        
        self.canv.itemconfig(self.bank_usd_case, text=self.oshchad_obj.oshchad_usd_case)
        self.canv.itemconfig(self.bank_usd_sale, text=self.oshchad_obj.oshchad_usd_sale)
        self.canv.itemconfig(self.bank_eur_case, text=self.oshchad_obj.oshchad_eur_case)
        self.canv.itemconfig(self.bank_eur_sale, text=self.oshchad_obj.oshchad_eur_sale)        
        self.canv.itemconfig(self.bank_rur_case, text=self.oshchad_obj.oshchad_rur_case)
        self.canv.itemconfig(self.bank_rur_sale, text=self.oshchad_obj.oshchad_rur_sale)
        self.canv.pack()
        
    def bank_aval(self):
        """
        Модуль виведення значень курсів валют по банку Аваль
        """
        self.clean()
        self.bank_view()        
        self.canv.itemconfig(self.title_bank, text='Курс валют в банку Аваль')        
        self.canv.itemconfig(self.bank_usd_case, text=self.aval_obj.aval_usd_case)
        self.canv.itemconfig(self.bank_usd_sale, text=self.aval_obj.aval_usd_sale)
        self.canv.itemconfig(self.bank_eur_case, text=self.aval_obj.aval_eur_case)
        self.canv.itemconfig(self.bank_eur_sale, text=self.aval_obj.aval_eur_sale)        
        self.canv.itemconfig(self.bank_rur_case, text=self.aval_obj.aval_rur_case)
        self.canv.itemconfig(self.bank_rur_sale, text=self.aval_obj.aval_rur_sale)
        self.canv.pack()
        
    def bank_pumb(self):
        """
        Модуль виведення значень курсів валют по банку ПУМБ
        """
        self.clean()
        self.bank_view()        
        self.canv.itemconfig(self.title_bank, text='Курс валют в банку ПУМБ')        
        self.canv.itemconfig(self.bank_usd_case, text=self.pumb_obj.pumb_usd_case)
        self.canv.itemconfig(self.bank_usd_sale, text=self.pumb_obj.pumb_usd_sale)
        self.canv.itemconfig(self.bank_eur_case, text=self.pumb_obj.pumb_eur_case)
        self.canv.itemconfig(self.bank_eur_sale, text=self.pumb_obj.pumb_eur_sale)        
        self.canv.itemconfig(self.bank_rur_case, text=self.pumb_obj.pumb_rur_case)
        self.canv.itemconfig(self.bank_rur_sale, text=self.pumb_obj.pumb_rur_sale)
        self.canv.pack()
        
    
    def version(self):
        """
        Модуль виведення версії програми
        """
        try:
            showinfo('ProCourse', 'Version 1.0\nby Serhii Yaroshevskyi')
        except:
            pass
    
    def save_csv(self):
        """
        Модуль збереження курсів валют у файлі CSV
        """
        path = asksaveasfilename(initialfile='courses.csv')   
        try:
            with open(path, 'w') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(('Банк', "Валюта", "Покупка", "Продажа"))           
                courses=[]
                for lst in self.aval_obj.a, self.oshchad_obj.b, self.privat_obj.c, self.pumb_obj.d:
                    courses.extend(lst)
                writer.writerows((course['bank'], course['name'], course['case'], course['sale']) for course in courses)         
        except:
            pass
        
    def close_win(self):
        """
        Модуль закриття вікна
        """
        if not askyesno("Вихід", "Ви хочете завершити роботу з програмою?"):
            pass
        else:
            root.destroy()

        

root = Tk()
app = MainMenu()
app.menu()
root.mainloop()