import graphene


class userCreationInput(graphene.InputObjectType):
    user_id = graphene.ID()
    email = graphene.String()
    firstName = graphene.String()
    lastName = graphene.String()
    bio = graphene.String()
