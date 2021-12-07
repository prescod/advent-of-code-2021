def binary_search_lowest(start:int, end:int, callback):
    mid = 0
    step = 0
    lowest_seen = 9999999999999

    while (start <= end):
        step = step+1
        mid = (start + end) // 2
        latest_val = callback(mid)

        if latest_val < lowest_seen:
            lowest_seen = latest_val

        if callback(mid-1) < latest_val:
            end = mid - 1
        else:
            start = mid + 1
    return lowest_seen
