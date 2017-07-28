from django.db import models
from django.contrib.postgres.fields import HStoreField
from django.core.urlresolvers import reverse
from places.models import Place
from vocabs.models import SkosConcept
from bib.models import Book


class Seal(models.Model):
    owner = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="tablet_owner"
    )
    seal_type = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="tablet_sealtype"
    )
    seal_motive = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="tablet_motive"
    )
    seal_position = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="tablet_position"
    )
    reference = models.ManyToManyField(
        Book, blank=True, related_name="tablet_seal_book"
    )
    custom_md = HStoreField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('tablets:seal_detail', kwargs={'pk': self.id})


class Tablet(models.Model):
    place = models.ForeignKey(Place, blank=True, null=True)
    archive = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        help_text="Archiv = Sammlung von Tafeln", related_name='tablet_archive')
    cdli_no = models.CharField(
        max_length=50, blank=True, verbose_name="CDLI no.", help_text="Nummer der Tafel in CDLI")
    nabucco_no = models.CharField(
        max_length=50, blank=True, verbose_name="NABUCCO no.",
        help_text="Nummer der Tafel in NABUCCO")
    museum_no = models.CharField(
        max_length=50, blank=True, verbose_name="Museum Number")
    scribe = models.ForeignKey(
        SkosConcept, blank=True, null=True, help_text="asdf", related_name="tablet_scribe")
    period = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="tablet_period")
    year = models.IntegerField(blank=True, null=True)
    date_not_after = models.IntegerField(blank=True, null=True)
    date_not_before = models.IntegerField(blank=True, null=True)
    babyloneian_time = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="tablet_babyloneian_time")
    date_comment = models.TextField(blank=True, null=True)
    text_type = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="text_type")
    reference = models.ManyToManyField(
        Book, blank=True
    )
    seal = models.ManyToManyField(
        Seal, blank=True
    )
    custom_md = HStoreField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.cdli_no)

    def get_absolute_url(self):
        return reverse('tablets:tablet_detail', kwargs={'pk': self.id})
