from app import app

@app.route('/')
@app.route('/index')
def index():
    return "<center><b>KAIXO TEAM !!!</b></center>"