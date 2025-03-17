# 📌 Proyecto: EticaIA

## **🔍 Descripción del Proyecto**
**EticaIA** es una plataforma interactiva que recopila y visualiza **casos éticos relacionados con la Inteligencia Artificial (IA)** a nivel global. A través de **web scraping**, extraemos información de fuentes confiables sobre problemáticas como **sesgos algorítmicos, privacidad, automatización del empleo, deepfakes y vigilancia masiva**, y las representamos en un **mapa interactivo** con filtros avanzados.

Este proyecto tiene un enfoque **educativo y divulgativo**, ayudando a investigadores, periodistas, legisladores y ciudadanos a comprender el impacto real de la IA en nuestra sociedad.

---

## **🎯 Objetivos del Proyecto**
✅ **Scraping de Noticias Éticas sobre IA**
- Extraer información de fuentes tecnológicas y medios de verificación como **MIT Tech Review, Wired, The Verge, Snopes y Maldita.es**.
- Recopilar datos sobre **casos éticos de IA**, incluyendo **título, fecha, ubicación, categoría, descripción y fuente**.
- Automatizar la extracción de datos mediante **GitHub Actions**.

✅ **Base de Datos y API REST**
- Almacenar la información en **MongoDB**, estructurada por categorías y geolocalización.
- Desarrollar una **API en Flask o FastAPI** para exponer los datos al frontend.
- Implementar **endpoints REST** como `/cases`, `/cases?category=sesgo`, `/cases/{id}`.

✅ **Frontend Interactivo en React**
- Desarrollar una interfaz visual con **React Vite**.
- Implementar un **mapa interactivo** con **Google Maps API o OpenStreetMap**.
- Integrar filtros por **categoría, fecha y ubicación**.
- Incorporar gráficos con **Chart.js o D3.js** para visualizar tendencias.

✅ **Automatización y Despliegue**
- **GitHub Projects (`EticaIA-management`)** para la gestión ágil del desarrollo.
- **GitHub Actions** para ejecutar el scraper periódicamente y desplegar la API y el frontend automáticamente.
- **Docker** para contenerización del backend y la API.
- **Railway/Render** para el despliegue de la API y la interfaz.

---

## **📅 Planificación del Desarrollo**
| Fecha | Tareas |
|--------|----------------------------------------------------------------|
| **Lunes 17** | Configuración inicial: repo, GitHub Projects, tecnologías |
| **Martes 18** | Desarrollo del scraper y conexión con MongoDB |
| **Miércoles 19** | Refinamiento del scraping y automatización con GitHub Actions |
| **Jueves 20** | Creación de la API con Flask/FastAPI |
| **Viernes 21** | Desarrollo del frontend con React y mapa interactivo |
| **Lunes 24** | Revisión final, documentación y despliegue |
| **Martes 25** | Presentación del proyecto |

---

## **🛠 Tecnologías Utilizadas**
### **Backend y Scraping**
- Python
- BeautifulSoup / Selenium
- Flask / FastAPI
- MongoDB

### **Frontend**
- React Vite
- Google Maps API / OpenStreetMap
- Chart.js / D3.js

### **Infraestructura y DevOps**
- GitHub Projects (gestión del proyecto)
- GitHub Actions (automatización)
- Docker (contenedorización)
- Railway / Render (despliegue)

---

## **📌 Instalación y Configuración**
### **1️⃣ Clonar el Repositorio**
```bash
 git clone https://github.com/organizacion/EticaIA.git
 cd EticaIA
```

### **2️⃣ Configurar Entorno Virtual y Dependencias**
```bash
# Crear y activar entorno virtual
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt
```

### **3️⃣ Ejecutar el Scraper**
```bash
python scraper.py
```

### **4️⃣ Iniciar el Backend**
```bash
uvicorn app.main:app --reload
```

### **5️⃣ Iniciar el Frontend**
```bash
cd frontend
npm install
npm run dev
```

---

## **📌 Contribución**
🚀 Este es un proyecto **didáctico**, y estamos abiertos a contribuciones. Si deseas participar, puedes:
1. **Abrir un Issue** con sugerencias o mejoras.
2. **Hacer un Fork** del repositorio y enviar un Pull Request.
3. **Comentar en GitHub Projects (`EticaIA-management`)** para discutir ideas.

---

## **📜 Licencia**
📖 Este proyecto está bajo la licencia **MIT**.

---

📢 **¡Gracias por tu interés en EticaIA!** Si tienes dudas, revisa la documentación y colabora con nosotros. 🚀

