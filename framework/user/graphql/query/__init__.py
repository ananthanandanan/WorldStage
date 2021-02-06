import graphene
from user.models import User
from user.graphql.types import UserBasicObj

class UserQuery(graphene.ObjectType):
    users = graphene.List(UserBasicObj)
    
    def resolve_users(self, info):
        return User.objects.all()
    
    
    
__all__ = [
    'UserQuery'
]