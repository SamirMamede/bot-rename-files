
from botcity.core import DesktopBot

class Bot(DesktopBot):
    def action(self, execution=None):
        self.browse("C:/Users/Anuar/Documents/arquivos_recebidos")


        self.wait(1000)

        self.type_down()
        self.type_up()

        id = 0
        previous_name = None

        while True:

            self.key_f2()
            self.control_c()
            name_file = self.get_clipboard()
            name_standard = name_file.capitalize()

            if previous_name == name_standard:
                self.key_esc()
                self.alt_f4()
                break

            self.kb_type(name_standard + " " + str(id))
            self.enter()
            self.type_down()

            
            previous_name = name_standard + " " + str(id)
            id += 1



    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
