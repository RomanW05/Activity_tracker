import os
from os import listdir
from os.path import isfile, join
import copy

settings = {
    'idle_time_in_seconds': 120,  # 120 seconds
}

programs = [
    'Sublime Text (UNREGISTERED)',
    'Select Command Prompt',
    'Command Prompt',
    'Mozilla Firefox',
    'Desktop',
    'Search',
    'Volume Control',
    'Program Manager',
    'Microsoft\u200b Edge',
    'Visual Studio Code',
    'Task Manager',
    'Xbox',
    'Steam',
    'Telegram',
    'File Explorer',
    'OpenOffice Writer',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    
]

'''

'''
raw_categories = {
    'Youtube': None,
    'Work': None,
    'Leisure': None,
    'Gaming': None,
    'Learning': None,
    'Email': None
}

def get_categories(raw_categories):
    Youtube = ['Youtube', 'youtube', 'Google Chrome', 'chrome']
    Work = ['Visual Studio Code', 'Stack Overflow', 'Python', 'python', 'clean code', 'clean architecture',
            'Oracle VM VirtualBox']
    Leisure = ['Meneame', 'meneame', 'boredpanda', 'Boredpanda']
    Gaming = ['Albion', 'Clash of clans']
    Learning = ['Coursera', 'coursera']
    Email = ['Mozilla Thunderbird']

    categories = copy.deepcopy(raw_categories)
    categories['Youtube'] = Youtube
    categories['Work'] = Work
    categories['Leisure'] = Leisure
    categories['Gaming'] = Gaming
    categories['Learning'] = Learning
    categories['Email'] = Email
    # categories['Idle'] = 0
    # categories['Unknown'] = None

    return categories



script_path = os.path.dirname(os.path.abspath(__file__))
logs = script_path + '/logs/'

def get_log_files():
    directories = os.listdir( logs )
    for file in directories:
        yield logs + file
    
