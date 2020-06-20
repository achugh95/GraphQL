import graphene
from sample_app.schema import Query as snippets_query
from sample_app.schema import Mutation as snippets_mutation


class Query(snippets_query):
    pass

class Mutation(snippets_mutation):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
