"""Engine module initialization"""

import sys
import os

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
