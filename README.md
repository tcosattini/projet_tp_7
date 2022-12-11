# Fromagerie
___

Projet de gestion des cadeau d'une fromagerie

## Installer les dependences

- Prerequis:
```bash
pip3 install -r requirements.txt
```

## Generer la documentation

1. installer les prerequis

### Le dossier docs n'existe pas

2. Creer le conteneur de la documentation :

- Dans le terminal (a la racine du projet django):
```bash
mkdir docs && cd docs && sphinx-quickstart
```

- Les options a renseigner quand demandé :
```bash
Welcome to the Sphinx 5.3.0 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]:

The project name will occur in several places in the built documentation.
> Project name: Fromagerie
> Author name(s): Thibault, Madani, Maxime, Brice, Amin
> Project release []: 0.9.0

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
> Project language [en]: fr
```

### Le dossier docs existe

4. supprimer les fichiers .rst et le contenu du dossier docs/_build (si ils existent)

5. generer la documentation :

- Dans le terminal (a la racine du dossier docs):
```bash
sphinx-apidoc -o . .. && make html
```

## Construire le projet


- Build project with (a racine du projet)

```bash
python3 manage.py tailwind start
```

## Configurer le projet

Change you DB config in settings.py

## References

- Installation de Sphinx dans Django : https://www.freecodecamp.org/news/sphinx-for-django-documentation-2454e924b3bc/

- Tailwind documentation : https://django-tailwind.readthedocs.io/en/latest/installation.html