from fileinput import close
import PySimpleGUI as sg
import string
import packages.popup_password_gui as popup_password_gui
import packages.cipher as cp

password = 'passworddibalik'
acc_info_arr = []
headings = ['Platform','Email', 'Username', 'Password', 'Key']

layout  = [
    [sg.Text("Mengenkripsi dan Dekripsi Kredensial Login Akun Anda ")],
    [sg.Text("Platform   : "), sg.Input(key="-IN-Platform", do_not_clear=True, size=(20,1))],
    [sg.Text("Email       : "), sg.Input(key="-IN-Email", do_not_clear=True, size=(30,1))],
    [sg.Text("Username : "), sg.Input(key="-IN-Username")],
    [sg.Text("Password : "), sg.Input(key="-IN-Pass")],
    [sg.Radio("Shift-Cipher", "RADIO", key="-IN-Shift-Cipher"), sg.Radio("Triangle-Cipher", "RADIO", key="-IN-Triangle-Cipher", default=True)],
    [sg.Button("Submit")],
    [sg.Table(values=acc_info_arr, headings = headings, max_col_width=35
        , auto_size_columns=True,
        display_row_numbers = True,
        num_rows = 10,
        key="-TABLE-Acc",
        tooltip="Acc Table")],
    [sg.Button("Decrypt!"), sg.Button("Delete!")]
]

window = sg.Window('Your Login Credentials Database', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Exit"):
        break

    elif event == "Submit":
        val = "true"
        enc = [values['-IN-Username'], values['-IN-Pass']]
        if values['-IN-Username'] == "" and values['-IN-Pass'] == "" :
            sg.popup_error("username atau password tidak diisi!")
        else : 
            if values["-IN-Shift-Cipher"]:
                key = int(sg.popup_get_text("Masukkan Key : "))
                for i in range(0, len(enc)):
                    enc[i] = cp.shift_cipher(enc[i], key, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation])
                acc_info = [values['-IN-Platform'], values['-IN-Email']] + enc + [val]
            else :
                val = "false"
                for i in range(0, len(enc)):
                    enc[i] = cp.tricipherenc(enc[i])
            acc_info = [values['-IN-Platform'], values['-IN-Email']] + enc + [val]
            acc_info_arr.append(acc_info)
            window["-TABLE-Acc"].update(acc_info_arr)
        window["-IN-Platform"].update("")
        window["-IN-Email"].update("")
        window["-IN-Username"].update("")
        window["-IN-Pass"].update("")

    elif event == "Decrypt!":
        selected_row_index = values["-TABLE-Acc"][0]
        user_info = acc_info_arr[selected_row_index]
        user_uname = user_info[2]
        user_pass = user_info[3]
        user_key = user_info[4]
        popup_password_gui.create_popup(password, user_uname, user_pass, user_key)

    elif event == "Delete!":
        if values["-TABLE-Acc"] == []:
            sg.popup("Tidak ada data yang dipilih!")
        else:
            del acc_info_arr[values["-TABLE-Acc"][0]]
            window["-TABLE-Acc"].update(acc_info_arr)