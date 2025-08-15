music = {
    "skyfall": "https://youtu.be/sZrTJesvJeo?si=g1YjCxXF4m_0XA3M",
    "believer": "https://youtu.be/W0DM5lcj6mw?si=vvSwQR-Jg_RnNn9l",
    "hall of fame": "https://youtu.be/3Kxf2dHlDpQ?si=7s-iETxixxVeLHbQ",
}

def play_music(song_name):
    song_name = song_name.lower().strip()
    return music.get(song_name, None)
