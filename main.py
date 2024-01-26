from web_page import create_app, create_database
from web_page.auth import login_manager

app = create_app()
create_database(app=app)
login_manager.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, extra_files=['web_page/auth.py'])
