from schemas.shared_model import ma
from models.BankAccountModel import BankAccount



#Bank Account Schema
class BankAccountSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BankAccount
        include_fk =True