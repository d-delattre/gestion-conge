from congé import Conge
from data_modifier import File_modifier
from view import View
from datetime import date, timedelta
import time

import PySimpleGUI as sg
import matplotlib.pyplot as plt



def main():
    """C'est la fonction principale qui gère l'interface"""

    vi = View()
    today = date.today()
    year = today.year
    month = today.month
    c = Conge(year, month)
    fm = File_modifier()
    listen = True


    vi.draw_figure(c.fig_maker(c.display_mmatrix()))

    while listen:

        event, values = vi.window.read()

        if event == "-DISPLAY_DATE-":
            plt.close('all')
            month, year = values['-DISPLAY_DATE-'].split('/')
            c = Conge(int(year), int(month))
            fig = c.fig_maker(c.display_mmatrix())
            vi.draw_figure(fig)
            vi.window.Refresh()

        elif event == "-ADD-":
            try:
                dd, mm, yy = values["-DATE-"].split('/')
                i, j = (0,0)
                while j < values["-DAYS-"]:
                    d = date(int(yy), int(mm), int(dd)) + timedelta(days=i)
                    newd = d.day
                    newm = d.month
                    newy = d.year
                    cc = Conge(int(newy), int(newm))
                    if cc.isweekend(newd)==False:
                        fm.add_data(values["-NAME-"], newd, newm, newy, values["-TYPE-"])
                        j+=1
                    i=i+1
                plt.close('all')
                fig = c.fig_maker(c.display_mmatrix())
                vi.draw_figure(fig)
                vi.window.Refresh()
            except:
                pass

        elif event == "-REMOVE-":
            try:
                dd, mm, yy = values["-DATE-"].split('/')
                i, j = (0, 0)
                while j < values["-DAYS-"]:
                    d = date(int(yy), int(mm), int(dd)) + timedelta(days=i)
                    newd = d.day
                    newm = d.month
                    newy = d.year
                    cc = Conge(int(newy), int(newm))
                    if cc.isweekend(newd)==False:
                        fm.remove_data(values["-NAME-"], newd, newm, newy, values["-TYPE-"])
                        j+=1
                    i+=1
                plt.close('all')
                fig = c.fig_maker(c.display_mmatrix())
                vi.draw_figure(fig)
                vi.window.Refresh()
            except:
                pass


        elif event == sg.WIN_CLOSED:
            listen = False


if __name__ == "__main__":
    main()
