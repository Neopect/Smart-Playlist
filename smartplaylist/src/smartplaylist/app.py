"""
A Spotify app that creates group playlists based on a set of user's selected playlists.
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import os
from . import config
from . import data_runner

first = True
class SmartPlaylist(toga.App):

    

    # ------------- control_box -----------------------------------
    def btn_play_pressed(self, widget):
        None

    def btn_copy_pressed(self, widget):
        None

    def btn_create_pressed(self, widget):
        usersOn = []
        for x in users_box.children:
            if x.is_on():
                usersOn.append(True)
            else:
                usersOn.append(False)

        data_runner.create(usersOn)


    def btn_fetch_pressed(self, widget):
        None

    # ------------- dbedit_box -----------------------------------
    def btn_add_pressed(self, widget):
        global first
        if first == True:
            data_runner.downloadPlist(config.gPlayl[0], "glob")
            first = False
        lbl_status.text = "Adding user ..."
        config.users.append(txt_plistid.value)
        config.users.append(txt_user.value)
        os.chdir(config.rootConfig)
        fw = open("users", "w")
        fw.close()
        data_runner.downloadPlist(txt_plistid.value, txt_user.value)
        users_box.add(toga.Switch(txt_user))
        users_box.refresh()

    def btn_update_pressed(self, widget):
        None

    def btn_remove_pressed(self, widget):
        None

    # ------------- Client_box -----------------------------------
    def btn_login_pressed(self, widget, id, secret):
        os.chdir(config.rootConfig)
        os.remove("sp")
        fw = open("sp", "w")
        fw.write(id+"\n"+secret)
        fw.close()
        config.spCred[0] = id
        config.spCred[1] = secret
        data_runner.initSP


    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        config.configRunner()
        # data_runner.initSP()

        global users_box

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

        # testl = []
        # x = 1
        # while x < 4:
        #     testl.append(toga.Switch("number " + str(x)))
        #     x += 1
        # # input = toga.Switch("")
        # for x in testl:
        #     users_box.add(x)

        # print(users_box.children)

        # if users_box.children[0].is_on == False:
        #     print("Yesss")
        

        # >>>>>>>>>>>>>>>>>>>>>>> Entry Box <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        entry_box = toga.Box(style=Pack(direction=ROW, padding=5))
        
        global txt_user
        global txt_plistid

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
            on_press=self.btn_login_pressed(txt_client.value, txt_secret.value),
            style=Pack(padding=5)
        )

        client_box.add(txt_client)
        client_box.add(txt_secret)
        client_box.add(btn_login)
        
        global lbl_status
        lbl_status = toga.Label('Started')

        main_box.add(lbl_status)
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
