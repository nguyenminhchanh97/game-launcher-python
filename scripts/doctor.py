import sys, platform
print("Python:", sys.version.split()[0], "| Platform:", platform.platform())

# PySide6
try:
    import PySide6
    from PySide6.QtWidgets import QApplication, QLabel
    print("PySide6:", PySide6.__version__)
except Exception as e:
    print("PySide6 import FAIL:", e)

# psutil
try:
    import psutil
    print("psutil:", psutil.__version__, "| CPU count:", psutil.cpu_count())
except Exception as e:
    print("psutil import FAIL:", e)

# pydantic
try:
    import pydantic
    print("pydantic:", pydantic.__version__)
except Exception as e:
    print("pydantic import FAIL:", e)

# appdirs
try:
    import appdirs
    print("appdirs:", appdirs.__version__)
except Exception as e:
    print("appdirs import FAIL:", e)

# requests
try:
    import requests
    print("requests:", requests.__version__)
except Exception as e:
    print("requests import FAIL:", e)

print("OK: doctor ran.")
