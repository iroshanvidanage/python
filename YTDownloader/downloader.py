from pytube import YouTube


def on_complete(stream, filepath):
    print('Download Complete')
    print(filepath)


def on_progress(stream, chunk, bytes_remaining):
    progress_str = f'100 - {round(bytes_remaining / stream.filesize * 100, 2)}'
    print(progress_str)


link = input("The Link to Download: ")
video_down = YouTube(link, on_complete_callback=on_complete, on_progress_callback=on_progress)

print(f'Title:  {video_down.title}')
print(f'Length:  {video_down.length}')
print(f'Author:  {video_down.author}')

print(f'Download options: (b)est | (w)orst | (a)udio | (e)xit')

down_opt = input('Select option:')

opt = {'b': video_down.streams.get_highest_resolution().download(r'C:\Users\user\Downloads\Video'),
       'w': video_down.streams.get_lowest_resolution().download(r'C:\Users\user\Downloads\Video'),
       'a': video_down.streams.get_audio_only().download(r'C:\Users\user\Downloads\Video')}

opt[down_opt]
