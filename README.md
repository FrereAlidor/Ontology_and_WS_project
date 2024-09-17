
# Semantic Search Engine using RDF and OWL

## Description
This project implements a semantic search engine based on **RDF** (Resource Description Framework) 
and **OWL** (Web Ontology Language) technologies. The aim is to enable more intelligent queries 
and improve information retrieval by leveraging the semantic relationships between data.

By using RDF and OWL, the search engine can understand the meaning of data and establish meaningful 
connections between them, providing more precise and relevant search results.

## Features
- **Ontological Modeling**: Use of OWL to define concepts, relationships, and classes in the search domain.
- **RDF Querying**: Use of SPARQL to query RDF graphs and retrieve relevant information.
- **Semantic Search**: Generating search results based on semantic relationships rather than exact keyword matches.
- **Extensibility**: Ability to add new ontologies and RDF datasets to enrich search results.

## Technologies
- **RDF**: Data modeling in triples (subject-predicate-object).
- **OWL**: Representation of semantic and ontological relationships.
- **SPARQL**: Query language used to retrieve data from RDF.
- **Apache Jena**: Java framework for managing and querying RDF graphs.


## Prerequisites
Before getting started, ensure you have the following:

-**Python**: Python is an interpreted, multi-paradigm, and cross-platform programming language. 
It supports imperative, functional, and object-oriented programming styles. In this project, 
we used VSCode as the Integrated Development Environment (IDE) to write and execute Python code.

-**Jena**: Jena is an open-source Java API developed by Hewlett-Packard Labs for reading and
manipulating ontologies described in RDFS or OWL. It is used in this project for managing 
and querying RDF graphs.

## Installation

1. Clone the Git repository:
   ```bash
   git clone https://github.com/FrereAlidor/Ontology_and_WS_project.git
   cd Ontology_and_WS_project
   ```

2. Install dependencies with Maven:
   ```bash
   mvn install
   ```

3. Set up and launch the Fuseki server to query your RDF datasets.

4. Import your OWL ontology and RDF datasets into Fuseki or use Apache Jena tools to load the data locally.

## Usage

### 1. Load RDF Datasets
- You can load RDF datasets directly into the Fuseki server or use Jena locally. Use the provided OWL
  file or add your own ontologies to enrich the semantic relationships.

### 2. Execute SPARQL Queries
- You can query the RDF data using SPARQL queries either through the Fuseki interface or within
   the application using the Jena API. Here is an example of a SPARQL query:
   ```sparql
   SELECT ?subject ?predicate ?object 
   WHERE { 
       ?subject ?predicate ?object .
   }
   LIMIT 100
   ```

### 3. User Interface
- If the project includes a user interface, you can access it via `http://localhost:3030/`
   (or the configured URL) after starting the Fuseki server. Query results will be displayed
  in a readable format, highlighting semantic relationships.

## Contribution
Contributions are welcome! If you'd like to add new features, improve performance, 
or fix bugs, feel free to submit a pull request.

## Authors
- **Mbayandjambe Alidor** - mbayandjambealidor@gmail.com

## License
This project is licensed under the [MIT License](LICENSE).








