import graphene
from user.models import User 
from user.graphql.types import UserBasicObj
from user.graphql.inputs import userCreationInput 



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
                user.save()
                return UserCreationResponse(success=True, returning=user)


class Mutation(graphene.ObjectType):
        createUser = CreateUser.Field()

__all__ = [
        'Mutation',
]
