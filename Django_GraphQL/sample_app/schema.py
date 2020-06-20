import graphene
from graphene_django.types import DjangoObjectType
from . models import Snippet

# Query
class SnippetType(DjangoObjectType):
    class Meta:
        model = Snippet


class Query(graphene.ObjectType):
    all_snippets = graphene.List(SnippetType)

    def resolve_all_snippets(self, info, **kwrgs):
        return Snippet.objects.all()

# Mutation
class SnippetInput(graphene.InputObjectType):
    title   = graphene.String()
    body    = graphene.String()


class CreateSnippet(graphene.InputObjectType):
    
    class Arguments:
        input = SnippetInput(required=True)

    snippet = graphene.Field(SnippetType)

    @staticmethod
    def mutate(root, info, input=None):
        snippet_instance = Snippet(title=input.title, body=input.body)
        snippet_instance.save()
        return CreateSnippet(snippet=snippet_instance)


class Mutation(graphene.ObjectType):
    create_snippet = CreateSnippet.Field()
