# stolen from https://github.c4SublimeFortran/blob/master/InlineDocsHover.py

import sublime
import sublime_plugin

intrinsics = ["BRK","LIT","POP","DUP","SWP","OVR","ROT","EQU","NEQ","GTH","LTH","JMP","JCN","JSR","STH","LDZ","STZ","LDR","STR","LDA","STA","DEI","DEO","ADD","SUB","MUL","DIV","AND","ORA","EOR","SFT"]

class InlineDocsHover(sublime_plugin.EventListener):
    def on_hover(self, view, point, hover_zone):
        if "uxntal" not in view.settings().get('syntax'):
            return
        # if view.settings().get('fortran_disable_docs', False):
        #     return
        if hover_zone != sublime.HOVER_TEXT:
            return
        wordregion = view.word(point)
        word = view.substr(wordregion).upper()[:3]
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