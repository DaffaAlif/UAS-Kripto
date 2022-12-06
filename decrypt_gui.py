import PySimpleGUI as sg
import packages.cipher as cp
import string

def create_popup(user_name, user_pass, key):
    dec_user_name = dec_user_pass = ""
    if isinstance(key,  int):
        dec_user_name = cp.shift_cipher(user_name, 26 - key, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation])
        dec_user_pass = cp.shift_cipher(user_pass, 26 - key, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation])
    else:
        dec_user_name = cp.tricipherdec(user_name)
        dec_user_pass = cp.tricipherdec(user_pass)
    popup_decrypt_layout = [
        [sg.Text("Username : " + dec_user_name)],
        [sg.Text("Password : " + dec_user_pass)],
        [sg.OK()]
    ]

    popup_decrypt_layout_window = sg.Window("Hasil :", popup_decrypt_layout)
    while True:
        event, values = popup_decrypt_layout_window.read()
        if event in (sg.WIN_CLOSED, "Exit"):
            break
        elif event == 'OK':
            break
    popup_decrypt_layout_window.close()
  