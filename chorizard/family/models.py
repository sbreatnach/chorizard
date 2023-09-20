import enum

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import UniqueConstraint
from django.utils.translation import gettext_lazy as _


class Relation(enum.Enum):
    Parent = "parent"
    Child = "child"

    @classmethod
    def db_choices(cls):
        return [(relation.value, _(f"relation.{relation.value}")) for relation in cls]


class Family(models.Model):
    name = models.CharField(max_length=255)

    def get_related_users(self, relation: Relation):
        query = self.relations.filter(relation=relation.value).select_related("user")
        return [relation.user for relation in query]

    @property
    def parents(self):
        return self.get_related_users(Relation.Parent)

    @property
    def children(self):
        return self.get_related_users(Relation.Child)


class User(AbstractUser):
    families = models.ManyToManyField(
        Family, related_name="members", through="FamilyRelation"
    )


class FamilyRelation(models.Model):
    class Meta:
        constraints = [
            UniqueConstraint(fields=["user", "family"], name="family_user_relation")
        ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="relations")
    family = models.ForeignKey(
        Family, on_delete=models.CASCADE, related_name="relations"
    )
    relation = models.CharField(max_length=255, choices=Relation.db_choices())
