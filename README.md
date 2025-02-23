# 📌 Convenciones para Commits

✅ **Estructura Recomendada**

Cada commit debe seguir este formato:

```sh
  tipo(scope): mensaje breve en presente
```

📌 **Ejemplo**

```sh
refactor(backend): improve route structure

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
feat(ui): add custom buttons component
fix(api): Fix error in authentication endpoint
docs(readme): Improve the installation guide
test(backend): Add tests for the service layer
chore(linter): Update ESLint configuration
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
git checkout -b frontend/add-modal-products
```

2️⃣ **Hacer commits siguiendo las reglas:**

```sh
git commit -m "feat(ui): add-modal-products"
```

3️⃣ **Subir la rama al repositorio:**

```sh
git push origin frontend/add-modal-products
```

4️⃣ Abrir un Pull Request (PR) en GitHub.
