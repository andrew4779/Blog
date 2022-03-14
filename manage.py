from xmlrpc.client import Server
from app import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# from app.models import

app = create_app("development")
manager = Manager(app)
manager.add_command("server", Server)



@manager.command
def test():
    """
    Run the unittests
    """
    import unittest
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestResult(verbosity = 2).run(tests)









if __name__== '__main__':
    manager.run()