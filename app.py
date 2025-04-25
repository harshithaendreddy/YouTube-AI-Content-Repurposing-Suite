from flask import Flask, render_template, request, send_from_directory
from youtube_transcript_api import YouTubeTranscriptApi
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

app = Flask(__name__)

AUDIO_FOLDER = "static/audio"
TRANSCRIPT_FOLDER = "static/transcripts"
os.makedirs(AUDIO_FOLDER, exist_ok=True)
os.makedirs(TRANSCRIPT_FOLDER, exist_ok=True)

def extract_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1]
    else:
        raise ValueError("Invalid YouTube URL format")

def split_text(text, max_length=5000):
    words = text.split()
    chunks, current = [], ""
    for word in words:
        if len(current) + len(word) + 1 <= max_length:
            current += " " + word if current else word
        else:
            chunks.append(current)
            current = word
    if current:
        chunks.append(current)
    return chunks

@app.route("/", methods=["GET", "POST"])
def index():
    transcript_text = ""
    translated_text = ""
    audio_file = ""
    transcript_file = ""
    translated_file = ""
    video_id = ""
    selected_lang = ""

    if request.method == "POST":
        action = request.form["action"]
        youtube_url = request.form["youtube_url"]
        video_id = extract_video_id(youtube_url)

        if action == "get_transcript":
            try:
                transcript = YouTubeTranscriptApi.get_transcript(video_id)
                transcript_text = " ".join([entry['text'] for entry in transcript])
                transcript_file = f"{video_id}_original.txt"
                with open(os.path.join(TRANSCRIPT_FOLDER, transcript_file), "w", encoding="utf-8") as f:
                    f.write(transcript_text)
            except Exception as e:
                transcript_text = f"❌ Error: {str(e)}"

        elif action == "translate":
            selected_lang = request.form["language"]
            try:
                with open(os.path.join(TRANSCRIPT_FOLDER, f"{video_id}_original.txt"), "r", encoding="utf-8") as f:
                    transcript_text = f.read()

                translated_chunks = []
                for chunk in split_text(transcript_text):
                    translated = GoogleTranslator(source='auto', target=selected_lang).translate(chunk)
                    translated_chunks.append(translated)
                translated_text = "\n".join(translated_chunks)

                translated_file = f"{video_id}_{selected_lang}_translated.txt"
                with open(os.path.join(TRANSCRIPT_FOLDER, translated_file), "w", encoding="utf-8") as f:
                    f.write(translated_text)

                tts = gTTS(text=translated_text, lang=selected_lang)
                audio_file = f"{video_id}_{selected_lang}.mp3"
                tts.save(os.path.join(AUDIO_FOLDER, audio_file))

            except Exception as e:
                translated_text = f"❌ Error: {str(e)}"

    return render_template("index.html",
                           transcript=transcript_text,
                           translated=translated_text,
                           audio_file=audio_file,
                           transcript_file=transcript_file,
                           translated_file=translated_file,
                           language=selected_lang)

@app.route("/audio/<filename>")
def get_audio(filename):
    return send_from_directory(AUDIO_FOLDER, filename)

@app.route("/transcripts/<filename>")
def get_transcript(filename):
    return send_from_directory(TRANSCRIPT_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)