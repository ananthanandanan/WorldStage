import graphene
from user.models import User


class UserBasicObj(
    graphene.ObjectType,
    description='the user type'
):
    id = graphene.ID() 
    firstName = graphene.String()
    lastName = graphene.String()
    city = graphene.String()
    phoneNo = graphene.String()
    
    
    def resolve_id(self, info):
        if isinstance(self, User):
            return self.id
    def resolve_firstName(self, info):
        if isinstance(self, User):
            return self.first_name
    def resolve_lastName(self, info):
        if isinstance(self, User):
            return self.last_name
    def resolve_city(self, info):
        if isinstance(self, User):
            return self.city
    def resolve_phoneNo(self, info):
        if isinstance(self, User):
            return self.phone