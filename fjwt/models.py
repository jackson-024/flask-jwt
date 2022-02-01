from fjwt import db

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    date_of_birth = db.Column(db.DateTime(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    msisdn = db.Column(db.Integer, unique=True, nullable=False)
    password = db.Column(db.String(255), unique=True, nullable=False)
    # department_id = db.Column(db.Integer, db.ForeignKey("department.department_id"), nullable=False)
    # message = db.relationship("Messages", backref="users", lazy=True)
    # escalated = db.relationship("EscalatedMessages", backref='users', lazy=True)


    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return self.user_id

    def get_id(self):
        return self.user_id

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    # def __repr__(self):
    #     return f"{self.department_id}"
