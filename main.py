#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.backend.manager import app
# noinspection PyUnresolvedReferences
from src.backend.function_manager import *


if __name__ == "__main__":
    app.run(debug=True)

    # To deploy: Not use Heroku web server (paid), use Railway or Render (free).
