#!/usr/bin/env python3
"""Build the episode 1 draft (animatic) from the clips, still plates and audio."""
import os, re, subprocess, sys

W = os.path.dirname(os.path.abspath(__file__))
CH = "/home/user/Oryx/channel"
EP = f"{CH}/episode-01-pio-pio-pajarito"
SH = f"{CH}/shared"
FONT = "/usr/share/fonts/opentype/inter/InterDisplay-Black.otf"
FPS = 30
GAP = 0.35
SEG = f"{W}/seg"
os.makedirs(SEG, exist_ok=True)

CLIP = {
    "saucer": f"{SH}/presentation/flying-saucer-and-luna-16x9.mp4",
    "night_end": f"{SH}/presentation/oryx-good-night-16x9.mp4",
    "s03": f"{EP}/clips/scene03-bip-bip-baby-bird.mp4",
    "s04": f"{EP}/clips/scene04-luna-barks-oryx-confused.mp4",
    "s05": f"{EP}/clips/scene05-question-to-kids.mp4",
    "s09": f"{EP}/clips/scene09-sticker.mp4",
    "s10": f"{EP}/clips/scene10-what-did-we-learn.mp4",
}
PLATE = {"day": f"{W}/plates/day.png", "night": f"{W}/plates/night.png"}
VO = lambda n: f"{W}/vo/{n}.wav"
A_OPEN = f"{SH}/audio/opening-song-oryx-y-luna.m4a"
A_CLOSE = f"{SH}/audio/closing-song-adios-terricolas.m4a"
A_SONG = f"{EP}/audio/song-pio-pio-pajarito.m4a"
A_WELCOME = f"{EP}/audio/narrator-welcome.m4a"
A_REFLECT = f"{EP}/audio/narrator-reflection.m4a"
SONG_SRT = f"{EP}/audio/song-pio-pio-pajarito-lyrics.srt"

# Cover the "KlingAI" watermark (bottom right) with a small channel tag
COVER = ("drawbox=x=1690:y=1008:w=230:h=64:color=0x1d2b6b@0.92:t=fill,"
         f"drawtext=fontfile={FONT}:text='Oryx y Luna':fontsize=30:fontcolor=white:x=1712:y=1025")


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(" ".join(cmd)); print(r.stderr[-2000:]); sys.exit(1)


