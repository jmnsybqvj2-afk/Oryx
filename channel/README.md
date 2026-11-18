# 🛸 Oryx and Luna — Production folder

```
channel/
├── README.md                          ← this file
├── channel-bible.md                   ← overview of the channel
├── shared/                            ← used in EVERY episode
│   ├── kling-guide.md                 ← ⭐ how to produce in Kling, step by step
│   ├── characters-and-style.md        ← how Oryx and Luna look and sound + prompt blocks
│   ├── opening-and-closing-songs.md   ← opening and closing songs + music prompts
│   ├── youtube-settings.md            ← how to upload each video (Made for Kids, etc.)
│   ├── references/                    ← official character images and channel avatar
│   └── presentation/                  ← channel trailer and presentation clips
├── episode-01-pio-pio-pajarito/
├── episode-02-agua-fresca/
└── episode-03-crece-florecita/
```

Each episode folder has:

| File | What it contains |
|---|---|
| `01-script.md` | Full script by scene, with timings, dialogue and what's on screen |
| `02-song.md` | Lyrics, music style, moves for the kids and the prompt to generate the music |
| `03-title-and-thumbnail.md` | Title, alternatives, thumbnail design and the prompt to generate it |
| `04-description-and-tags.md` | Description ready to paste into YouTube, tags and hashtags |
| `05-video-prompts.md` | One prompt per scene for other AI video tools |
| `06-production-checklist.md` | Step-by-step list, from recording voices to publishing |
| `07-kling-shots.md` | ⭐ **The shots for Kling**: only English prompts, ready to paste (with the negative prompt at the top) |
| `08-voices.md` | 🎙️ **The dialogue for ElevenLabs**: only Spanish lines, one box per line, with the audio file name |
| `PROGRESS.md` | Which shots are done and which are missing (episode 1 for now) |
| `clips/` | Finished clips, named after their scene |

## Language
Everything is in English **except the dialogue and the songs**, which are in Spanish because
that is what the kids hear. The YouTube titles and descriptions are also in Spanish, because the
channel's viewers read them.
- **Kling (video):** `07-kling-shots.md` → only English.
- **ElevenLabs (voices):** `08-voices.md` → only Spanish.

## If you use Kling (recommended)
Start with `shared/kling-guide.md`, then use the `07-kling-shots.md` of each episode. Those
prompts are complete: no tags to replace.

## Using the general prompts (`05-video-prompts.md`, for other tools)
1. Open `shared/characters-and-style.md` and copy the **[STYLE]**, **[ORYX]** and **[LUNA]** blocks.
2. In each scene prompt, replace those tags with the full block. Always using the same text is
   what keeps the characters the same in every scene.
3. The prompts are in English because most AI video and image tools understand English better.
