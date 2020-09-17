import pickle

error_file = open('errors.pkl', 'rb')
matches_file = open('matches.pkl', 'rb')

error_list = list(set(pickle.load(error_file)))
match_list = list(set(pickle.load(matches_file)))
