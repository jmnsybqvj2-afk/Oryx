# Guía para producir Oryx y Luna en Kling

Las funciones de Kling cambian seguido según la versión y el plan. Esta guía funciona con clips
de **10 segundos o menos**. Si tu versión permite clips más largos, puedes unir dos tomas
seguidas en un solo clip.

## Paso 1 · Crear las imágenes de referencia (Kling Imagen)
Genera en la sección de imágenes de Kling, en formato 16:9, fondo liso:

**Oryx**
```
Character reference sheet of Oryx, a small cute alien child with chibi proportions, smooth
bright yellow skin, big round glossy black eyes with white sparkles, small smiling mouth,
two short antennae with round soft-orange tips poking out of his hood, wearing a green
one-piece dinosaur onesie pajama with the hood up, white felt teeth on the hood edge, small
orange spikes on the back and a short stubby dinosaur tail. Front view, side view, back
view. Soft 3D cartoon style for toddlers, bright saturated colors, plain light blue background.
```

**Luna**
```
Character reference sheet of Luna, a tiny cream and fawn colored chihuahua puppy, big
upright ears, big shiny brown eyes, pink collar with a small golden moon-shaped tag. Front
view, side view, sitting and standing. Soft 3D cartoon style for toddlers, bright saturated
colors, plain light green background.
```

**Rosa** (solo episodio 1)
```
Character reference sheet of Rosa, a kind middle-aged park ranger woman, green ranger
uniform, ranger hat, gardening gloves, warm smile. Front view and side view. Soft 3D
cartoon style for toddlers, plain light yellow background.
```

**La nave**
```
A round shiny yellow cartoon spaceship with a small round door, soft glowing lights around
the edge, three short legs. Soft 3D cartoon style for toddlers, plain light blue background.
```

Genera varias opciones de cada uno y quédate con la que más te guste. **Esa imagen será
Oryx (o Luna) para siempre.**

## Paso 2 · Crear los Elements (personajes guardados)
En Kling, crea un Element por personaje con sus imágenes de referencia (Kling acepta varias
imágenes por Element): **Oryx**, **Luna**, **Rosa** y **Nave**.
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
  `Soft 3D cartoon for toddlers, bright saturated colors, gentle warm lighting.`

## Tomas comunes (entrada y salida, se generan una sola vez)

**Entrada · T1 · 10 s** · Elements: Nave, Oryx, Luna
```
A round shiny yellow spaceship flies across a bright blue sky with puffy clouds and lands
softly on green grass in a park, the door opens and Oryx steps out waving, his antenna tips
glow red, Luna jumps out next to him wagging her tail. Static wide shot, then slow push in.
Soft 3D cartoon for toddlers, bright saturated colors, gentle warm lighting.
```
**Entrada · T2 · 5 s** · Elements: Oryx, Luna
```
Oryx and Luna stand side by side smiling at the camera, Oryx makes a playful dinosaur claw
pose and roars, Luna barks happily. Static medium shot, space at the top for a logo.
Soft 3D cartoon for toddlers, bright saturated colors, gentle warm lighting.
```
**Salida · T1 · 10 s** · Elements: Oryx, Luna
```
Sunset in a green park, Oryx sits next to Luna and opens a small notebook full of colorful
animal stickers, then both put a hand and paw on their heart and smile. Slow push in.
Soft 3D cartoon for toddlers, bright saturated colors, gentle warm sunset lighting.
```
**Salida · T2 · 10 s** · Elements: Oryx, Luna, Nave
```
Oryx and Luna stand next to the round yellow spaceship at sunset and wave goodbye to the
camera, the spaceship floats a little above the ground glowing softly. Slow pull back.
Soft 3D cartoon for toddlers, bright saturated colors, gentle warm sunset lighting.
```
