# Скользящее среднее
def find_sma():
    with open('input.txt', 'r') as file_in:
        lines = file_in.readlines()

    arr = [int(item) for item in lines[1].split()]

    window_size = int(lines[2])
    result = []
    current_sum = sum(arr[0:window_size])
    result.append(str(current_sum / window_size))
    for i in range(0, len(arr) - window_size):
        current_sum -= arr[i]
        current_sum += arr[i + window_size]
        current_avg = current_sum / window_size
        result.append(str(current_avg)) 

    print(' '.join(result))


# Двойная индексация
def find_sum():
    with open('input.txt', 'r') as file_in:
        lines = file_in.readlines()

    average = int(lines[0])
    arr = [int(item) for item in lines[1].split()]
    sum = int(lines[2])

    out = False

    i = 0
    j = average - 1

    while i != j:
        cursum = arr[i] + arr[j]
        print(cursum)
        if cursum < sum:
            i += 1
        elif cursum > sum:
            j -= 1
        elif cursum == sum:
            print(arr[i], arr[j])
            out = True
            break

    if not out:
        print(None)


# Скользящее окно
def serf_win():
    with open('input.txt', 'r') as file_in:
        lines = file_in.readlines()
    result = []
    string = str(lines[0]).strip()
    unique_string = ''
    start_pos = 0
    i = 0
    while i < len(string):
        if string[i] not in unique_string:
            unique_string += string[i]
            i += 1
        else:
            result.append(i-start_pos)
            start_pos += unique_string.find(string[i]) + 1
            i = start_pos
            unique_string = ''

    result.append(i-start_pos)
    result.sort()
    max_string = result[-1]

    print(max_string)