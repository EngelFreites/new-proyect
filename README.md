# 📌 Convenciones para Commits

✅ **Estructura Recomendada**

Cada commit debe seguir este formato:

```sh
  tipo(scope): mensaje breve en presente
```

📌 **Ejemplo**

```sh
refactor(backend): mejorar estructura de rutas

```

## 🎯 Tipos de Commits

- **feat** : ✨ Nueva funcionalidad o característica
- **fix** :🐛 Corrección de errores
- **refactor** : 🔨 Reestructuración del código sin cambiar su funcionalidad
- **docs** : 📖 Cambios en la documentación (README, comentarios, etc.)
- **style** : 🎨 Cambios de formato, espacios, comas. (sin afectar el código)
- **test** : ✅ Agregar o modificar pruebas
- **chore** : 🔧 Mantenimiento, configuración o tareas automáticas
- **ci** : 🔄 Cambios en integración continua (GitHub Actions, Docker, etc.)
- **build** : 🏗 Cambios en dependencias, compilación o herramientas de construcción

## ⚡ Ejemplos de Commits Correctos

```sh
feat(ui): agregar componente de botones personalizados
fix(api): corregir error en el endpoint de autenticación
docs(readme): mejorar la guía de instalación
test(backend): agregar pruebas para la capa de servicios
chore(linter): actualizar configuración de ESLint
```

## 🔀 Reglas para Nombres de Ramas

📌 **Este proyecto es un monorepositorio, por lo que las ramas deben seguir estas reglas:**

- **Si trabajas en el frontend, la rama debe llamarse:**

```sh
frontend/nombre-de-la-tarea
```

- **Si trabajas en el backend, la rama debe llamarse:**

```sh
backend/nombre-de-la-tarea
```

## ⚡ Ejemplo de Flujo de Trabajo

1️⃣ **Crear una nueva rama antes de trabajar:**

```sh
git checkout -b frontend/agregar-modal-productos
```

2️⃣ **Hacer commits siguiendo las reglas:**

```sh
git commit -m "feat(ui): agregar modal de productos en frontend"
```

3️⃣ **Subir la rama al repositorio:**

```sh
git push origin frontend/agregar-modal-productos
```

4️⃣ Abrir un Pull Request (PR) en GitHub.
