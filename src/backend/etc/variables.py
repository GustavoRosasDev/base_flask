#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.backend.manager import Flask

app = Flask(__name__, template_folder='../../../templates')
