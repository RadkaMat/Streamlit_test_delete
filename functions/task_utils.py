from datetime import datetime
import re
from collections import defaultdict

REGEX_TASKS = r"^(.*?) (\d{2}\. \d{2}\. \d{4}) (\d{2}:\d{2})$"


def parse_tasks(to_do_list: list[str]) -> list[tuple[str, datetime]]:
    """ Parse tasks from to-do list and return task details with datetime. """
    tasks = []
    for line in to_do_list:
        match = re.match(REGEX_TASKS, line.strip())
        if match:
            task = match.group(1)
            date_str = match.group(2)
            time_str = match.group(3)
            task_datetime = datetime.strptime(f"{date_str} {time_str}", "%d. %m. %Y %H:%M")
            tasks.append((task, task_datetime))
        else:
            print(f"Could not parse line: {line}")
    tasks.sort(key=lambda x: x[1], reverse=True)
    return tasks


def group_tasks_by_date(tasks: list[tuple[str, datetime]]) -> defaultdict:
    """ Group tasks by their date. """
    grouped_tasks = defaultdict(list)

    for task, dt in tasks:
        date_only = dt.date()
        grouped_tasks[date_only].append((task, dt))
    return grouped_tasks
