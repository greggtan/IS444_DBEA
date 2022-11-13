from schemas.shared_model import ma
from models.UserModel import User



#User Schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk =True

#User with Bank Accounts Schema
class UserWithBankAccountsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk =True
    bankAccounts = ma.Nested("BankAccountSchema", many=True)

#User with Billing Organizations Schema
class UserWithBillingOrganizationsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk =True
    userBillingOrganizations = ma.Nested("UserBillingOrganizationSchema", many=True)