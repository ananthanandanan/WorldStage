import graphene
from user.models import User, EducationInstitution, EmailAddress
from user.graphql.types import UserBasicObj, EducationInstitutionType, EmailAddressType


class UserQuery(graphene.ObjectType):
    users = graphene.List(UserBasicObj)

    def resolve_users(self, info):
        return User.objects.all()


class EducationInstitutionQuery(graphene.ObjectType):
    educationInstitutions = graphene.Field(EducationInstitutionType,
                                           id=graphene.ID(),
                                           description='education type')

    @staticmethod
    def resolve_educationInstitutions(self, info, **kwargs):
        id = kwargs.get('id')
        return EducationInstitution.objects.get(id=id)


class EmailAddressQuery(graphene.ObjectType):
    emailAddress = graphene.Field(EmailAddressType, user=graphene.String(),
                                  description='email addresses of the user')

    def resolve_emailAddress(self, info, **kwargs):
        user = kwargs.get('user')
        print(EmailAddress.objects.filter(user__username=user).values('user_email'))
        return EmailAddress.objects.filter(user__username=user).values('user_email')


__all__ = [
    'UserQuery',
    'EducationInstitutionQuery',
    'EmailAddressQuery'
]
