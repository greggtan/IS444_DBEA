from models.shared_model import db

#User Class/Model
class BankAccount(db.Model):
    __tablename__ = 'bankAccount'
    bankAccountID = db.Column(db.String(10), primary_key=True)
    GMSAccountID = db.Column(db.String(10), db.ForeignKey('user.GMSAccountID'), primary_key=True)
    userBillingOrganizations = db.relationship('UserBillingOrganization', backref='bankAccount', lazy=True)

    def __init__(self, bankAccountID, GMSAccountID):
        self.bankAccountID = bankAccountID
        self.GMSAccountID = GMSAccountID

    


