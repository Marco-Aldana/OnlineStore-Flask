from project import app
from project.setup_project import setup_database


if __name__ == '__main__':
    setup_database()
    app.run()
