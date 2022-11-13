import datetime
from models.shared_model import db

#User Class/Model
class Request(db.Model):
    __tablename__ = 'request'
    requestID = db.Column(db.Integer, primary_key=True)
    GMSAccountID = db.Column(db.String(10), db.ForeignKey('user.GMSAccountID'))
    bankAccountID = db.Column(db.String(10))
    billingOrganizationAccountID = db.Column(db.String(10))
    transactionAmount = db.Column(db.Float)
    transactionReferenceNumber = db.Column(db.String(100))
    narrative = db.Column(db.String(100))
    status = db.Column(db.String(10))
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, GMSAccountID, bankAccountID, billingOrganizationAccountID, transactionAmount, transactionReferenceNumber, narrative, status):
        self.GMSAccountID = GMSAccountID
        self.bankAccountID = bankAccountID
        self.billingOrganizationAccountID = billingOrganizationAccountID
        self.transactionAmount = transactionAmount
        self.transactionReferenceNumber = transactionReferenceNumber
        self.narrative = narrative
        self.status = status
    


