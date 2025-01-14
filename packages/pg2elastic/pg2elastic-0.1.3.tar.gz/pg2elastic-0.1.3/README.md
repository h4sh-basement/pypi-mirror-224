# ⚡ pg2elastic

Enhanced PostgreSQL to Elasticsearch Data Synchronization

### 📚 Description

Welcome to pg2elastic, a fork of the official [pgsync](https://pgsync.com/) package, designed to provide seamless and
efficient data synchronization between PostgreSQL databases and Elasticsearch clusters.
Building upon the solid foundation of pgsync, pg2elastic inherits all of its powerful capabilities and takes them a step
further.

#### Key Features:

* High-Performance Sync: pg2elastic inherits the robust data synchronization engine from pgsync, ensuring lightning-fast
  and reliable transfers.
* Real-time Indexing: Seamlessly mirror your PostgreSQL data into Elasticsearch indices, keeping them in sync in
  real-time.
* Schema Mapping: Easily define and customize the mapping of PostgreSQL schemas to Elasticsearch indexes, giving you
  full control over the data structure.
* Efficient Data Types Handling: pg2elastic effortlessly handles data type conversions, ensuring accurate representation
  across platforms.
* Continuous Enhancements: We are committed to actively maintaining and enhancing pg2elastic, incorporating the latest
  advancements in both PostgreSQL and Elasticsearch technologies.
* Whether you're working on a data-driven application or performing complex data analysis, pg2elastic empowers you with
  a streamlined and feature-rich solution for harmonizing your PostgreSQL and Elasticsearch ecosystems.

---

### 🛠️ Prerequisites

[PGSync Requirements](https://github.com/toluaina/pgsync#requirements)

---

### ✨ Key Enhancements

* [Loguru, Better Logging Module](https://github.com/Delgan/loguru)

#### Environment Variables

`PG_SCHEMA`

* Environment variable to enhance performance by eliminating the need to scan all schemas

`REDIS_USERNAME`

* Environment variable to specify redis username

`REDIS_PASSWORD`

* Environment variable to specify redis password

`REDIS_ENDPOINT`

* Environment variable to specify redis connection endpoint, defaults to `localhost`

`REDIS_SSL`

* Environment variable to specify if redis connection should use ssl, defaults to `true`

`REDIS_CLUSTER`

* Environment variable to specify if redis connection is clustered, defaults to `true`

`REDIS_CHECKPOINT`

* Environment variable to specify if redis will be used to save restore checkpoints, defaults to `true`

`SKIP_BOOTSTRAP`

* Environment variable to specify if boostrap command should be skipped, defaults to `true`.
* Use this env variable if bootstrap command was already run, and you have your bootstrap command stuck in a shell
  script.
* Set to false in cause there are new indexes or schema changes

---

### 🚀 Deployment

#### Manual Deployment

How to run `pg2elastic` and initialize it.

- Create a .env file using the `cp .env.sample .env` command and replace the existing environment variables with
  personal configuration settings.

- Download dependencies using `python setup.py develop`

- Start the app by using `pg2elastic` file command from bin folder, using `python3 pg2elastic --schema yourschema.json`

If you do not run the full setup, you will get errors when running this package.

---

### ✅ Testing

```bash
$ export PG_SCHEMA=
$ flake8 pg2elastic tests
$ python setup.py test
```

---

### 🔊 Logs

This project comes with a [loguru](https://github.com/Delgan/loguru) module for logging, the configurations
for loguru can be found in `pg2elastic` file from bin folder.

---

### 🚚 Deployment

```bash
$ python setup.py sdist bdist_wheel
$ twine upload dist/*
```

---
