# 🛸 Oryx y Luna — Carpeta de producción

```
canal/
├── README.md                         ← este archivo
├── biblia-del-canal.md               ← resumen general del canal
├── comun/                            ← lo que se usa en TODOS los episodios
│   ├── kling-guia.md                 ← ⭐ cómo producir en Kling, paso a paso
│   ├── personajes-y-estilo.md        ← cómo se ven y suenan Oryx y Luna + bloques de prompt
│   ├── cancion-entrada-salida.md     ← intro y outro + prompt de música
│   └── configuracion-youtube.md      ← cómo subir cada video (Hecho para niños, etc.)
├── episodio-01-pio-pio-pajarito/
├── episodio-02-agua-fresca/
└── episodio-03-crece-florecita/
```

Cada carpeta de episodio tiene:

| Archivo | Qué contiene |
|---|---|
| `01-guion.md` | Guion completo por escenas, con tiempos, diálogos y lo que se ve en pantalla |
| `02-cancion.md` | Letra, estilo musical, movimientos y prompt para generar la música |
| `03-titulo-y-miniatura.md` | Título, alternativas, diseño de miniatura y prompt para generarla |
| `04-descripcion-y-etiquetas.md` | Descripción lista para pegar en YouTube, etiquetas y hashtags |
| `05-prompts-video.md` | Un prompt por escena para generar el video con IA |
| `06-checklist-produccion.md` | Lista paso a paso, de la grabación de voces a la publicación |
| `07-kling-tomas.md` | ⭐ **Las tomas para Kling**: 5 o 10 s cada una, con Elements, diálogo para Lip Sync y prompt listo para pegar |

## Si usas Kling (recomendado)

Empieza por `comun/kling-guia.md` y luego usa el `07-kling-tomas.md` de cada episodio.
Esos prompts ya están completos: no hay que reemplazar etiquetas.

## Cómo usar los prompts generales (`05-prompts-video.md`, para otras herramientas)

1. Abre `comun/personajes-y-estilo.md` y copia los bloques **[ESTILO]**, **[ORYX]** y **[LUNA]**.
2. En cada prompt de escena, reemplaza esas etiquetas por el bloque completo.
   Usar siempre el mismo texto es lo que mantiene a los personajes iguales en todas las escenas.
3. Los prompts están en inglés porque la mayoría de las herramientas de video e imagen con IA
   entienden mejor el inglés. Los diálogos y canciones están en español.
4. Primero genera una **imagen de referencia** de Oryx y otra de Luna, y úsalas como referencia
   de personaje en todas las escenas si tu herramienta lo permite.
