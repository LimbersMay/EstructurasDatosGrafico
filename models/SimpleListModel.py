from .templates.list_model_template import ListModelTemplate
from .fichero import Fichero


class SimpleListModel(ListModelTemplate):
    def __init__(self, list_name):
        super().__init__(list_name)

        self.fichero = Fichero("recursos/datos/listas_enlazadas.json")