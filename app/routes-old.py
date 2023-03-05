# from 

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "<center><h1><b>---------KAIXO TEAM--------</b></h1></center>"