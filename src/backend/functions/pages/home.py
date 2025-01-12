#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.backend.manager import app, render_template


@app.route("/")
def homepage():
    return render_template("homepage.html")
