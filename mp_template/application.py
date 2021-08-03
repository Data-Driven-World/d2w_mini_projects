from app import application, db
# import all your table model here
from app.models import User

@application.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User}

if __name__ == "__main__":
	application.run(host="0.0.0.0", port=8080, debug=True)
