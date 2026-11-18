# Guía para producir Oryx y Luna en Kling

Las funciones de Kling cambian seguido según la versión y el plan. Esta guía funciona con clips
de **10 segundos o menos**. Si tu versión permite clips más largos, puedes unir dos tomas
seguidas en un solo clip.

## Paso 1 · Preparar las imágenes de referencia
Ya tienes las ilustraciones oficiales en `referencias/` (ver `personajes-y-estilo.md`).
Están en formato vertical, así que conviene crear con **Kling Imagen** algunas versiones extra
usando la imagen 01 como referencia:

**Oryx de cuerpo completo, de lado y de espaldas** (sube la imagen 01 como referencia)
```
Character reference sheet of the same alien child from the reference image: front view,
side view and back view, full body, neutral happy pose, two thin gray antennae with round
yellow balls on top, green dinosaur onesie with dinosaur face hood, long tail. Children's
storybook illustration style, hand-painted gouache and colored pencil texture, plain light
blue background.
```

**Luna de lado y caminando** (sube la imagen 01 como referencia)
```
Character reference sheet of the same chihuahua puppy from the reference image: front view,
side view, sitting, walking, small brown and tan chihuahua with cream chest, red collar with a
small golden bell. Children's storybook illustration style, hand-painted gouache texture,
plain light green background.
```

**Rosa** (no tiene imagen todavía; sube la imagen 01 como referencia de estilo)
```
Character reference sheet of Rosa, a kind middle-aged park ranger woman, green ranger
uniform, ranger hat, gardening gloves, warm smile. Front view and side view. Same
children's storybook illustration style as the reference image, hand-painted gouache
texture, plain light yellow background.
```

**Escena de día de prueba** (para confirmar que el estilo funciona de día)
```
The same alien child and chihuahua puppy from the reference image playing in a sunny green
park with a big tree and flowers, bright blue sky with soft clouds. Children's storybook
illustration style, hand-painted gouache and colored pencil texture, 16:9.
```

## Paso 2 · Crear los Elements (personajes guardados)
En Kling, crea un Element por personaje con sus imágenes de referencia (Kling acepta varias
imágenes por Element):
- **Oryx:** imagen 01 + la hoja de vistas que generaste (NO uses la 02, ahí no tiene antenitas).
- **Luna:** imágenes 01, 02 y 03 + su hoja de vistas.
- **Nave:** imagen 02 (el platillo volador).
- **Rosa:** su hoja de vistas.
En cada toma de los archivos `07-kling-tomas.md` se indica qué Elements adjuntar.
No adjuntes más de los necesarios: con 2 o 3 personajes por toma los resultados salen mejor.

## Paso 3 · Generar cada toma
- **Formato:** 16:9 para los episodios, 9:16 para los Shorts.
- **Duración:** la que dice cada toma (5 o 10 s).
- **Modo:** con Elements adjuntos, o de imagen a video si primero generas la imagen inicial de
  la escena con Kling Imagen (da más control).
- **Prompt negativo** (pégalo en todas las tomas):
```
realistic, photorealistic, scary, dark, horror, violence, blood, crying hard, distorted
face, deformed hands, extra limbs, extra fingers, text, letters, watermark, logo, blurry,
flickering, fast cuts, strobe lights
```
- Genera 2 o 3 versiones de cada toma y quédate con la mejor.

## Paso 4 · Voces (recomendado: por separado + Lip Sync)
Kling puede generar voces dentro del video, pero en un episodio de 25 tomas la voz de Oryx
puede salir distinta en cada una. Para que Oryx y Luna **suenen igual siempre**:
1. Graba tú las voces (o genéralas con una herramienta de voz) usando siempre la misma voz.
2. Genera las tomas en Kling **sin diálogo** (solo movimiento y, si quieres, efectos de sonido).
3. En las tomas donde un personaje habla, usa la función **Lip Sync** de Kling con el audio
   de esa línea, para que mueva la boca.

Si tu versión de Kling permite guardar también la voz en el Element del personaje, puedes
probar el audio nativo en español. Revisa que la voz suene igual de una toma a otra.

## Paso 5 · Música
Kling no hace canciones completas. Genera las canciones con una app de música usando los
prompts y letras de cada `02-cancion.md` y de `cancion-entrada-salida.md`.

## Paso 6 · Edición (CapCut u otro editor)
Une las tomas en orden y agrega lo que Kling no hace bien:
- **Textos y gráficos:** el signo de pregunta, los íconos de opciones (🍪💧🧸, 🎸💧☀️), la
  letra de las canciones y el logo. No se los pidas a Kling: los textos le salen mal.
- **Pausa de 3 segundos** en la pregunta a los niños (congela la imagen o alarga la toma).
- **Sonidos:** "¡bip-bip!", "¡RAWR!", "¡Guau!" y el ambiente.

## Consejos para escribir prompts en Kling
- Una acción principal por toma. Si pasan dos cosas, divídelo en dos tomas.
- Nombra siempre al personaje igual ("Oryx", "Luna") que su Element.
- Di cómo se mueve la cámara: *slow push in*, *slow pan*, *static shot*, *slow tilt up*.
- Termina siempre con el mismo estilo:
  `Children's storybook illustration style, hand-painted gouache and colored pencil texture, warm soft lighting.`

## Tomas comunes (entrada y salida, se generan una sola vez)

**Entrada · T1 · 10 s** · Elements: Nave, Oryx, Luna
```
A flying saucer flies across a starry night sky with a crescent moon and lands
softly on green grass in a park, Oryx and Luna float down gently in its yellow light beam, Oryx waves, his antenna tips
glow red, Luna lands next to him wagging her tail. Static wide shot, then slow push in.
Children's storybook illustration style, hand-painted gouache and colored pencil texture, warm soft lighting.
```
**Entrada · T2 · 5 s** · Elements: Oryx, Luna
```
Oryx and Luna stand side by side smiling at the camera, Oryx makes a playful dinosaur claw
pose and roars, Luna barks happily. Static medium shot, space at the top for a logo.
Children's storybook illustration style, hand-painted gouache and colored pencil texture, warm soft lighting.
```
**Salida · T1 · 10 s** · Elements: Oryx, Luna
```
Night in a green park under a crescent moon and stars, Oryx sits next to Luna and opens a small notebook full of colorful
animal stickers, then both put a hand and paw on their heart and smile. Slow push in.
Children's storybook illustration style, hand-painted gouache and colored pencil texture, warm soft moonlight.
```
**Salida · T2 · 10 s** · Elements: Oryx, Luna, Nave
```
Oryx and Luna stand next to the flying saucer under a crescent moon and stars and wave goodbye to the
camera, the flying saucer floats a little above the ground glowing softly. Slow pull back.
Children's storybook illustration style, hand-painted gouache and colored pencil texture, warm soft moonlight.
```
