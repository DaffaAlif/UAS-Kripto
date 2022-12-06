from optparse import Values
import PySimpleGUI as sg
import packages.decrypt_gui as decrypt_gui

def create_popup(password, user_uname, user_pass, user_key):
    popup_password_layout = [
        [sg.Text("Password : ")],
        [sg.Input(key="-IN-popup", do_not_clear=True, size=(20,1))],
        [sg.OK()]
    ]

    popup_password_layout_window = sg.Window("Input", popup_password_layout)
    
    while True:
        event, values = popup_password_layout_window.read()
        if event in (sg.WIN_CLOSED, "Exit"):
            break
        elif event == 'OK':
            if values['-IN-popup'] == password:
                key = 0
                if user_key == "true":
                    key =  int(sg.popup_get_text("Masukkan Key : "))
                elif user_key == "false":
                    key = None
                decrypt_gui.create_popup(user_uname, user_pass, key)
                popup_password_layout_window.close()
                break
            else :
                sg.popup("password salah")

    popup_password_layout_window.close()