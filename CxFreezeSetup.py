import sys
from cx_Freeze import setup, Executable

base = None

includes = ["pyxel", "random", "re", "math", "webbrowser", "urllib.parse"]
excludes = ["pandas", "numpy", "tkinter", "html", "email",
            "xml", "pydoc_data", "xmlrpc", "PyQt4", "PyQt5","concurrent","multiprocessing","unittest","http"]
if sys.platform == "win32":
    base = "Win32GUI"
exe = Executable(script = "game.py", base= base)

setup(
    name = '',
    version='',
    options={"build_exe": {"includes": includes, "excludes": excludes,'include_files':["assets/"],"optimize": 2}},
    executables = [exe])
