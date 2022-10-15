import datetime


def total_today():
    count = 0

    now = datetime.datetime.now()
    now = now.strftime("%d %m %Y")
    day, month, year = now.split()
    for _ in log:
        _ = int(_)
        _ = datetime.datetime.fromtimestamp(_)
        _ = _.strftime("%d %m %Y")
        _day, _month, _year = _.split()

        rules = [ 
            day   == _day, 
            month == _month, 
            year  == _year 
        ]

        if all(rules):
            count += 1

    return count


def most_recent():
    if not log:
        return -1
    length = len(log)
    recent = log[length - 1]
    recent = int(recent)
    # last entry in log converted to <datetime>
    recent = datetime.datetime.fromtimestamp(recent)
    now    = datetime.datetime.now()
    # calculates time between current time and last entry
    # in log
    delta  = now - recent

    return delta.total_seconds()


def relapse():
    user_input = input("Have you relapsed [y/n]: ")

    if user_input[0] == 'y':
        cur_time   = datetime.datetime.now()
        unix       = datetime.datetime.timestamp(cur_time)
        unix       = int(unix)

        log.append(str(unix))
        write_to_file(unix)
    

def write_to_file(message):
    with open(file_path, "a") as file:
        file.write(f"{message}\n")


def retrieve_from_file():
    try:
        # read unix timestamps from file
        with open(file_path, "r") as file:
            file_contents = [timestamp.replace('\n', '') for
                timestamp in file if timestamp != ""]

    # create file incase it is not found
    except FileNotFoundError:
        with open(file_path, "w") as file:
            file.write("")
        file_contents = []

    return file_contents
        

if __name__ == "__main__":
    file_path = "log.txt"
    log       = retrieve_from_file()

    relapse()

    print(f"Seconds since last relapse: {int(most_recent())}")
    print(f"Times relapsed today      : {total_today()}")

