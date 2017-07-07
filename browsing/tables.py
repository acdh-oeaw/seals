import django_tables2 as tables
from django_tables2.utils import A
from tablets.models import Tablet, Seal


class TabletTable(tables.Table):
    id = tables.LinkColumn(
        'tablets:tablet_detail', args=[A('pk')])

    class Meta:
        model = Tablet
        fields = ['cdli_no', 'place', 'archive']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class SealTable(tables.Table):
    id = tables.LinkColumn(
        'tablets:seal_detail', args=[A('pk')])

    class Meta:
        model = Seal
        fields = ['owner', 'seal_type', 'seal_motive', 'seal_position']
        attrs = {"class": "table table-hover table-striped table-condensed"}
