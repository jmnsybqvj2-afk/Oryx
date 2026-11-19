# Episode 1 progress — "Pío, pío, pajarito"

## 🎬 Draft
- ✅ `draft/episode-01-draft-v1.mp4` — full episode (4:36) with all the audio, the 6 animated
  clips, and still images with slow camera moves where shots are still missing.
  Rebuilt with `../tools/build-episode-01-draft.py` when new shots arrive.

Finished clips are in `clips/`, named after the scene they belong to.
The shots (T1, T2…) are the ones in `07-kling-shots.md`.

## 🎬 Video

| Shot | Scene | Status | Clip |
|---|---|---|---|
| Opening | Flying saucer and Luna | ✅ | `../shared/presentation/flying-saucer-and-luna-16x9.mp4` |
| T1 | Walk in the park | ⬜ to do | |
| T2 | "There's no grass on my planet! RAWR!" | ⬜ to do | |
| T3 | Beep-beep! red antennae | ✅ | `clips/scene03-bip-bip-baby-bird.mp4` |
| T4 | They find the baby bird | ✅ | `clips/scene03-bird-found.mp4` (gray bird; has a cream border → crop ~6% in the edit) |
| T5 | Oryx wants to take it, Luna steps in front | ✅ | `clips/scene04-oryx-reaches-luna-stops.mp4` (cream border → crop in the edit) |
| T6 | Luna barks, Oryx confused | ✅ | `clips/scene04-luna-barks-oryx-confused.mp4` |
| T7 | "Do you know what it needs?" | ✅ | `clips/scene05-question-to-kids.mp4` |
| T8 | Luna listens to the baby bird | ✅ | `clips/scene06-luna-listens-nest.mp4` (first half) |
| T9 | Camera moves up to the nest and the mother | ✅ | `clips/scene06-luna-listens-nest.mp4` (second half) |
| T10 | Oryx surprised | ⬜ to do | |
| T11 | Rosa arrives | ⬜ to do | |
| T12 | Rosa puts the baby bird back in the nest | ❌ redo | `clips/REDO-scene07-rosa-with-text.mp4` (see below) |
| T13 | Rosa congratulates Oryx | ⬜ to do | |
| T14–T19 | Song (6 shots) | ⬜ to do | |
| T20 | Oryx jumps "RAWR!" | ⬜ to do | |
| T21 | Sticker in the Diary | ✅ | `clips/scene09-sticker.mp4` (use the 2nd half) |
| T22 | "What did we learn today?" | ✅ | `clips/scene10-what-did-we-learn.mp4` |
| Closing | Oryx falls asleep | ✅ | `../shared/presentation/oryx-good-night-16x9.mp4` |

**Done: 6 of 22 shots + opening and closing.**

### Why the Rosa shot (T12) has to be redone
1. It has **text drawn inside the video** ("¡RAWR! (feliz)…" and an unreadable "[EN PANTALLA…]").
   This happened because the Spanish script was pasted into Kling. It can't be removed afterwards.
2. Rosa is now a **veterinarian**, so the white coat is correct. The only problem is the text.

## 🎙️ Audio
- [x] Narrator welcome ✅ `audio/narrator-welcome.m4a` (18.7 s, volume adjusted to match the songs)
- [x] Narrator reflection ✅ `audio/narrator-reflection.m4a` (10.7 s, volume adjusted) — shown over the official night image
- [x] Voices for Oryx, Luna and Rosa (ElevenLabs) ✅ ALL 21 LINES — use `08-voices.md`. Saved in `audio/voices/`
      Oryx: ✅ ALL 14 lines done (T1, T2, T3, T4, T5, T6, T7, T10, T11, T13-1, T13-2, T20, T22-1, T22-2)
      Luna: ✅ ALL 6 lines done (T1, T8, T9, T11, T13, T22) — in T13 Luna explains "¡Es la doctora de los animales!"
      Rosa: ✅ 1 line done (T13)
- [x] Song "Pío, pío, pajarito" ✅ `audio/song-pio-pio-pajarito.m4a` (1:45, made in Suno — the "Pío" version)
      Timed lyrics for the on-screen text: `audio/song-pio-pio-pajarito-lyrics.srt`
      Parts: intro 0:00–0:14 · verse 1 0:14–0:29 · chorus 0:29–0:44 · verse 2 0:44–0:58 ·
      chorus 0:58–1:10 · chorus 1:10–1:24 · whispered ending 1:24–1:45
- [x] Opening song ✅ `../shared/audio/opening-song-oryx-y-luna.m4a` (24 s)
- [x] Closing song ✅ `../shared/audio/closing-song-adios-terricolas.m4a` (33 s)
- [ ] Effects: beep-beep, RAWR, woof, Luna's bell, birds
