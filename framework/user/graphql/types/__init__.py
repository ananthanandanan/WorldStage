import graphene
from user.models import User, EducationInstitution, EmailAddress
from framework.utils import EDUCATIONAL_INSTITUTION_TYPE


class EducationInstitutionType\
            (graphene.ObjectType,
             description='EducationInstitution type'
             ):
    name = graphene.String()
    isVerified = graphene.Boolean()
    slug = graphene.String()
    type = graphene.String()

    def resolve_name(self, info):
        return self.name

    def resolve_isVerified(self, info):
        return self.isVerified

    def resolve_slug(self, info):
        return self.slug

    def resolve_type(self, info):
        return EDUCATIONAL_INSTITUTION_TYPE[self.type][1]


class UserBasicObj(
    graphene.ObjectType,
    description='the user type'
):
    id = graphene.ID()
    firstName = graphene.String()
    lastName = graphene.String()
    city = graphene.String()
    phoneNo = graphene.String()
    education = graphene.Field(EducationInstitutionType)

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

    def resolve_education(self, info):
        return self.educationInstitution


class EmailAddressType(graphene.ObjectType,
                       description='email address type'):
    userEmails = graphene.List(graphene.String)

    ## [{'user_email': 'thisis1@gmail.com'}, {'user_email': 'thisis2@gmail.com'}, {'user_email': 'hello@gmail.com'}]
    def resolve_userEmails(self, info):
        emails = []
        for e in self:
            emails.append(e['user_email'])
        return emails
