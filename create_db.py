from main import app, db  

with app.app_context():
    db.create_all()


# you can see your data in sqlite viewer