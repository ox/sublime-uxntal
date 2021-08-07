import sublime
import sublime_plugin
import re

class Base(sublime_plugin.TextCommand):
    def run(self, edit):
        regions = self.view.sel()
        for region in regions:
            text = self.view.substr(region)
            self.view.replace(edit, region, self.op(self.sanitize(text)))

    def sanitize(self, text):
        return re.sub(r"([\s\#])", "", text.lower())
    
    def op(self, text):
        return text

class BinToHexCommand(Base):
    def op(self, text):
        return "#{0:04x}".format(int(text, 2))

class HexToBinCommand(Base):
    def op(self, text):
        return " ".join(["{0:08b}".format(int(text[i:i+2], 16)) for i in range(0, len(text), 2)])

class HexToIntCommand(Base):
    def op(self, text):
        return "".join([str(int(text[i:i+2], 16)) for i in range(0, len(text), 2)]).lstrip("0")

class IntToHexCommand(Base):
    def op(self, text):
        return "#{0:02x}".format(int(text))