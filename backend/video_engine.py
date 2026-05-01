import os
from gtts import gTTS
from moviepy import ImageClip, AudioFileClip, ColorClip

def generate_ai_video(script_text: str, output_filename: str = "output_reel.mp4"):
    """
    Generates a simple AI video by converting text to speech
    and overlaying it on a static background image.
    """
    try:
        # 1. Generate Audio from Text using gTTS
        print("Generating audio...")
        audio_filename = "temp_audio.mp3"
        tts = gTTS(text=script_text, lang='en', slow=False)
        tts.save(audio_filename)

        # 2. Create Video using moviepy
        print("Generating video...")
        background_image_path = "background.png"
        
        # Load the audio file
        audio_clip = AudioFileClip(audio_filename)
        audio_duration = audio_clip.duration

        # Load the background image
        # If no background image exists, we create a solid color clip (black)
        if os.path.exists(background_image_path):
            video_clip = ImageClip(background_image_path)
        else:
            video_clip = ColorClip(size=(1080, 1920), color=(0, 0, 0))

        # Set duration and add audio
        video_clip = video_clip.with_duration(audio_duration)
        video_clip = video_clip.with_audio(audio_clip)
        
        # Set frames per second
        video_clip.fps = 24

        # Write to file
        print(f"Saving video to {output_filename}...")
        video_clip.write_videofile(
            output_filename, 
            codec="libx264", 
            audio_codec="aac", 
            temp_audiofile="temp-audio.m4a", 
            remove_temp=True,
            fps=24
        )

        # Clean up temporary audio file
        if os.path.exists(audio_filename):
            os.remove(audio_filename)

        return output_filename

    except Exception as e:
        print(f"Error generating video: {e}")
        return None
