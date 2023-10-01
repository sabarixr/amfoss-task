import json
import os

from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QMessageBox,\
    QDialog

import requests


class SearchWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self):
        super().__init__()

        self.w = None
        self.setFixedSize(850, 500)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.setGeometry(50, 50, 280, 40)

        text_layout = QVBoxLayout()

        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 5, 600, 70)

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)
        enter_button.clicked.connect(self.poke_info)

        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        capture_button.clicked.connect(self.capture_pokemon)

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        display_button.clicked.connect(self.display_captured_pokemon)

        self.image = QLabel(self)
        self.image.setGeometry(400, 10, 275, 275)

        main_layout = QHBoxLayout()
        main_layout.addLayout(text_layout)
        main_layout.addWidget(self.image)

        self.info_area = QTextEdit(self)
        self.info_area.setGeometry(400, 300, 300, 200)
        self.info_area.setReadOnly(True)

        self.captured_pokemon_list = []
        self.current_pokemon_index = 0

        self.dialog = QDialog(self) 
        self.dialog.setWindowTitle("Captured Pokemon List")
        self.dialog.setGeometry(100, 100, 400, 300)
        self.dialog.hide() 

        layout = QVBoxLayout()

        self.label = QLabel(self.dialog) 
        layout.addWidget(self.label)

        self.image_label_display = QLabel(self.dialog) 
        layout.addWidget(self.image_label_display)

        # Navigation buttons
        past_pkmn = QPushButton("<", self.dialog)
        past_pkmn.clicked.connect(self.prev_pokemon)
        next_pkmn = QPushButton(">", self.dialog)
        next_pkmn.clicked.connect(self.next_pokemon)
        windw_layout = QHBoxLayout()
        windw_layout.addWidget(past_pkmn)
        windw_layout.addWidget(next_pkmn)
        layout.addLayout(windw_layout)

        self.dialog.setLayout(layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        background = QPixmap('../assets/landing.jpg')
        painter.drawPixmap(self.rect(), background)

    def poke_info(self):
        pokemon = self.textbox.text()
        data = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
        ock = json.loads(data.text)

        # print("Received data:", ock)
        if data.status_code != 200:

            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText(f"There's no pokemon with the name you have entered")
            msg.exec_()
            return


        sprite_url = ock['sprites']['front_default']
        pixmap = QPixmap()
        pixmap.loadFromData(requests.get(sprite_url).content)

        pixmap = pixmap.scaled(275, 275)
        self.image.setPixmap(pixmap)
        # I had to google a lot for this and the background:'(
        name = ock['name']
        abilities = [ability['ability']['name'] for ability in ock['abilities']]
        types = [type_['type']['name'] for type_ in ock['types']]
        stats = {stat['stat']['name']: stat['base_stat'] for stat in ock['stats']}

        result_text = f'Name: {name}\n'
        result_text += f'Abilities: {", ".join(abilities)}\n'
        result_text += f'Types: {", ".join(types)}\n'
        result_text += 'Stats:\n' + '\n'.join([f'{key}: {value}' for key, value in stats.items()])

        self.info_area.setText(result_text)
        # due to time limit i choose to go with list i dont have time to check for any other option as the deadline
        # is really near

    def capture_pokemon(self):
        global sprite_url
        pokemon_name = self.textbox.text()
        data = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
        if data.status_code == 200:
            pokemon_data = json.loads(data.text)
            sprite_url = pokemon_data['sprites']['front_default']

        if sprite_url:
            response = requests.get(sprite_url)
            if response.status_code == 200:
                if not os.path.exists('captured_pokemon_images'):
                    os.makedirs('captured_pokemon_images')

                image_path = f'captured_pokemon_images/{pokemon_name}.png'

                with open(image_path, 'wb') as image_file:
                    image_file.write(response.content)

                self.captured_pokemon_list.append(
                    {
                        'image_path': image_path,
                        'name': pokemon_name,
                    }
                )

                msg = QMessageBox()
                msg.resize(400, 200)
                msg.setWindowTitle("Capture Success")
                msg.setText(f"You have captured {pokemon_name}!")
                msg.exec_()

    def display_captured_pokemon(self):
        if not self.captured_pokemon_list:
            return

        self.dialog.show()

        if self.current_pokemon_index < 0:
            self.current_pokemon_index = len(self.captured_pokemon_list) - 1
        elif self.current_pokemon_index >= len(self.captured_pokemon_list):
            self.current_pokemon_index = 0

        captured_pokemon = self.captured_pokemon_list[self.current_pokemon_index]

        image_path = captured_pokemon['image_path']
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaledToWidth(300) 
        self.image_label_display.setPixmap(pixmap)
        self.label.setText(captured_pokemon['name'])

    def prev_pokemon(self):
        self.current_pokemon_index -= 1
        self.display_captured_pokemon()

    def next_pokemon(self):
        self.current_pokemon_index += 1
        self.display_captured_pokemon()

   # i may made the code a little complicated as i google the problems i face at a specific time and corrected that  part...
   # i needed to learn more about file reading stuffs in python to make the third function work i am speaking about the display button so i used list but the image will get 
   # dowloaded anyway


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
