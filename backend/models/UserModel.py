from models.shared_model import db

#User Class/Model
class User(db.Model):
    __tablename__ = 'user'
    GMSAccountID = db.Column(db.String(10), primary_key=True)
    bankAccounts = db.relationship('BankAccount', backref='user', lazy=True)
    userBillingOrganizations = db.relationship('UserBillingOrganization', backref='user', lazy=True)

    def __init__(self, GMSAccountID):
        self.GMSAccountID = GMSAccountID
    

