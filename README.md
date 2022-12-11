# Fromagerie
___

Projet de gestion des cadeau d'une fromagerie

## Installer les dependences

Prerequis:
```bash
pip3 install -r requirements.txt
```
Tailwind documentation :

https://django-tailwind.readthedocs.io/en/latest/installation.html

Build project with

```bash
python3 manage.py tailwind start
```

## Generer la documentation

1. installer les dependances

2. Se deplacer a la racine du projet Django (projet_fil_rouge_api)

Dans le terminal:
```bash
mkdir docs && cd docs
```

3. generer la documentation

Dans le terminal:
```bash
make html
```

## Configurer le projet

Change you DB config in settings.py