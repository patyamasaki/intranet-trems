from intranet_trems import _
from plone import api
from plone.dexterity.content import Container
from plone.supermodel import model
from plone.supermodel.model import Schema
from zope import schema
from zope.interface import implementer


class IArea(Schema):
    """Definição de uma area no TRE-MS."""

    title = schema.TextLine(title=_("Nome área"), required=True)
    description = schema.Text(title=_("Descrição"), required=False)


@implementer(IArea)
class Area(Container):
    """Uma area no TRE-MS."""

    @property
    def pessoas(self):
        """Lista de pessoas conectadas a esta área."""
        relations = api.relation.get(target=self, relationship="area")
        return [i.from_object for i in relations]
