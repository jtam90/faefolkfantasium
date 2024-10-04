from faefolkfantasium import db

class EtherealBeing(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each being
    name = db.Column(db.String(100), nullable=False)  # Name of the being
    description = db.Column(db.Text, nullable=False)  # Description of the being
    type = db.Column(db.String(50), nullable=False)  # Type (e.g., faerie, elf)

    def __repr__(self):
        return f'<EtherealBeing {self.name}>'
