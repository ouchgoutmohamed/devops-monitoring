# Application Microservices avec Surveillance Prometheus

Ce projet démontre la mise en place d'une architecture microservices conteneurisée avec un système de surveillance des performances complet basé sur Prometheus et Grafana.

## Architecture du Système

L'architecture se compose de trois microservices principaux fonctionnant ensemble pour créer un système e-commerce :

- **Product Service** (port 5001) : Gestion du catalogue de produits
- **Order Service** (port 5002) : Traitement des commandes
- **Inventory Service** (port 5003) : Gestion des stocks

Ces services sont instrumentés pour exposer des métriques via leurs endpoints `/metrics` respectifs, qui sont ensuite collectées et analysées par notre stack de surveillance.

## Stack de Surveillance

### Prometheus
- Collecte de métriques et stockage temporel
- Configuration définie dans `prometheus-multiservice-example/prometheus.yml`
- Scrape toutes les 15 secondes
- Accessible sur le port 9090

### Grafana
- Visualisation des métriques et tableaux de bord
- Pré-configuré pour se connecter à Prometheus
- Accessible sur le port 3000 (identifiants par défaut : admin/admin)

### Node Exporter
- Collecte des métriques système (CPU, mémoire, disque, réseau)
- Accessible sur le port 9100

## Outils de Test de Charge

Le projet inclut deux configurations pour les tests de charge avec K6 :

1. **Tests simples** dans `k6-microservice-tests/`
2. **Tests avancés** avec métriques personnalisées dans `my-k6-load-testing-project/`

## Comment démarrer

### Prérequis
- Docker et Docker Compose
- Git

### Installation et démarrage

1. Clonez le dépôt :
```bash
git clone <url-du-repo>
cd <nom-du-repo>
```

2. Démarrez l'ensemble des services :
```powershell
cd prometheus-multiservice-example
docker-compose up -d
```

3. Vérifiez que les services sont opérationnels :
```powershell
docker-compose ps
```

### Accès aux interfaces

- **Product Service** : http://localhost:5001
- **Order Service** : http://localhost:5002
- **Inventory Service** : http://localhost:5003
- **Prometheus** : http://localhost:9090
- **Grafana** : http://localhost:3000

## Exécution des Tests de Charge

### Tests simples
```powershell
cd k6-microservice-tests
k6 run src/scenarios/product_service_test.js
```

### Tests avancés
```powershell
cd my-k6-load-testing-project
docker-compose up
```

## Métriques Disponibles

### Métriques Application
- `app_requests_total` : Nombre total de requêtes par endpoint
- `http_requests_by_status_code_total` : Requêtes par code de statut HTTP
- `app_request_latency_seconds_bucket` : Latence des requêtes
- `products_viewed_total` : Nombre de consultations par produit
- `product_catalog_size` : Taille du catalogue de produits

### Métriques Infrastructure
- Utilisation CPU
- Consommation mémoire
- I/O disque
- Trafic réseau

## Structure des Tableaux de Bord Grafana

Les tableaux de bord suivants sont recommandés :

1. **Overview** : Vue globale de tous les services
2. **Service-Specific** : Métriques détaillées par service
3. **Infrastructure** : Métriques système et conteneurs
4. **Business Metrics** : Indicateurs métier

## Architecture Technique

Chaque microservice utilise une approche d'instrumentation adaptée à son framework :

- **Product Service** : Flask avec prometheus_flask_exporter
- **Order Service** : Flask/ASGI avec prometheus_flask_exporter
- **Inventory Service** : FastAPI avec prometheus_fastapi_instrumentator

## Développement

### Ajout de nouvelles métriques

Pour ajouter de nouvelles métriques à un service :

1. Définir la métrique dans le module d'instrumentation approprié
2. Instrumenter le code aux points d'intérêt
3. Vérifier que la métrique apparaît dans l'endpoint `/metrics`
4. Ajouter la métrique aux tableaux de bord Grafana

### Test et validation

Utilisez l'endpoint `/metrics` de chaque service pour vérifier que les métriques sont correctement exposées avant de les intégrer dans les tableaux de bord.

## Références
- [Documentation Prometheus](https://prometheus.io/docs/introduction/overview/)
- [Documentation Grafana](https://grafana.com/docs/grafana/latest/)
- [K6 Documentation](https://k6.io/docs/)
