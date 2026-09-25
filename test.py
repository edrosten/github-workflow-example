import platform
import sys
print(platform.system())
if platform.system() == "Linux":
    sys.exit(1)
