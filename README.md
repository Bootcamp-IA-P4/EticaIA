# 🧠 EticaIA – Transparencia ética en la inteligencia artificial

**EticaIA** es una plataforma de código abierto que permite visualizar, analizar y recopilar información sobre casos éticos relacionados con el desarrollo y uso de la inteligencia artificial. A través de un sistema de scraping automatizado, base de datos en la nube, API backend y una interfaz React moderna, se ofrece un **mapa interactivo** que facilita el acceso público y transparente a esta información.

---

## 🌍 Objetivo del proyecto

Este proyecto nace del interés por fomentar el debate y la transparencia sobre los desafíos éticos que plantea la inteligencia artificial, recogiendo artículos reales sobre casos actuales, automatizando su recopilación y visualización, y permitiendo construir una base de conocimiento accesible para cualquier persona interesada.

---

## 🧩 Tecnologías utilizadas

### 🔙 Backend

- **Python 3.12**
- **FastAPI** – Framework para crear la API REST.
- **Motor + MongoDB** – Para gestionar la base de datos NoSQL.
- **Unittest / Pytest** – Para la ejecución de pruebas automáticas.
- **dotenv** – Para gestionar variables de entorno.

### 🔮 Web Scraping

- **Requests** – Para hacer peticiones HTTP.
- **BeautifulSoup** – Para extraer contenido de páginas web.
- **Scraper personalizado** – Recolecta datos de MIT Technology Review (ajustable).

### 🧪 Testing

- **Unittest (versión final)** – Adaptado para evitar errores de cierre del bucle de eventos.
- **Tests por separado** – Ejecutados con un script que los lanza uno a uno para evitar colisiones asincrónicas.

### 🗃️ Base de datos

- **MongoDB local y test** (`eticaia_db`, `eticaia_db_test`) – Repositorios separados para entorno de producción y pruebas.

### 🎨 Frontend

- **React + Vite** – Aplicación SPA para visualizar los artículos en un mapa.
- **Leaflet.js (previsto)** – Biblioteca de mapas interactivos.

---

## ⚙️ Pasos para iniciar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/Bootcamp-IA-P4/EticaIA
cd eticaia/server
```

### 2. Crear entorno virtual

```bash
python -m venv .venv
source .venv/Scripts/activate  # en Windows
# o
source .venv/bin/activate  # en Linux/macOS
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crea un archivo `.env` en la carpeta `server` con este contenido:

```env
MONGO_URI=mongodb://localhost:*****
DB_NAME=nombre_de_tu_base_de_datos
MONGO_DB_NAME_TEST=nombre_de_tu_base_de_datos_test
```

### 5.⚡ Arranque simultáneo del frontend y backend

El proyecto está configurado para levantar **tanto el frontend como el backend** con un solo comando:

```bash
cd client
npm run dev
```

Esto lanzará automáticamente:

El frontend (React + Vite) en http://localhost:5173

El backend (FastAPI) accesible desde http://localhost:8000

### 🧩 Arranque por separado

Si prefieres iniciar los servidores manualmente y por separado, puedes hacerlo así:

---

### 🟠 Levantar solo el backend (FastAPI)

Desde la carpeta `server`:

```bash
cd server
uvicorn api.main:app --reload
```

Esto levantará el backend en: http://localhost:8000

### 🔵 Levantar solo el frontend (React + Vite)

Desde la carpeta client:

```bash

cd client
npm run dev

```

Esto levantará el frontend en: http://localhost:5173

La opción automática es útil durante el desarrollo, mientras que levantar los servicios por separado puede ser útil para debugging o despliegue independiente.

### 6. Acceder a la documentación interactiva

FastAPI genera automáticamente dos interfaces de documentación para la API:

- **Swagger UI** (interactiva):  
  [http://localhost:8000/docs](http://localhost:8000/docs)

- **ReDoc** (documentación estructurada):  
  [http://localhost:8000/redoc](http://localhost:8000/redoc)

Puedes utilizar cualquiera de las dos para explorar los endpoints, ver los modelos y probar las peticiones directamente desde el navegador.

---

## 📈 Briefing del proyecto

- **Nombre:** EticaIA
- **Tipo:** Proyecto didáctico full stack
- **Objetivo:** Automatizar la recogida y visualización de casos éticos sobre IA.
- **Entorno:** Local (futuro despliegue en la nube)
- **Repositorio Git:** GitHub con organización de ramas y tablero de planificación
- **Metodología:** Git Flow + planificación en GitHub Projects

---

## 🔄 Funcionalidad del scraper

El scraper accede a una fuente web (actualmente MIT Technology Review) y extrae:

- Título del artículo
- Extracto (si existe)
- Fecha o antigüedad relativa
- Enlace original

Cada ejecución puede:

- Añadir artículos nuevos
- Actualizar artículos existentes
- Guardarlos automáticamente en MongoDB

---

## 🧪 Funcionamiento de los tests

Para evitar conflictos con el event loop de `asyncio`, los tests se ejecutan por separado mediante:

```bash
python tests/run_tests_separately.py
```

Este script lanza los siguientes archivos:

- `test_api.py`: Comprueba que los endpoints devuelven correctamente los artículos.
- `test_db_save.py`: Fuerza la inserción de un artículo y verifica que se guarda en MongoDB.
- `test_scraper.py`: Verifica que el scraper devuelve artículos y con la estructura esperada.

---

## 🌿 Git Flow y ramas

- `main` – Rama estable para producción
- `dev` – Desarrollo general
- `test-backend` – Ramas específicas para testing de backend
- `feature/*` – Para cada nueva funcionalidad (`feature/scraper`, `feature/db-test`, etc.)

---

## 📋 Planificación en GitHub Projects

Se utilizó un tablero tipo **Kanban** llamado **EticaIA-management** en GitHub Projects para:

- Planificar tareas
- Hacer seguimiento de features
- Documentar bloqueos o mejoras futuras
- Dividir el proyecto por áreas: Scraper, API, Tests, Base de datos, Frontend, DevOps

---

## 🚀 ¿Qué puedes aportar?

Si te interesa colaborar en el proyecto, puedes:

- Proponer nuevas fuentes de scraping
- Sugerir mejoras visuales o de accesibilidad
- Ayudar con la documentación o pruebas
- Participar en la internacionalización del contenido

---

## 📬 Contacto

¿Tienes alguna idea o comentario?  
Abre un issue o contáctanos directamente vía GitHub.
