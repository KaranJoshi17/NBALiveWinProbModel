# this is for seconds remaining

def timeToSeconds(clock: str) -> int:

    arr = list(clock)

    for i in range(len(arr)):

        if arr[i] == "M":
            minutes = int(arr[i-2] + arr[i-1])
            seconds = int(arr[i+1] + arr[i+2])

            minutesToSeconds = minutes * 60
            finalTime = seconds + minutesToSeconds

    return finalTime
        


