from models.shared_model import db

#UserBillingOrganization Class/Model
class UserBillingOrganization(db.Model):
    __tablename__ = 'userBillingOrganization'
    billingOrganizationAccountID = db.Column(db.String(10), primary_key=True)
    GMSAccountID = db.Column(db.String(10), db.ForeignKey('user.GMSAccountID'), primary_key=True)
    bankAccountID = db.Column(db.String(10), db.ForeignKey('bankAccount.bankAccountID'),nullable = False)
    
    def __init__(self, billingOrganizationAccountID, GMSAccountID, bankAccountID):
        self.billingOrganizationAccountID = billingOrganizationAccountID
        self.GMSAccountID = GMSAccountID
        self.bankAccountID = bankAccountID


    


