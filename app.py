import whisper
import os
import shutil
from moviepy.editor import AudioFileClip,VideoFileClip

model = whisper.load_model("base")


def segments_twenty_minutes(mp3_file_path, video_id):
    mp3_audio = AudioFileClip(mp3_file_path)
    segment_duration_seconds = 1200  # 20 minutes in seconds
    start = 0
    counter = 0
    n = round(mp3_audio.duration)
    path = os.path.join(os.getcwd(), f'{video_id}')
    os.mkdir(path)
    
    while start < n:
        audio_clip = AudioFileClip(mp3_file_path)
        
        end = min(start + segment_duration_seconds, n)  # Ensure the segment doesn't exceed the video duration

        temp = audio_clip.subclip(start, end)
        temp_file = os.path.join(os.getcwd(), f'{video_id}', f'{counter}.mp3')
        temp.write_audiofile(filename=temp_file, codec='mp3')
        temp.close()
        counter += 1
        start = end

        audio_clip.close()
        
    return path
 


def get_transcript(file_path,language_code,video_id):
  mp3file_size_bytes = os.path.getsize(file_path)
  
  whisper_default_size = 25*1024*1024 #25 MB in bytes
  if(mp3file_size_bytes < whisper_default_size): # check if given file is smaller than 25 MB
        result = model.transcribe(file_path,language=language_code)['text']
        os.remove(file_path)
        return result
  else:
        transcribed_text = []
        segmented_files_dir = segments_twenty_minutes(file_path, video_id) # function call for segmennting video into small segments
        files_list = os.listdir(segmented_files_dir)
        for index in range(len(files_list)):
            audio_segment_path = os.path.join(segmented_files_dir,f'{index}.mp3')
            result = model.transcribe(audio_segment_path,language=language_code)['text']
            transcribed_text.append(result)
        shutil.rmtree(segmented_files_dir)
        os.remove(file_path)
        return transcribed_text



def convert_to_mp3_and_transcript(mp4_file_path,language,file_id):
     # Load the MP4 video file
    video_clip = VideoFileClip(mp4_file_path)
    
    # Get the file name without the extension
    file_name = os.path.splitext(os.path.basename(mp4_file_path))[0]
    
    # Define the output MP3 file path
    mp3_file_path = os.path.join(os.path.dirname(mp4_file_path), f'{file_name}.mp3')
    # Convert and save as MP3
    video_clip.audio.write_audiofile(mp3_file_path, codec='mp3')
    
    transcript= get_transcript(mp3_file_path,language,file_id)
    return transcript


print(convert_to_mp3_and_transcript("a1.mp4","en","2222"));

