# from qbittorrent import Client
# import qbittorrentapi

# for files in os.listdir(dir_path):
#     if fnmatch(files, f'*{line}*'):
#         print(f'{line} found')
#         break
#     else:
#         print(f'{line} not found')

# Connect to qbittorrent Web UI
# qbt_client = qbittorrentapi.Client(host='http://127.0.0.1', port=8080, username='admin', password='adminadmin')
# qb = Client('http://127.0.0.1:8080/')

# qbt_client.auth_log_in(username='admin', password='adminadmin')
# Credentials
# qbt_client.torrents_add(torrent_files=file)

# try:
#     qbt_client.auth_log_in()
# except qbittorrentapi.LoginFailed as e:
    # print(e)

# qb.login('admin', 'adminadmin')

# # Torrent
# with open(file, 'rb') as f:
#     # Download
#     qb.download_from_file(f)
