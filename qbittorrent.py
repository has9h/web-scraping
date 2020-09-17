from pickle import dump
from time import sleep, asctime, localtime
from re import search, sub
import logging
import os

logging.basicConfig(filename='logger.log', level=logging.INFO)
logging.info('Logger set to INFO')
logging.info(f'{asctime(localtime())}')

print('Current Directory: ', os.getcwd())

dir_path = 'H:\\Program Files\\Software\\7-Zip\\7z320\\z7289\\Completed\\O-P'
source_file = 'data/pruned.txt'

with open(source_file, encoding='utf-8', errors='ignore') as f:
    dir_list = os.listdir(dir_path)
    error_list = []
    hit_list = []

    # For each line in file
    for idx, line in enumerate(f.readlines()):
        logging.info(f'Current line: {idx}, {line}')
        
        # Check with each file in directory
        for file in dir_list:
            print('Current dir file: ', file)
            file_stat = 0

            try:
                if not line[:15]:
                    logging.warning(f'Need more characters for {line}')
                    error_list.append((idx, line))
                    continue
                if search(line[:15], str(sub('(.t\d{7} - )|(.torrent)$', '', file))):
                    logging.info(f'Match found:\n {idx}, {line} in file {file}')
                    hit_list.append((idx, line))
                    file_stat = 1

                    os.startfile(os.path.join(dir_path, file))
                    sleep(1.2)
                    break
                else:
                    print('Target unmatched')
            except Exception as err:
                logging.exception(f'{err} Exception raised; \n Logging and continuing to next file')
                error_list.append((idx, line))
                continue
        # sleep(0.5)
        if file_stat == 0:
            logging.warning(f'{line} not found. Logging and continuing')
            error_list.append((idx, line))
    
    with open('errors.pkl', 'wb') as writer:
        dump(error_list, writer)
    
    with open('matches.pkl', 'wb') as writer:
        dump(hit_list, writer)
