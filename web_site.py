from user import *
from service import *

app = Flask(__name__)
app.secret_key = 'test'

app.register_blueprint(user)
app.register_blueprint(service)


