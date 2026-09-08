from enum import Enum

from textual_textarea.text_editor import TextAreaPlus

class Mode(str, Enum):
    NORMAL = "NORMAL"
    INSERT = "INSERT"
    VISUAL = "VISUAL"
    VISUAL_LINE = "V-LINE"
    COMMAND = "COMMAND"

class VimTextAreaPlus(TextAreaPlus):
    mode: Mode
