from schemas.shared_model import ma
from models.RequestModel import Request



#Request Schema
class RequestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Request
        include_fk =True
