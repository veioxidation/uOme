import os
import configparser
import json
from SingleEntry import SingleEntry


class EntryRegistry:
    def __init__(self, filename='entries.json'):
        self.file = filename
        self.entries = []

    def SetPath(self, path):
        self.file = path

    def AddEntry(self, entry):
        self.entries.append(entry)

    def ExportRegistry(self, ):
        file = open(self.file, 'w+')
        entry_list = []
        for entry in self.entries:
            entry_list.append(entry.__dict__)
        json.dump(entry_list, file)