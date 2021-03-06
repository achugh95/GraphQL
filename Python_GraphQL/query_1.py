import graphene
import json


class Query(graphene.ObjectType):
    is_staff = graphene.Boolean()

    def resolve_is_staff(self, info):
        return True

schema = graphene.Schema(query=Query, auto_camelcase=False)

result = schema.execute(
    '''
    {
        is_staff
    }
    '''
)

items = dict(result.data.items())
print(json.dumps(items, indent=4))