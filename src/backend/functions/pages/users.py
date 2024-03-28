#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.backend.manager import app, render_template


@app.route("/users/<user_name>")
def usuarios(user_name):
    return render_template("users.html", user_name=user_name)
