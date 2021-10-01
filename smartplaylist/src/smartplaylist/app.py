"""
A Spotify app that creates group playlists based on a set of user's selected playlists.
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

import config


class SmartPlaylist(toga.App):

    # ------------- control_box -----------------------------------
    def btn_play_pressed():
        None

    def btn_copy_pressed():
        None

    def btn_create_pressed():
        None

    def btn_fetch_pressed():
        None

    # ------------- dbedit_box -----------------------------------
    def btn_add_pressed():
        None

    def btn_update_pressed():
        None

    def btn_remove_pressed():
        None

    # ------------- Client_box -----------------------------------
    def btn_login_pressed():
        None


    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        config.configRunner()

        main_box = toga.Box(style=Pack(direction=COLUMN))

        # >>>>>>>>>>>>>>>>>>>>>>> Control Box <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        control_box = toga.Box(style=Pack(direction=ROW, padding=5))

        btn_play = toga.Button(
            'Play',
            on_press=self.btn_play_pressed,
            style=Pack(padding=5)
        )
        btn_copy = toga.Button(
            'Copy',
            on_press=self.btn_copy_pressed,
            style=Pack(padding=5)
        )
        btn_create = toga.Button(
            'Create',
            on_press=self.btn_create_pressed,
            style=Pack(padding=5)
        )
        btn_fetch = toga.Button(
            'Fetch',
            on_press=self.btn_fetch_pressed,
            style=Pack(padding=5)
        )

        control_box.add(btn_play)
        control_box.add(btn_copy)
        control_box.add(btn_create)
        control_box.add(btn_fetch)


        # >>>>>>>>>>>>>>>>>>>>>>> Users Box <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        users_box = toga.Box(style=Pack(direction=COLUMN, padding=5))

        testl = []
        x = 1
        while x < 4:
            testl.append(toga.Switch("number " + str(x)))
            x += 1
        # input = toga.Switch("")
        for x in testl:
            users_box.add(x)

        print(users_box.children)

        if users_box.children[0].is_on == False:
            print("Yesss")
        

        # >>>>>>>>>>>>>>>>>>>>>>> Entry Box <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        entry_box = toga.Box(style=Pack(direction=ROW, padding=5))
        
        txt_user = toga.TextInput(placeholder='enter name here')
        txt_plistid = toga.TextInput(placeholder='enter playlist id here')

        entry_box.add(txt_user)
        entry_box.add(txt_plistid)



        # >>>>>>>>>>>>>>>>>>>>>>> dbedit Box <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        dbedit_box = toga.Box(style=Pack(direction=ROW, padding=5))

        btn_add = toga.Button(
            'Add',
            on_press=self.btn_add_pressed,
            style=Pack(padding=5)
        )
        btn_update = toga.Button(
            'Update',
            on_press=self.btn_update_pressed,
            style=Pack(padding=5)
        )
        btn_remove = toga.Button(
            'Remove',
            on_press=self.btn_remove_pressed,
            style=Pack(padding=5)
        )

        dbedit_box.add(btn_add)
        dbedit_box.add(btn_update)
        dbedit_box.add(btn_remove)
    
        # >>>>>>>>>>>>>>>>>>>>>>> Client Box <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        client_box = toga.Box(style=Pack(direction=ROW, padding=5))

        txt_client = toga.PasswordInput()
        txt_secret = toga.PasswordInput()

        btn_login = toga.Button(
            'login',
            on_press=self.btn_login_pressed,
            style=Pack(padding=5)
        )

        client_box.add(txt_client)
        client_box.add(txt_secret)
        client_box.add(btn_login)
        


        main_box.add(control_box)
        main_box.add(toga.Divider())
        main_box.add(users_box)
        main_box.add(entry_box)
        main_box.add(dbedit_box)
        main_box.add(toga.Divider())
        main_box.add(client_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return SmartPlaylist()
