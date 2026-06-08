---
title: "Memories Viewer — Mapa del Proyecto"
type: reference
updated: 2026-06-07
---

# Memories Viewer — Mapa del Proyecto

**Ruta local:** `C:\Users\avada\Personal_Projects\memories-viewer`  
**Framework:** Quasar v2 (SPA) + Vue 3 + Vite  
**Propósito:** Visualizador interactivo del vault narrativo *Destiny: Renewed Fate*

---

## Stack

| Capa | Tecnología |
|------|------------|
| Framework UI | Quasar v2.16 (SPA mode) |
| JS | Vue 3.5 — Composition API, `<script setup>` |
| Router | Vue Router v5 con navigation guard |
| Estado | Pinia v3 — store `auth` funcional |
| Auth | Google Identity Services (OAuth2 implicit grant) |
| Data | Google Drive API v3 (service listo, sin usar aún) |
| Iconos | Lucide Vue (`@lucide/vue`) |
| Estilos | SCSS global + `<style scoped>` por componente |
| Build | Quasar CLI / Vite |
| Gestor | pnpm |

```
pnpm dev    → servidor de desarrollo
pnpm build  → build de producción
```

**Variables de entorno necesarias:**
```
VITE_GOOGLE_CLIENT_ID    → OAuth2 client ID de Google Cloud Console
VITE_DRIVE_FOLDER_ID     → ID de la carpeta raíz del vault en Google Drive
```

---

## Estructura de archivos

```
src/
├── App.vue                      ← raíz: solo <router-view>
├── boot/
│   └── google.js                ← registra vue3-google-login en la app
├── css/
│   ├── app.scss                 ← estilos globales (bg, body, scrollbar, overrides)
│   └── quasar.variables.scss    ← variables de Quasar
├── layouts/
│   └── MainLayout.vue           ← header con brand bar + subnav de 5 secciones
├── pages/
│   ├── LoginPage.vue            ← pantalla de login con Google OAuth2
│   ├── IndexPage.vue            ← Timeline (AgeCards hardcodeadas)
│   ├── CharactersPage.vue       ← shell: "EN CONSTRUCCIÓN"
│   ├── DialoguesPage.vue        ← shell: "EN CONSTRUCCIÓN"
│   ├── ArchivesPage.vue         ← shell: "EN CONSTRUCCIÓN"
│   ├── ChaptersPage.vue         ← shell: "EN CONSTRUCCIÓN"
│   └── ErrorNotFound.vue        ← 404
├── components/
│   ├── AgeCard.vue              ← tarjeta de Age (dot + título + desc + tag de estado)
│   ├── NavItem.vue              ← ítem de nav con ícono (definido, sin uso aún)
│   └── EssentialLink.vue        ← boilerplate de Quasar (sin uso)
├── router/
│   ├── index.js                 ← Vue Router + navigation guard (redirect → /login)
│   └── routes.js                ← todas las rutas definidas
├── services/
│   └── drive.js                 ← Google Drive API v3: listFiles() y readFile()
└── stores/
    ├── auth.js                  ← Pinia store de autenticación (token + isAuthenticated)
    └── index.js                 ← setup de Pinia

public/
└── bg.jpg                       ← fondo de pantalla
```

---

## Flujo de autenticación

```
Usuario abre la app
    ↓
router.beforeEach — ¿hay token en auth store?
    ├── NO  → redirect /login
    └── SÍ (y no expirado) → deja pasar

/login — LoginPage.vue
    ↓
click "ACCEDER CON GOOGLE"
    ↓
google.accounts.oauth2.initTokenClient({ scope: drive.readonly })
    ↓
.requestAccessToken() → popup Google
    ↓
callback({ access_token, expires_in })
    ↓
auth.setToken(token, expiresIn)
    → guarda en localStorage: 'gtoken' + 'gtoken_exp'
    ↓
router.push('/')
```

**Auth store (`stores/auth.js`):**
- `token` — ref, hidratado desde `localStorage.getItem('gtoken')`
- `expiresAt` — ref, hidratado desde `localStorage.getItem('gtoken_exp')`
- `isAuthenticated` — computed: `!!token && Date.now() < expiresAt`
- `setToken(t, expiresIn)` — guarda token y calcula expiración
- `logout()` — limpia refs y localStorage

**Guard en `router/index.js`:**
```js
Router.beforeEach((to) => {
  const auth = useAuthStore()
  if (to.path !== '/login' && !auth.token) return '/login'
})
```
Nota: checa `auth.token` (existencia), no `auth.isAuthenticated` (existencia + expiración). Si el token venció pero sigue en localStorage, el guard deja pasar — las llamadas a Drive fallarán con 401.

---

## Servicio Drive (`services/drive.js`)

Dos funciones, ambas reciben el token del auth store:

```js
listFiles(token, folderId?)
// GET /drive/v3/files?q='FOLDER_ID'+in+parents&fields=files(id,name,mimeType)&orderBy=name
// Retorna: { files: [{ id, name, mimeType }] }

readFile(token, fileId)
// GET /drive/v3/files/FILE_ID?alt=media
// Retorna: string (contenido del archivo Markdown)
```

