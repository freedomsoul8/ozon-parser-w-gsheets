from telebot import types



class Buttons:

    UPDATE_BT = types.KeyboardButton(text = "Update Data")

    class Data:

        UPDATE_BT = "Update Data"

    data = Data()

buttons = Buttons()

class Keyboards:

    def home_keyboard(self):
        HOME_KB = types.ReplyKeyboardMarkup(resize_keyboard=True)
        HOME_KB.add(buttons.UPDATE_BT)

        return HOME_KB

keyboards = Keyboards()