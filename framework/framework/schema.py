import graphene
import graphql_jwt
from user.graphql.query import UserQuery, EducationInstitutionQuery
from user.graphql.mutations import Mutation as UserMutation

class Query(UserQuery,
            EducationInstitutionQuery):
    pass
    

class Mutation(UserMutation,
        graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()



schema = graphene.Schema(query=Query, mutation=Mutation)
