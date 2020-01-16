from yandex_music.client import Client
import requests
import os
import time
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

YA_LOGIN = config['YA MUSIC']['yaMusicLogin'];
YA_PASS = config['YA MUSIC']['yaMusicPass'];

TG_BOT_TOKEN = config['TG CONFIG']['botToken'];
TG_CHANNEL_CHAT_ID = config['TG CONFIG']['channel_chat_id'];

def downloadTrack(trackData):
    downloadInfoList = trackData.get_download_info()
    downloadInfoMp3 = None
    for downloadInfo in downloadInfoList:
        if downloadInfo.codec == "mp3":
            downloadInfoMp3 = downloadInfo
            break
    if downloadInfoMp3 == None:
        print("Not found mp3")
        return
    downloadDirectLink = downloadInfoMp3.get_direct_link();    
    title = trackData.title + " - "
    title += ", ".join(map(lambda artist: artist["name"], trackData.artists))
    print("Downloading " + title)
    trackFileName = title + ".mp3"
    trackFileName = trackFileName.replace("/", " ")
    trackData.download(trackFileName)
    apiLink = "https://api.telegram.org/bot" + TG_BOT_TOKEN + "/sendAudio"
    trackFile = open(trackFileName, 'rb')
    files = {'audio': trackFile}
    data = {
        'chat_id': TG_CHANNEL_CHAT_ID,
        'title': title,
        'caption': title,
    }
    resp = requests.post(apiLink, data, files=files)
    print(resp.text)
    trackFile.close()
    os.remove(trackFileName)

def main():
    print("Loading...")
    downloaded_arr = []
    downloaded_file = open('downloaded.txt', 'r+')
    for line in downloaded_file:
        downloaded_arr.append(int(line))
    downloaded_file.close()
    downloaded_file_a = open('downloaded.txt', 'a+')
    print("Feching metadata...")
    client = Client.from_credentials(YA_LOGIN, YA_PASS)
    playlists = client.users_playlists_list();

    for playlist in playlists:
        kind = playlist.kind
        playlistData = client.users_playlists(kind)[0]
        tracks = playlistData.tracks
        for track in tracks:
            if track.id in downloaded_arr:
                continue
            trackData = track.track
            downloaded_file_a.write(str(track.id))
            downloaded_file_a.write("\n")
            downloaded_arr.append(track.id)
            downloadTrack(trackData)
            time.sleep(5)

main()