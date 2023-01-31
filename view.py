from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
matplotlib.use('TkAgg')

class View:
    def __init__(self):
        """This constructor init all objects in the window"""

        image_viewer = [
            [sg.Text("Choisir la date ",size=(10,1), font ="Lucida",text_color="black"), sg.InputText(key='-DISPLAY_DATE-', enable_events=True), sg.CalendarButton("Select Date", close_when_date_chosen=True, target="-DISPLAY_DATE-", format='%m/%Y', size=(10,1))],
            #[sg.Text(key="-PATH-",size=(60,1), font ="Lucida", background_color = "white",text_color="black")],
            [sg.Image(key='-IMAGE-', size=(5000, 100), expand_x=True, expand_y=True)]
        ]

        self.f = np.loadtxt('./.personel.txt', dtype=[('Names', "U12"), ("JoursRestant", "i4")], delimiter=";")
        self.name_list = self.f['Names']

        parameters = [
            [sg.Text("Nom :", size=(5,1), font="Lucida", text_color="black"), sg.Combo([name for name in self.name_list], key='-NAME-')],
            #[],
            [sg.Text("Date :", size=(5, 1), font="Lucida", text_color="black"), sg.InputText(size=(7, 1), key='-DATE-'), sg.CalendarButton("Select Date", close_when_date_chosen=True, target="-DATE-", format='%d/%m/%Y', size=(10,1))],
            #[],
            #[sq.Text("Au :", size=(10, 1), font="Lucida", text_color="black"), sg.InputText(key='-END-'), sg.CalendarButton("Select Date", close_when_date_chosen=True, target="Date", format='%d/%m/%Y', size=(10,1))],
            [sg.Text("Durée :", size=(5, 1), font="Lucida", text_color="black"), sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], default_value=1, key="-DAYS-"), sg.Text("jour(s)", size=(10, 1), font="Lucida", text_color="black")],
            #[],
            [sg.Text("Type: ", size=(5, 1), font="Lucida", text_color="black"), sg.Combo(["congé", "maladie", "demi jour de congé", "récup","récup de l'année précédente","jour férié","quatre cinquième","convention","accouchement","quarantaine"], default_value="congé", size=(10,1), key='-TYPE-')],
            #[],
            [sg.Button("Ajouter", key='-ADD-'), sg.Button("Supprimer", key='-REMOVE-')]
        ]

        # buttons = [
        #     [sg.Button("Ajouter", key='-ADD-'), sg.Button("Supprimer", key='-REMOVE-')]
        # ]

        layout = [
            [sg.Column(image_viewer), sg.Column(parameters)]
        ]

        self.window = sg.Window("Gestionnaire de congés", layout, finalize=True, resizable=True)

    def draw_figure(self, figure):
        try:
            self.window["-IMAGE-"].update(figure)
        except :
            return "Une erreur s'est produite en changeant d'image."
    


if __name__ == "__main__":
    view = View()
    #print(view.name_list)
    while True:
        event, values = view.window.read()
        if event == sg.WIN_CLOSED:
            break
    view.window.close()
