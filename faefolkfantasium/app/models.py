from . import db  # Assuming `db` is initialized in `faefolkfantasium/app/__init__.py`



class Being(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Being {self.name}>"


