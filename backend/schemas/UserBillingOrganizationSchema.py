from schemas.shared_model import ma
from models.UserBillingOrganizationModel import UserBillingOrganization



#Bank Account Schema
class UserBillingOrganizationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserBillingOrganization
        include_fk =True