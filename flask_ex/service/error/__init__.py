from flask import render_template

def not_found(error):
    return render_template('404.html',error=str(error))