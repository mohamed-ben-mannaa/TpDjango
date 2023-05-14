# Generated by Django 4.1.7 on 2023-05-03 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0003_categorie_fournisseur_produitnc_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produit',
            old_name='categorie',
            new_name='catégorie',
        ),
        migrations.RenameField(
            model_name='produit',
            old_name='Fournisseur',
            new_name='fournisseur',
        ),
        migrations.RenameField(
            model_name='produit',
            old_name='libelle',
            new_name='libellé',
        ),
        migrations.AddField(
            model_name='commande',
            name='adresse_livraison',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='commande',
            name='nom_client',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='produit',
            name='qte',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(choices=[('Al', 'Alimentaire'), ('Mb', 'Meuble'), ('Sn', 'Sanitaire'), ('Vs', 'Vaisselle'), ('Vt', 'Vêtement'), ('Jx', 'Jouets'), ('Lg', 'Linge de Maison'), ('Bj', 'Bijoux'), ('Dc', 'Décor')], default='Al', max_length=50),
        ),
        migrations.AlterField(
            model_name='commande',
            name='produits',
            field=models.ManyToManyField(related_name='produits', to='magasin.produit'),
        ),
        migrations.AlterField(
            model_name='fournisseur',
            name='adresse',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='fournisseur',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='fournisseur',
            name='nom',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fournisseur',
            name='telephone',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='description',
            field=models.TextField(default='non définie'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='prix',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='produitnc',
            name='Duree_garantie',
            field=models.CharField(max_length=100),
        ),
    ]
