# Guide to producing Oryx and Luna in Kling

Kling's features change often depending on the version and plan. This guide works with clips of
**10 seconds or less**. Each prompt makes **one** clip: an episode is built from many clips joined
together in the editor.

## Step 1 · Prepare the reference images
The official image is `references/oryx-and-luna-official.jpg` (night) and
`references/oryx-and-luna-day.png` (day). They are vertical and only show the characters from
the front, so it helps to create a few extra versions in **Kling Image**, uploading **the same
image** as the reference:

**Oryx full body, side and back view** (upload the official image as the reference)
```
Character reference sheet of the same alien child from the reference image: front view,
side view and back view, full body, neutral happy pose, two thin gray antennae with round
yellow balls on top, green dinosaur onesie with dinosaur face hood, long tail. Children's
storybook illustration style, hand-painted gouache and colored pencil texture, plain light
blue background.
```

**Luna from the side and walking** (upload the official image as the reference)
```
Character reference sheet of the same chihuahua puppy from the reference image: front view,
side view, sitting, walking, small brown and tan chihuahua with cream chest, red collar with a
small golden bell. Children's storybook illustration style, hand-painted gouache texture,
plain light green background.
```

**Rosa, the veterinarian** (upload the official image as a style reference)
```
Character reference sheet of Rosa, a kind young woman veterinarian with long brown hair,
white vet coat over a light blue shirt, blue gloves, a stethoscope around her neck, warm smile.
Front view and side view. Same children's storybook illustration style as the reference image,
hand-painted gouache texture, plain light yellow background.
```

**The flying saucer** (upload the official image as a style reference)
```
A classic cartoon flying saucer, lavender-gray metal, round glowing yellow lights around the
rim, light blue glass dome on top with a tiny antenna, warm yellow light beam shining down.
Same children's storybook illustration style as the reference image, hand-painted gouache
texture, starry night sky background.
```

## Step 2 · Create the Elements (saved characters)
In Kling, create one Element per character with its reference images (Kling accepts several
images per Element):
- **Oryx:** the official image + the day image + his view sheet.
- **Luna:** the official image + the day image + her view sheet.
- **Saucer:** the saucer image you generated.
- **Rosa:** her view sheet.

Check that each view sheet looks like the official image (gray antennae with yellow balls, red
collar with a bell). If one comes out different, don't use it: generate another one.
Each shot in the `07-kling-shots.md` files says which Elements to attach. Don't attach more
than needed: 2 or 3 characters per shot gives better results.

## Step 3 · Generate each shot
- **Format:** 16:9 for episodes, 9:16 for Shorts.
- **Length:** what each shot says (5 or 10 s).
- **Paste only the English text inside the box** of `07-kling-shots.md`. Never paste anything
  from the script or from `08-voices.md`: Kling draws it as text inside the video.
- **Negative prompt** (paste it on every shot):
```
realistic, photorealistic, scary, dark, horror, violence, blood, crying hard, distorted
face, deformed hands, extra limbs, extra fingers, text, letters, watermark, logo, blurry,
flickering, fast cuts, strobe lights, subtitles, captions, words, gun, pistol, weapon,
holster, knife, police
```
- Generate 2 or 3 versions of each shot and keep the best one.

### The first-frame trick (if the characters come out different)
1. In **Kling Image**, upload the day image and ask for the scene, for example:
   *"The same alien child and the same chihuahua puppy from the reference image, in a sunny
   colorful park with a big tree. Keep the characters exactly the same. Children's storybook
   illustration style, hand-painted gouache texture, 16:9."*
2. In **Video**, choose **image to video** and upload that image as the **first frame**.
3. In the prompt, write **only the movement** (for example: *"Oryx walks slowly and touches the
   grass, Luna trots beside him. Slow side tracking shot."*). Don't describe the characters again.

## Step 4 · Voices (recommended: separately + Lip Sync)
Kling can generate voices inside the video, but across a 20-shot episode Oryx's voice may come
out different in each one. So that Oryx and Luna **always sound the same**:
1. Record the voices yourself or generate them in ElevenLabs, always with the same voice.
   Write **"Oris"** in the voice text so the name is pronounced correctly.
2. Generate the shots in Kling **without dialogue**.
3. In shots where a character speaks, use Kling's **Lip Sync** with the audio of that line.
   If Lip Sync doesn't work well, put the voice on top in CapCut.

## Step 5 · Music
Kling doesn't make full songs. Generate the songs in a music app using the prompts and lyrics
in each `02-song.md` and in `opening-and-closing-songs.md`.

## Step 6 · Editing (CapCut or another editor)
Put the shots in order and add what Kling doesn't do well:
- **Text and graphics:** the question mark, the option icons (🍪💧🧸, 🎸💧☀️), the song lyrics
  and the logo.
- A **3-second pause** on the question for the kids (freeze the image or stretch the shot).
- **Sounds:** "¡bip-bip!", "¡RAWR!", "¡Guau!", Luna's bell and the ambience.
- If Kling added its own sound or music to a clip, remove it or turn it down.
- Cover the "KlingAI" watermark with the channel logo, or download without it on a paid plan.

## Tips for writing prompts in Kling
- One main action per shot. If two things happen, split it into two shots.
- Always call each character by the same name as their Element ("Oryx", "Luna").
- Say how the camera moves: *slow push in*, *slow pan*, *static shot*, *slow tilt up*.
- Always end with the same style:
  `Children's storybook illustration style, hand-painted gouache and colored pencil texture, warm soft lighting.`

## Shared shots (opening and closing, generated only once)

These happen **at night**: for these four, upload the official night image
(`references/oryx-and-luna-official.jpg`) as the reference instead of the day image.

**Opening · S1 · 10 s** · Elements: Saucer, Oryx, Luna
```
A flying saucer flies across a starry night sky with a crescent moon and lands
softly on green grass in a park, Oryx and Luna float down gently in its yellow light beam, Oryx waves, his antenna tips
glow red, Luna lands next to him wagging her tail. Static wide shot, then slow push in.
Children's storybook illustration style, hand-painted gouache and colored pencil texture, warm soft lighting.
```
**Opening · S2 · 5 s** · Elements: Oryx, Luna
```
Oryx and Luna stand side by side smiling at the camera, Oryx makes a playful dinosaur claw
pose and roars, Luna barks happily. Static medium shot, space at the top for a logo.
Children's storybook illustration style, hand-painted gouache and colored pencil texture, warm soft lighting.
```
**Closing · S1 · 10 s** · Elements: Oryx, Luna
```
Night in a green park under a crescent moon and stars, Oryx sits next to Luna and opens a small notebook full of colorful
animal stickers, then both put a hand and paw on their heart and smile. Slow push in.
Children's storybook illustration style, hand-painted gouache and colored pencil texture, warm soft moonlight.
```
**Closing · S2 · 10 s** · Elements: Oryx, Luna, Saucer
```
Oryx and Luna stand next to the flying saucer under a crescent moon and stars and wave goodbye to the
camera, the flying saucer floats a little above the ground glowing softly. Slow pull back.
Children's storybook illustration style, hand-painted gouache and colored pencil texture, warm soft moonlight.
```
