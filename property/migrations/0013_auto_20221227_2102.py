# Generated by Django 4.1.4 on 2022-12-27 18:02

from django.db import migrations


def connect_flats_to_owner(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    owner_set = Owner.objects.all()
    for owner in owner_set.iterator():
        owner_flats = Flat.objects.filter(owner=owner.name, owner_pure_phone=owner.owner_pure_phone)
        owner.owned_flats.set(owner_flats)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_alter_flat_owner_alter_flat_owner_pure_phone_and_more'),
    ]

    operations = [
        migrations.RunPython(connect_flats_to_owner)
    ]
