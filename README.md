
# Moteur de recherche sémantique utilisant RDF et OWL

## Description
Ce projet implémente un moteur de recherche sémantique basé sur les technologies **RDF** 
(Resource Description Framework) et **OWL** (Web Ontology Language). 
L'objectif est de permettre des requêtes plus intelligentes et d'améliorer la recherche 
d'informations en exploitant les relations sémantiques entre les données.

Grâce à RDF et OWL, le moteur de recherche peut interpréter le sens des données et établir 
des liens significatifs entre elles, offrant ainsi des résultats plus précis et pertinents.

## Fonctionnalités
- **Modélisation ontologique** : Utilisation d'OWL pour définir des concepts, relations et classes dans le domaine de recherche.
- **Interrogation RDF** : Utilisation de SPARQL pour interroger des graphes RDF et extraire des informations pertinentes.
- **Recherche sémantique** : Génération de résultats basés sur des relations sémantiques plutôt que sur des correspondances exactes de mots-clés.
- **Extensibilité** : Possibilité d'ajouter de nouvelles ontologies et de nouveaux jeux de données RDF pour enrichir les résultats de recherche.

## Technologies
- **RDF** : Modélisation des données en triplets (sujet-prédicat-objet).
- **OWL** : Représentation des relations sémantiques et ontologiques.
- **SPARQL** : Langage de requête utilisé pour interroger les données RDF.
- **Apache Jena** : Framework Java pour la gestion et l'interrogation des graphes RDF.
- **Fuseki** : Serveur SPARQL pour exécuter des requêtes sur des jeux de données RDF.

## Prérequis
Avant de commencer, assurez-vous d'avoir les éléments suivants installés :
- **Java JDK** (version 8 ou plus récente)
- **Apache Maven** (pour la gestion des dépendances)
- **Apache Jena** et **Fuseki**
- **Git** (pour cloner le projet)

## Installation

1. Clonez le dépôt Git :
   ```bash
   git clone https://github.com/FrereAlidor/Ontology_and_WS_project.git
   cd Ontology_and_WS_project
   ```

2. Installez les dépendances avec Maven :
   ```bash
   mvn install
   ```

3. Configurez et lancez le serveur Fuseki pour interroger vos jeux de données RDF.

4. Importez votre ontologie OWL et vos jeux de données RDF dans Fuseki ou utilisez les outils d'Apache Jena pour charger les données localement.

## Utilisation

### 1. Charger les jeux de données RDF
- Vous pouvez charger des jeux de données RDF directement sur le serveur Fuseki ou en utilisant Jena en local.
-  Utilisez le fichier OWL fourni ou ajoutez vos propres ontologies pour enrichir les relations sémantiques.

### 2. Exécuter des requêtes SPARQL
- Vous pouvez interroger les données RDF à l'aide de requêtes SPARQL dans l'interface Fuseki ou
-  dans l'application en utilisant l'API Jena. Voici un exemple de requête SPARQL :
   ```sparql
   SELECT ?subject ?predicate ?object 
   WHERE { 
       ?subject ?predicate ?object .
   }
   LIMIT 100
   ```

### 3. Interface utilisateur
- Si le projet inclut une interface utilisateur, accédez-y via `http://localhost:3030/`
- (ou l'URL configurée) après avoir démarré le serveur Fuseki. Les résultats des requêtes
- seront affichés dans un format lisible et pertinent, avec une mise en avant des relations sémantiques.

## Structure du projet
- `/src` : Contient le code source Java pour l'intégration avec Jena et les requêtes SPARQL.
- `/data` : Contient des exemples de jeux de données RDF et des fichiers OWL.
- `/queries` : Contient des exemples de requêtes SPARQL pour interroger les données.

## Contribution
Les contributions sont les bienvenues ! Si vous souhaitez ajouter de nouvelles fonctionnalités,
améliorer les performances ou corriger des bugs, n'hésitez pas à soumettre une pull request.

## Auteurs
- **Mbayandjambe Alidor** - mbayandjambealidor@gmail.com

## Licence
Ce projet est sous licence [MIT](LICENSE).

