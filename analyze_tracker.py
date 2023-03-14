from parameters import settings, raw_categories, get_log_files, get_categories
import datetime
import copy

'''
Objectives:
    - Tell for how long a window remained opened
    - Group windows into categories
        - Create categories
            - Discern between work and pleasure
        - Include those windows into those categories
    - Clean empty rows
    - Display graphics and statistics
    - Detect movements (go to another window but very soon after come back)
'''


def time_task_divider(line:str):
    # print(line)
    splited = line.split('|')
    date = splited[0]
    activity = splited[1]

    time = date.split(' ')
    day = time[0]
    hour = time[1]
    
    return hour, activity


def text_parser(line:str) -> str:
    if '-' in line and '—' in line:
        delimiter = ['-', '—']
        pattern = 1
    if '-' in line and '—' not in line:
        delimiter = ['-']
        pattern = 2
    if '-' not in line and '—' in line:
        delimiter = ['—']
        pattern = 3
    if '-' not in line and not '—' in line:
        delimiter = []
        pattern = 4
    
    match pattern:
        case 1:
            pass

    



def elapsed_time(time1:str, time2:str) -> int:
    date1 = datetime.datetime.strptime(time1, '%H:%M:%S')
    date2 = datetime.datetime.strptime(time2, '%H:%M:%S')
    difference = date2 - date1

    return int(difference.total_seconds())


def task_delimiter(delimiter:str, task:str) -> list:
    tasks = task.split(delimiter)
    return tasks


def create_module(elapsed_time: int, active_window: str) -> dict:
    activity: dict[str: str|None]
    activity = {
        'layer_0_program_name': None,
        'layer_1_task_name': None,
        'layer_2_file_name': None,
        'duration': elapsed_time,
        'category': None
        }
    
    active_window = active_window[1:]
    active_window = active_window.replace('\n', '')

    delimiter1 = '—'
    delimiter2 = '-'
    delimiter = ''
    if delimiter1 in active_window:
        delimiter = delimiter1
    elif delimiter2 in active_window:
        delimiter = delimiter2
    else:
        if len(active_window) > 3:
            activity['layer_0_program_name'] = active_window
        else:
            activity['layer_0_program_name'] = 'Desktop'
        return activity

    tasks = task_delimiter(delimiter, active_window)
    if tasks[-1][0] == ' ':  # There is a space in front
        tasks[-1] = tasks[-1][1:]
    activity['layer_0_program_name'] = tasks[-1]
    activity['layer_1_task_name'] = tasks[-2]
    
    return activity


def category_selection(dictionary:dict, categories:dict) -> dict:
    for keyword in categories.items():
        # print(dictionary['layer_0_program_name'], 'task name')
        if dictionary['layer_0_program_name'] in keyword[1]:
            dictionary['category'] = keyword[0]
            return dictionary

    return dictionary


def get_task(line_from_readlines:str, old_time:str, categories:dict):
    new_time, active_window = time_task_divider(line_from_readlines)
    elapsed_seconds = elapsed_time(old_time, new_time)
    task_dictionary = create_module(elapsed_seconds, active_window)
    task_dictionary = category_selection(task_dictionary, categories)
    old_time = new_time
    return task_dictionary, old_time


def read_file(file):
    with open(file, 'r', encoding='utf-8') as text:
        for index, line in enumerate(text.readlines()):
            yield index, line


def refine(idle_time_in_seconds, task):
    # Second refinary
    if task['duration'] > idle_time_in_seconds and 'Yotube' not in task['layer_0_program_name']:  # Strong signs of idleing
        # print(task['duration'], task['layer_0_program_name'])
        task['category'] = 'Idle'

    return task

def validate_task(task: dict) -> dict:
    if task['category'] is None:
        task['category'] = 'Not defined'
    return task



# def statistics(task:dict, category:dict, single_session_schema:dict, single_session_duration:int, single_session_straight:list):
def test_main():
    # for day in log:
        # pie_activity, linear_activity, daily_activity = extract_activity(day)
    pass

