from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db import models
from web.item_model import ItemModel

class Account(ItemModel):
    collection_name = 'account'

    owner = models.ForeignKey(User, related_name='accounts')
    creation = models.DateTimeField(auto_now_add=True)
    level = models.PositiveIntegerField(_("Level"), null=True)

    def __unicode__(self):
        return u'#{} Level {}'.format(self.id, self.level)
