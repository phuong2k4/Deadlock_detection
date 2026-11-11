

def detect_deadlock(processes, available, allocation, request):
   n = len(processes)
   m = len(available)

   # Khoi tao Work va Finish
   work = list(available)
   finish = [False] * n

   for i in range(n):
      if all(allocation[i][j] == 0 for j in range(m)):
            finish[i] = True

   safe_sequence = []

   # Tim tien trinh co the thuc hien
   while True:
      found = False
      for i in range(n):
            if not finish[i]:
               if all(request[i][j] <= work[j] for j in range(m)):
                  for j in range(m):
                     work[j] += allocation[i][j]
                     finish[i] = True
                     safe_sequence.append(processes[i])
                  found = True
                  break
      if not found:
            break

   # Ket luan
   deadlocked_processes = [processes[i] for i in range(n) if not finish[i]]
   return deadlocked_processes, safe_sequence



processes = ['P0', 'P1', 'P2']
available = [0,0,0]
allocation = [[0,1,0], [2,0,0], [3,0,3]]
request = [[0, 1, 0], [2, 0, 2], [0, 0, 0]]

deadlock_processes, safe_sequence = detect_deadlock(processes, available, allocation, request)
print(f"deadlock_processes = {deadlock_processes}")
print(f"Safe sequence = {safe_sequence}")