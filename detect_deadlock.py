

def detect_deadlocks(processes, available, allocation, request):
   n = processes
   m = len(available)

   # Khoi tao Work va Finish
   work = list(available)
   finish = [False] * n

   for i in range(n):
      if all(allocation[i][j] == 0 for j in range(m)):
            finish[i] = True

   safe_sequence = []
   safe_sequences = []
   # Tim tien trinh co the thuc hien
   while True:
      found = False
      for i in range(n):
            if not finish[i]:
               if all(request[i][j] <= work[j] for j in range(m)):
                  for j in range(m):
                     work[j] += allocation[i][j]
                     finish[i] = True
                     safe_sequence.append(f"P{i}")
                  found = True
                  break
      if not found:
            break

   # Ket luan
   deadlocked_processes = [f"P{i}" for i in range(n) if not finish[i]]
   for i in range(len(safe_sequence)):
      if safe_sequence[i] not in safe_sequences:
         safe_sequences.append(safe_sequence[i])
   return deadlocked_processes, safe_sequences

