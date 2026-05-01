from video_engine import generate_ai_video

if __name__ == "__main__":
    script_text = "Welcome to our new AI reel generator. This is a test video to see if the text to speech and background image work perfectly!"
    output = generate_ai_video(script_text, "test_output.mp4")
    if output:
        print(f"Success! Video generated at {output}")
    else:
        print("Failed to generate video.")
