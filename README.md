# YouTube AI Content Repurposing Suite

[![Project Status](https://img.shields.io/badge/Status-Complete-green?style=for-the-badge)]()

An end-to-end web application designed to break down language barriers and make video content more accessible. This tool takes any YouTube video link, automatically extracts its transcript, translates it into multiple languages, and converts the translated text into high-quality audio, providing a complete solution for content consumption and repurposing.

![Untitled video - Made with Clipchamp (3) (online-video-cutter com)](https://github.com/user-attachments/assets/606b564a-b5be-4194-bd75-c1cf9c350571)

---

## 📖 Introduction

In an increasingly global world, a vast amount of valuable information on platforms like YouTube remains locked behind language barriers. The **YouTube AI Content Repurposing Suite** was built to solve this problem by creating a seamless, multi-modal content transformation pipeline.

Users can simply provide a YouTube link and instantly receive the video's content as a readable transcript, a translated document in one of several supported languages, and a high-quality audio file for on-the-go listening. This project demonstrates a practical application of API integration and automated content processing to create a high-value tool for students, professionals, and content creators worldwide.

---

## ✨ Core Features

-   **📝 Automated Transcription:** Integrates with the `youtube-transcript-api` to instantly pull available subtitles from any YouTube video, eliminating the need for manual transcription.
-   **🌐 Multi-Language Translation:** Utilizes the `deep-translate` library to translate the extracted transcript into English, Telugu, French, Spanish, and Hindi.
-   **⚙️ Robust Text Chunking:** Implements a custom logic to split large transcripts into smaller chunks before translation, successfully handling API character limits and ensuring the accurate processing of long-form content.
-   **🔊 Text-to-Speech Conversion:** Converts the final translated text into a high-quality audio file using Google Text-to-Speech (`gTTS`), making the content accessible via listening.
-   **📥 Multi-Format Downloads:** Allows users to download the original transcript, the translated text, and the generated audio file, providing ultimate flexibility.
-   **✔️ Graceful Error Handling:** Provides clear user feedback when a video does not have an available transcript, ensuring a smooth user experience.

---

## 🔧 Tech Stack & Architecture

| Component              | Technology / Library      | Purpose                                                                   |
| :--------------------- | :------------------------ | :------------------------------------------------------------------------ |
| **Core Logic**         | Python                    | The primary language for backend processing and API orchestration.        |
| **Web Framework**      | Flask                     | To build the API endpoint that handles user requests.      |
| **API Integration**    | `youtube-transcript-api`  | For automated extraction of video subtitles.                              |
| **Translation Engine** | `deep-translate`          | For translating text between supported languages.                         |
| **Audio Generation**   | `gTTS`                    | For converting translated text into listenable audio files.               |
| **Frontend**           | HTML/CSS, JavaScript      | For building the user-facing interface.       |

---

## 🚀 Running the Project Locally

To run this project on your local machine, follow these steps.

### Prerequisites

-   Python 3.8+
-   `pip` (Python package installer)

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://your-repo-link.com
    cd youtube-ai-suite
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```
3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the application:**
    ```bash
    flask run  # Or `uvicorn main:app --reload` if using FastAPI
    ```
5.  Open your web browser and navigate to `http://127.0.0.1:5000` to use the application.
