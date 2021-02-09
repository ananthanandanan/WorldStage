import graphene
from user.models import User, EmailAddress
from user.graphql.types import UserBasicObj
from user.graphql.inputs import userCreationInput 
from framework.api.API_Exceptions import APIException



class UserCreationResponse(graphene.ObjectType):
        success = graphene.Boolean()
        returning = graphene.Field(UserBasicObj)


class CreateUser(graphene.Mutation,
        description='create a user'):
        class Arguments:
                inputs = graphene.Argument(userCreationInput,
                                        required=True,
                                        description='inputs available for creation')
                password = graphene.String(required=True)
                username = graphene.String(required=True)
        Output = UserCreationResponse 
        
        def mutate(self, info, inputs: userCreationInput, password,
                username):
                user = User.objects.create(username=username, email=inputs.email,
                is_active=True)

                user.set_password(password)
                user.bio = inputs.bio
                EmailAddress.objects.create(user=user, 
                                        user_email=inputs.email,
                                        is_primary=True)
                user.save()
                return UserCreationResponse(success=True, returning=user)


class AddEmailAddress(graphene.Mutation,
                description='Add new email to user'):
        class Arguments:
                email = graphene.String(required=True,
                                description='New email to be added')
        Output = graphene.Boolean

        def mutate(self, info, email) -> bool:
                user = info.context.user
                EmailAddress.objects.create(user=user, 
                                user_email=email)
                return True


class SwitchUserEmail(graphene.Mutation,
                description='switch between user email-addresses'):
        class Arguments:
                email = graphene.String(required=True,
                                        description='email to set as primary')
        Output = graphene.Boolean
        
        def mutate(self, info, email) -> bool:
                email_obj = EmailAddress.objects.get(user_email=email)
                if email_obj is not None:
                        email_obj.set_primary()
                        return True
                else:
                        raise APIException('Wrong email address passed', code='INVALID_EMAIL')
                
class Mutation(graphene.ObjectType):
        createUser = CreateUser.Field()
        swithcUSerEmail = SwitchUserEmail.Field()
        addEmailAddress = AddEmailAddress.Field()

__all__ = [
        'Mutation',
]
