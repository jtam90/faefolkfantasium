from faefolkfantasium import db

class Being(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    is_example = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Being {self.name}>"