def dur(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", path], capture_output=True, text=True).stdout
    return float(out.strip())


# ---------- video parts ----------
MOVES = {
    "in":   ("1+0.10*on/{n}", "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"),
    "out":  ("1.10-0.10*on/{n}", "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"),
    "up":   ("1.12", "iw/2-(iw/zoom/2)", "(ih-ih/zoom)*(1-on/{n})"),
    "down": ("1.12", "iw/2-(iw/zoom/2)", "(ih-ih/zoom)*on/{n}"),
    "left": ("1.12", "(iw-iw/zoom)*(1-on/{n})", "ih/2-(ih/zoom/2)"),
    "right":("1.12", "(iw-iw/zoom)*on/{n}", "ih/2-(ih/zoom/2)"),
}


def part_plate(out, plate, d, move):
    n = max(1, round(d * FPS))
    z, x, y = (s.format(n=n) for s in MOVES[move])
    vf = f"zoompan=z='{z}':x='{x}':y='{y}':d={n}:s=1920x1080:fps={FPS},format=yuv420p"
    run(["ffmpeg", "-v", "error", "-y", "-i", PLATE[plate], "-vf", vf, "-frames:v", str(n),
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", out])


def part_clip(out, clip, d, start=0.0):
    length = dur(CLIP[clip]) - start
    pad = max(0.0, d - length + 0.1)
    vf = (f"scale=1920:1080:flags=lanczos,fps={FPS},{COVER},"
          f"tpad=stop_mode=clone:stop_duration={pad:.2f},format=yuv420p")
    run(["ffmpeg", "-v", "error", "-y", "-ss", f"{start}", "-i", CLIP[clip], "-an", "-vf", vf,
         "-t", f"{d:.3f}", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", out])


# ---------- audio ----------
def build_audio(out, items):
    """items: float = silence seconds, str = audio file path."""
    inputs, labels, k = [], [], 0
    for it in items:
        if isinstance(it, (int, float)):
            inputs += ["-f", "lavfi", "-t", f"{it}", "-i", "anullsrc=r=48000:cl=stereo"]
        else:
            inputs += ["-i", it]
        labels.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo[a{k}]")
        k += 1
    fc = ";".join(labels) + ";" + "".join(f"[a{i}]" for i in range(k)) + f"concat=n={k}:v=0:a=1[out]"
    run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", fc, "-map", "[out]",
         "-c:a", "pcm_s16le", out])
    return dur(out)


def times(items):
    """Start/end time of each audio item, to place on-screen words."""
    t, res = 0.0, []
    for it in items:
        d = it if isinstance(it, (int, float)) else dur(it)
        res.append((t, t + d)); t += d
    return res


def word(text, a, b):
    return (f"drawtext=fontfile={FONT}:text='{text}':fontsize=160:fontcolor=0xFFD93D:"
            f"borderw=12:bordercolor=0x1d2b6b:x=(w-tw)/2:y=70:enable='between(t,{a:.2f},{b:.2f})'")


def title(text, a, b, size=120):
    return (f"drawtext=fontfile={FONT}:text='{text}':fontsize={size}:fontcolor=white:"
            f"borderw=10:bordercolor=0x1d2b6b:x=(w-tw)/2:y=h-th-90:enable='between(t,{a:.2f},{b:.2f})'")


# ---------- segment ----------
def segment(name, audio_items, video_parts, overlays=(), subs=None, afade_out=0.0):
    print("segment", name, flush=True)
    a = f"{SEG}/{name}.wav"
    total = build_audio(a, audio_items)
    # stretch the last video part so video == audio
    known = sum(p[2] for p in video_parts[:-1])
    video_parts[-1] = (*video_parts[-1][:2], round(total - known, 3), *video_parts[-1][3:])
    files = []
    for i, p in enumerate(video_parts):
        f = f"{SEG}/{name}_p{i}.mp4"
        if p[0] == "plate":
            part_plate(f, p[1], p[2], p[3])
        else:
            part_clip(f, p[1], p[2], p[3] if len(p) > 3 else 0.0)
        files.append(f)
    lst = f"{SEG}/{name}_list.txt"
    open(lst, "w").write("".join(f"file '{f}'\n" for f in files))
    vf = list(overlays)
    if subs:
        vf.append(f"subtitles={subs}:force_style='Fontname=Inter Display Black,Fontsize=24,"
                  "PrimaryColour=&H00FFFFFF,OutlineColour=&H006B2B1D,BorderStyle=1,Outline=3,"
                  "Shadow=0,MarginV=22'")
    af = f"afade=t=out:st={total-afade_out:.2f}:d={afade_out}" if afade_out else "anull"
    cmd = ["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", a]
    if vf:
        cmd += ["-vf", ",".join(vf)]
    cmd += ["-af", af, "-map", "0:v", "-map", "1:a", "-t", f"{total:.3f}",
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "23", "-r", str(FPS),
            "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
            f"{SEG}/{name}.mp4"]
    run(cmd)
    return f"{SEG}/{name}.mp4"


def clean_srt(src, dst):
    blocks = open(src, encoding="utf-8").read().strip().split("\n\n")
    keep = []
    for b in blocks:
        lines = b.split("\n")
        if len(lines) >= 3 and not lines[2].startswith("["):
            keep.append(lines)
    out = []
    for i, l in enumerate(keep, 1):
        out.append(f"{i}\n{l[1]}\n" + "\n".join(l[2:]))
    open(dst, "w", encoding="utf-8").write("\n\n".join(out) + "\n")
    return keep


def srt_time(s):
    h, m, rest = s.split(":"); sec, ms = rest.split(",")
    return int(h) * 3600 + int(m) * 60 + int(sec) + int(ms) / 1000


def main():
    segs = []
    # 1 Opening song
    segs.append(segment("01_opening", [A_OPEN],
        [("clip", "saucer", 10.0), ("plate", "night", 0, "in")],
        [title("Las aventuras de Oryx y Luna", 10.6, 23.5, 110)]))
    # 1b Narrator welcome
    segs.append(segment("02_welcome", [0.3, A_WELCOME, 0.5], [("plate", "day", 0, "in")]))
    # 2 Walk in the park
    segs.append(segment("03_scene2",
        [0.3, VO("T1-oryx-1"), GAP, VO("T1-luna-1"), GAP, VO("T2-oryx-1"), 0.3],
        [("plate", "day", 0, "right")]))
    # 3 Beep-beep (PLUMAS on screen)
    it = [0.2, VO("T3-oryx-1"), GAP, VO("T4-oryx-1"), 0.5]
    t = times(it)
    segs.append(segment("04_scene3", it, [("clip", "s03", 5.0), ("plate", "day", 0, "down")],
        [word("PLUMAS", t[3][0], t[4][1])]))
    # 4 Oryx gets it wrong
    it = [0.3, VO("T5-oryx-1"), GAP, VO("T6-oryx-1"), 0.3]
    t = times(it)
    segs.append(segment("05_scene4", it,
        [("plate", "day", round(t[2][1], 3), "in"), ("clip", "s04", 0)]))
    # 5 Question for the kids (3 s pause)
    segs.append(segment("06_scene5", [0.2, VO("T7-oryx-1"), 3.0], [("clip", "s05", 0)]))
    # 6 Luna translates (NIDO on screen)
    it = [0.3, VO("T8-luna-1"), GAP, VO("T9-luna-1"), GAP, VO("T10-oryx-1"), 0.3]
    t = times(it)
    segs.append(segment("07_scene6", it, [("plate", "day", 0, "up")],
        [word("NIDO", t[3][0], t[4][1] + 0.3)]))
    # 7 Asking a grown-up (VETERINARIA on screen)
    it = [0.3, VO("T11-oryx-1"), GAP, VO("T11-luna-1"), GAP, VO("T13-oryx-1"), GAP,
          VO("T13-luna-1"), GAP, VO("T13-rosa-1"), GAP, VO("T13-oryx-2"), 0.4]
    t = times(it)
    half = round(t[6][1], 3)
    segs.append(segment("08_scene7", it, [("plate", "day", half, "in"), ("plate", "day", 0, "out")],
        [word("VETERINARIA", t[7][0], t[8][1] + 0.3)]))
    # 8 Song with lyrics, PÁJARO and NIDO on screen
    clean = f"{SEG}/song.srt"
    lines = clean_srt(SONG_SRT, clean)
    pajaro = next(srt_time(l[1].split(" --> ")[0]) for l in lines if "Pío, pío, pajarito" in l[2])
    nido = next(srt_time(l[1].split(" --> ")[0]) for l in lines if "nido volverás" in l[2])
    segs.append(segment("09_song", [A_SONG],
        [("plate", "day", 14.0, "in"), ("clip", "s09", 5.0), ("plate", "day", 10.0, "left"),
         ("clip", "s03", 5.0), ("plate", "day", 10.0, "out"), ("clip", "s10", 5.0),
         ("clip", "s04", 5.0), ("plate", "day", 12.0, "up"), ("clip", "s09", 5.0),
         ("plate", "day", 12.0, "right"), ("plate", "night", 0, "in")],
        [title("Pío, pío, pajarito", 1.0, 13.0, 120), word("PÁJARO", pajaro, pajaro + 3.0),
         word("NIDO", nido, nido + 3.0)], subs=clean, afade_out=1.5))
    # 9 Celebration and sticker
    segs.append(segment("10_scene9", [0.2, VO("T20-oryx-1"), 0.5], [("clip", "s09", 0, 2.4)]))
    # 10 What did we learn
    it = [0.3, VO("T22-oryx-1"), GAP, VO("T22-luna-1"), GAP, VO("T22-oryx-2"), 0.4]
    segs.append(segment("11_scene10", it, [("clip", "s10", 5.0), ("plate", "day", 0, "in")]))
    # 10b Narrator reflection
    segs.append(segment("12_reflection", [0.3, A_REFLECT, 0.6], [("plate", "night", 0, "in")]))
    # 11 Closing song
    close_d = dur(A_CLOSE)
    segs.append(segment("13_closing", [A_CLOSE],
        [("plate", "night", round(close_d - 10.0, 3), "out"), ("clip", "night_end", 0)],
        [title("¡Hasta la próxima aventura!", 0.5, close_d - 10.5, 100)], afade_out=2.0))

    lst = f"{SEG}/all.txt"
    open(lst, "w").write("".join(f"file '{s}'\n" for s in segs))
    out = sys.argv[1]
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst,
         "-c:v", "libx264", "-preset", "medium", "-crf", "24", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out])
    print("done", out, round(dur(out), 1), "s")


if __name__ == "__main__":
    main()