def extract_program(activity):
    if '-' in activity:
        delimiter = '-'
    elif '—' in activity:
        delimiter = '—'
    elif '—' in activity:
        delimiter = '—'
    else:
        try:
            while activity[0] == ' ':
                activity = activity[1:]
        except:
            pass
        return activity
    
    program = activity.split(delimiter)[-1]
    while program[0] == ' ':
        program = program[1:]
    return program
    

def extract_activity(index: int, line: str):
    activities_as_pie: dict
    activities_as_linear: dict
    old_time: str
    activity_type: str
    activity_duration: int

    activities_as_pie = {}
    activities_as_linear = {}
    old_time = '00:00:00'

    new_time, activity_type = time_task_divider(line)
    activity_type = extract_program(activity_type)
    activity_duration = elapsed_time(old_time, new_time)
    old_time = new_time

    try:
        activities_as_pie[activity_type] += activity_duration
    except:
        activities_as_pie[activity_type] = activity_duration

    activities_as_linear[index] = {'activity_type': activity_type, 'activity_duration': activity_duration}
    
    return activities_as_pie, activities_as_linear
        

def extract_activity_type(line):
    time, task = time_task_divider(line)


def clean_line(line):
    line = line.replace('\n', '')
    while line[0] == ' ':
        line = line[1:]
    return line

def main():
    all_sessions_schema: dict
    all_sessions_duration: int
    all_sessions_straight: list  # What happens event after event

    single_session_schema: dict
    single_session_duration: int
    single_session_straight: list

    all_sessions_schema = raw_categories
    all_sessions_schema = raw_categories
    all_sessions_schema = copy.deepcopy(raw_categories)
    for key, value in all_sessions_schema.items():
        all_sessions_schema[key] = 0
    all_sessions_schema['Idle'] = 0
    all_sessions_schema['Not defined'] = 0
    all_sessions_duration = 0
    all_sessions_straight = []
    

    available_categories = get_categories(raw_categories)
    for day_index, file in enumerate(get_log_files()):
        old_time = '00:00:00'
        activities_as_pie, activities_as_linear = extract_activity(file)





        single_session_schema = copy.deepcopy(raw_categories)
        for key, value in single_session_schema.items():
            single_session_schema[key] = 0
        single_session_schema['Idle'] = 0
        single_session_schema['Not defined'] = 0
        single_session_duration = 0
        single_session_straight = []
        a = []

        for index, line in read_file(file):
            task, old_time = get_task(line, old_time, available_categories)
            task = refine(settings['idle_time_in_seconds'], task)
            task = validate_task(task)

            # print(task['category'])
            single_session_schema[task['category']] += task['duration']
            single_session_duration += task['duration']
            single_session_straight.append(task['category'])
            # if task['category'] == 'Not defined': print(task, 'Not defined task')
            if task['layer_0_program_name'] not in a:
                print(task['layer_0_program_name'])
                a.append(task['layer_0_program_name'])

        # print(single_session_schema)


def new_main():
    for day_index, file in enumerate(get_log_files()):
        activities_as_pie: dict
        activities_as_linear: dict
        old_time: str
        activity_type: str
        activity_duration: int

        activities_as_pie = {}
        activities_as_linear = {}
        old_time = '00:00:00'


        for index, line in read_file(file):

            line = clean_line(line)
            new_time, activity_type = time_task_divider(line)
            activity_duration = elapsed_time(old_time, new_time)
            activity_type = extract_program(activity_type)
            old_time = new_time

            try:
                activities_as_pie[activity_type] += activity_duration
            except:
                activities_as_pie[activity_type] = activity_duration
            activities_as_linear[index] = {'activity_type': activity_type, 'activity_duration': activity_duration}

            # activities_as_pie, activities_as_linear = extract_activity(day)
            # print(activities_as_pie)
    print(activities_as_pie)




if __name__ == "__main__":
    new_main()





