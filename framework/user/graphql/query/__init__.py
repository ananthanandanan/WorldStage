import graphene
from user.models import User, EducationInstitution 
from user.graphql.types import UserBasicObj, EducationInstitutionType

class UserQuery(graphene.ObjectType):
    users = graphene.List(UserBasicObj)
    
    def resolve_users(self, info):
        return User.objects.all()
    
 
class EducationInstitutionQuery(graphene.ObjectType):
    educationInstitutions = graphene.Field(EducationInstitutionType,
            name= graphene.String(),
            description='education type')

    def resolve_educationInstitutions(self, info, **kwargs):
        name = kwargs.get('name')
        return EducationInstitution.objects.get(name=name)
    
__all__ = [
    'UserQuery',
    'EducationInstitutionQuery'
]
