from collections import deque

queue = deque()

queue.append(("JOB001", 10))
queue.append(("JOB002", 5))
queue.append(("JOB003", 20))

while queue:
    job_id, pages = queue.popleft()
    print(f"Printing {job_id} ({pages} pages)")