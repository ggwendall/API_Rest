![banner2](https://github.com/ggwendall/API_Rest/assets/48108275/e7db8110-4756-4353-bdd8-6098f013e0eb)

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

# Projet Open Data Environnement - README

## Table des matières

- [Introduction](#introduction)
- [Objectif](#objectif)
- [Prérequis](#prérequis)
- [Arboresence](#Arboresence)
- [Utilisation](#utilisation)
- [Portail Open Data](#portail-open-data)
- [Screenshot de l'app](#Screenshot-de-l'app)
- [Contributions](#contributions)

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

## Introduction

Bienvenue dans le projet Open Data Environnement ! Ce projet a été initié par une ONG qui s'engage à centraliser et à rendre accessibles toutes les données open data relatives à l'environnement. Notre objectif principal est de mettre ces données à la disposition du public, tout en explorant des possibilités de retraitement et de corrélation pour proposer des solutions visant à améliorer l'environnement.

Ce document vise à vous guider à travers le développement et le déploiement d'une API REST basée sur un jeu de données initial, ainsi qu'à explorer une ébauche de portail opendata. Cette phase initiale nous aidera à déterminer si cette approche est viable avant d'investir davantage dans le recrutement de développeurs et l'infrastructure.

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

## Objectif

L'objectif principal de ce projet est de développer et de tester une API REST qui rendra les données environnementales accessibles au plus grand nombre. Voici les points clés de notre mission :

1. **Développer l'API REST** : Créer une API REST robuste qui permettra aux utilisateurs d'accéder facilement aux données environnementales stockées dans notre base de données.

2. **Proposer une ébauche de portail opendata** : Mettre en place une interface web conviviale qui permettra aux utilisateurs de parcourir et de rechercher les jeux de données disponibles, de visualiser les informations pertinentes et de télécharger les données en fonction de leurs besoins.

3. **Tester la solution** : Effectuer des tests exhaustifs pour s'assurer que l'API et le portail fonctionnent de manière optimale et répondent aux besoins des utilisateurs.

4. **Évaluer la viabilité** : À l'issue de cette phase initiale, évaluer si cette solution répond à nos objectifs avant de prendre des décisions concernant le recrutement de développeurs supplémentaires et l'expansion de l'infrastructure.

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

## Prérequis

Avant de commencer à travailler sur ce projet, assurez-vous d'avoir les éléments suivants en place :

- **Environnement de développement** : Un environnement de développement Python 3.x configuré sur votre machine.

- **Bibliothèques Python** : Les bibliothèques Python nécessaires installées, que vous pouvez retrouver dans le fichier `requirements.txt`.

- **Base de données** : Une base de données pour stocker les données environnementales. Assurez-vous d'avoir la configuration de la base de données prête (par exemple, PostgreSQL, MySQL, SQLite).

- **Accès aux données** : Les jeux de données open data sur l'environnement que vous souhaitez rendre accessibles. Ces données devraient être stockées dans la base de données.

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

## Arboresence

Pour organiser le projet sur votre machine, suivez cette arboresence :

```bash
api-REST_Mongodb-CRUD
│ 
├─── client 
│   ├─── .streamlit
│   │   └─── config.toml
│   ├─── pages
│   │   ├─── 01_Create_Post.py
│   │   ├─── 02_Read_Get.py
│   │   ├─── 03_Update_Put.py
│   │   ├─── 04_Delete.py
│   │   └─── 05_Infos.py
│   ├─── client.py
│   └─── requirements_client.txt
│ 
├─── mongo
│   ├─── CO2_emission_by_countries.json
│   └─── Dockerfile
│
├─── server
│   ├─── connection_mongo.py
│   ├─── my_api.py
│   └─── requirements_api.txt
│
├─── .env 
├─── Dockerfile-serveur
├─── docker-compose.yml
└─── readme.md
```
![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

## Utilisation

Une fois le projet configuré et le serveur en cours d'exécution, vous pouvez commencer à utiliser l'API REST et à explorer le portail opendata.

   ```bash
   streamlit run client/client.py
   ```

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

## Portail Open Data

CO2 Emitted by countries into environment (Year wise from 1750 to 2022)
```bash
https://www.kaggle.com/datasets/moazzimalibhatti/co2-emission-by-countries-year-wise-17502022
```
![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

## Deployment:
* Navigate to the directory where you want to download the repo then run the following commands:
```bash
git clone https://github.com/Hatchi-Kin/api-REST_Mongodb-CRUD.git
```
```bash
cd api-REST_Mongodb-CRUD
```
```bash
docker compose up -d
```

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

## Client
You can use the streamlit client to test the API
* In /api-REST_Mongodb-CRUD
```bash
pip install -r client/requirements_client.txt
```
```bash
streamlit run client/client.py
```   

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

## Screenshot de l'app
<img width="1246" alt="Capture d'écran 2023-10-05 102736" src="https://github.com/ggwendall/API_Rest/assets/48108275/cd096ccc-b845-424b-85ed-3bfd8cc7a7d5">

<img width="1249" alt="Capture d'écran 2023-10-05 102753" src="https://github.com/ggwendall/API_Rest/assets/48108275/2eb84fef-a593-4434-b434-26f5ac62b998">

<img width="1247" alt="Capture d'écran 2023-10-05 102806" src="https://github.com/ggwendall/API_Rest/assets/48108275/e777d3c6-5382-4e72-9291-c0f15bf29ead">

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

## Contributions

Merci au contributeurs de ce projet ! 

<div align=center>

<img src="https://media.giphy.com/media/VgCDAzcKvsR6OM0uWg/giphy.gif" width="50"> 

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

![Bottom](https://github.com/ggwendall/ggwendall/assets/48108275/1f58de6a-f411-45fd-86a6-e9aa673332e6)
