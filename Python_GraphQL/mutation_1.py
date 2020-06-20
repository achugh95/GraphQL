import graphene
import json
from datetime import datetime

class User(graphene.ObjectType):
    id          = graphene.ID()
    username    = graphene.String()
    last_login  = graphene.DateTime(required=False)


class CreateUser(graphene.Mutation):

    class Arguments:
        username = graphene.String()

    user = graphene.Field(User)

    def mutate(self, info, username):
        if info.context.get('is_vip'):
            username = username.upper()
        user = User(username=username)
        return CreateUser(user=user)



class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(mutation=Mutations, auto_camelcase=False)

result = schema.execute(
    '''
    mutation createUser($username: String) {
        create_user(username : $ username){
            user {
                username
            }
        }
    }
    ''',
    variable_values = {'username': 'Anshul'},
    context         = {'is_vip': True}
)

items = dict(result.data.items())
print(json.dumps(items, indent=4))