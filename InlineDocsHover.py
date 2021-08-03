# stolen from https://github.com/315234/SublimeFortran/blob/master/InlineDocsHover.py

import sublime
import sublime_plugin

real_intrinsics = ["BRK", "BRK2", "LIT", "LIT2", "POP", "POP2", "DUP", "DUP2", "SWP", "SWP2", "OVR", "OVR2", "ROT", "ROT2", "EQU", "EQU2", "NEQ", "NEQ2", "GTH", "GTH2", "LTH", "LTH2", "JMP", "JMP2", "JCN", "JCN2", "JSR", "JSR2", "STH", "STH2", "LDZ", "LDZ2", "STZ", "STZ2", "LDR", "LDR2", "STR", "STR2", "LDA", "LDA2", "STA", "STA2", "DEI", "DEI2", "DEO", "DEO2", "ADD", "ADD2", "SUB", "SUB2", "MUL", "MUL2", "DIV", "DIV2", "AND", "AND2", "ORA", "ORA2", "EOR", "EOR2", "SFT", "SFT2"]

intrinsics = ["DEO"]

class InlineDocsHover(sublime_plugin.EventListener):
    def on_load(self, view):
        sublime.message_dialog("Hello world")

    def on_hover(self, view, point, hover_zone):
        if "uxntal" not in view.settings().get('syntax'):
            return
        # if view.settings().get('fortran_disable_docs', False):
        #     return
        if hover_zone != sublime.HOVER_TEXT:
            return
        wordregion = view.word(point)
        word = view.substr(wordregion).upper()
        self.show_doc_popup(view, point, word)

    def show_doc_popup(self, view, point, word):
        if not word in intrinsics:
            return
        max_width, max_height = 600, 300
        html_str = sublime.load_resource("Packages/sublime-uxntal/minihtml/"+word+".html")
        view.show_popup(html_str,
                        sublime.HIDE_ON_MOUSE_MOVE_AWAY,
                        point,
                        max_width,
                        max_height,
                        lambda s: self.on_navigate(s, view, point),
                        )

    def on_navigate(self, href, view, point):
        # Get function name from URL
        word = href.replace("005f", "").split(".")[0]
        if word in intrinsics:
            self.show_doc_popup(view, point, word)