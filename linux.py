import keyboard
import pyautogui


class EasyClicker:
    platform = 'Linux'

    def __init__(self):
        self.__enabled = False
        self.x = None
        self.y = None
        pyautogui.alert('Средней кнопкой мыши через Control установи место для кликов\n'
                        'Процесс генерации кликов завершается аналогичным образом - '
                        '[Control + Средняя кнопка мыши]', 'easyClicker', 'Понятно, спасибо')

    def run(self):
        keyboard.add_hotkey('alt+c', self.hotkey_handler)
        keyboard.wait()

    def hotkey_handler(self):
        self.x, self.y = pyautogui.position()
        pyautogui.alert(f'alt c - {self.current_pos}')

    @property
    def current_pos(self):
        return self.x, self.y


