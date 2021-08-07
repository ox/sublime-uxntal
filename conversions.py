import sublime
import sublime_plugin

class Base(sublime_plugin.TextCommand):
    def run(self, edit):
        regions = self.view.sel()
        for region in regions:
            text = self.view.substr(region)
            self.view.replace(edit, region, self.op(text))
    
    def op(self, text):
        return text

class BinToByteCommand(Base):
    def op(self, text):
        return "#{0:02x}".format(int(text.replace(" ", ""), 2))

class BinToShortCommand(Base):
    def op(self, text):
        return "#{0:04x}".format(int(text.replace(" ", ""), 2))

class ByteToBin(Base):
    def op(self, text):
        return "{0:08b}".format(int(text.replace("#", ""), 16))

class ShortToBin(Base):
    def op(self, text):
        text = text.replace("#", "")
        return " ".join(["{0:08b}".format(int(text[i:i+2], 16)) for i in range(0, len(text), 2)])

class IntToByte(Base):
    def op(self, text):
        return "#{0:02x}".format(int(text))