El `folderId` por defecto es `VITE_DRIVE_FOLDER_ID`. Para navegar subcarpetas hay que llamar `listFiles` con el ID de la subcarpeta correspondiente.

---

## Navegación y rutas

| Ruta | Página | Layout | Estado |
|------|--------|--------|--------|
| `/login` | `LoginPage.vue` | — (standalone) | ✅ Funcional |
| `/` | `IndexPage.vue` | `MainLayout` | ✅ Funcional (datos hardcodeados) |
| `/characters` | `CharactersPage.vue` | `MainLayout` | 🔲 Shell vacío |
| `/dialogues` | `DialoguesPage.vue` | `MainLayout` | 🔲 Shell vacío |
| `/archives` | `ArchivesPage.vue` | `MainLayout` | 🔲 Shell vacío |
| `/chapters` | `ChaptersPage.vue` | `MainLayout` | 🔲 Shell vacío |
| `/:catchAll` | `ErrorNotFound.vue` | — | ✅ Existe |

---

## Componentes

### `MainLayout.vue`
Header en dos capas:
1. **Brand bar** — "Memories of a Ghost" (Cinzel) + "VAULT // RENEWED FATE" + meta derecho con Age/Cap (hardcodeado: "AGE XVIII // HERESY" + "CAP. 55 EN PROGRESO")
2. **Subnav** — 5 ítems con ícono Lucide + label; estado activo por `ref currentSection`; al click llama `router.push(item.route)` y actualiza el ref

### `LoginPage.vue`
- Standalone (sin layout): fondo `bg.jpg` + overlay + card centrada
- Botón "ACCEDER CON GOOGLE" llama a `useAuthStore()` y usa la GSI API directamente
- No usa el componente `<GoogleLogin>` del plugin (usa `google.accounts.oauth2` global)

### `IndexPage.vue` (Timeline)
- Topbar: buscador placeholder + "294 ARCHIVOS" (estático)
- Lista de `<AgeCard>` sobre array `ages` hardcodeado (4 Ages)
- **Próximo paso:** reemplazar array por datos reales desde Drive

### `AgeCard.vue`
Props: `{ age: Object }` → `{ title, desc, status, color }`

| `color` | Hex | Uso típico |
|---------|-----|------------|
| `gold` | `#c9a84c` | COMPLETO |
| `blue` | `#4a7ab5` | (libre) |
| `red` | `#8b3a3a` | EN PROGRESO |

Elementos: dot de color + título mono + descripción dim + tag con borde de color + corners decorativos CSS.

### `NavItem.vue`
Props: `{ item, active }`. Definido pero no usado (el subnav está inline en MainLayout). Candidato a reemplazar el nav inline o para un drawer lateral futuro.

---

## Sistema de diseño

### Paleta

| Token | Hex | Uso |
|-------|-----|-----|
| Gold | `#c9a84c` | Activo, highlight, acento principal |
| Base | `#080a0e` | Fondo de cards y header |
| Border | `#1e2230` | Bordes y separadores |
| Text | `#c0c8d8` | Texto principal |
| Text dim | `#4a5068` | Texto secundario |
| Text ghost | `#3a4058` | Meta, contadores |
| Blue | `#4a7ab5` | Estado secundario |
| Red | `#8b3a3a` | En progreso / alerta |

### Tipografía

| Fuente | Uso |
|--------|-----|
| `Cinzel` (serif) | Brand, section titles |
| `Share Tech Mono` (mono) | Todo lo demás: HUD, etiquetas, nav, cards |

### Patrones visuales
- **Glass morphism:** `rgba(8,10,14,0.72–0.92)` + `backdrop-filter: blur(6–10px)`
- **Bordes:** `0.5px solid #1e2230`
- **Corners decorativos:** CSS border parcial `tl/br` en cards
- **Prefijo CSS:** `mv-*` en todas las clases del proyecto

---

## Estado actual

### Implementado ✅
- Login con Google OAuth2 (implicit grant, scope `drive.readonly`)
- Auth store Pinia con persistencia en localStorage
- Navigation guard que protege todas las rutas
- Servicio Drive con `listFiles` y `readFile` listos
- Layout completo con subnav funcional
- Todas las rutas definidas
- Shells de las 5 secciones (4 con "EN CONSTRUCCIÓN")
- Design system completo

### Pendiente ❌
- Conectar Drive service a las páginas (reemplazar datos hardcodeados)
- Implementar IndexPage con Ages reales desde Drive (`01_Timeline/`)
- Implementar CharactersPage, DialoguesPage, ArchivesPage, ChaptersPage
- Parsear Markdown de los archivos del vault (frontmatter + contenido)
- Buscador funcional
- Manejo de token expirado en el guard (actualmente checa `auth.token`, no `auth.isAuthenticated`)
- Decidir destino de `NavItem.vue`

---

## Correspondencia vault ↔ app

| Sección | Carpeta del vault | Archivos |
|---------|-------------------|----------|
| Timeline | `01_Timeline/` | 19 Age files |
| Personajes | `02_Characters/` | ~50 archivos |
| Diálogos | `05_Dialogues/` | 105 archivos |
| Archivos | `06_Timeline_Archives/` | ~20 archivos |
| Capítulos | `10_Chapters/` | 56 stubs (Caps 1–55) |
