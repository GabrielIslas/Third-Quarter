worker = lambda name, age, sex, branches: (name, age, sex, branches)

firstBranch = lambda worker: worker[3][0]

beenCasaMatriz = lambda worker: "Casa Matriz" in worker[3]

forRetirement = lambda worker: 60 - worker[1] if worker[2] == "F" else 65-worker[1]

sameBranch = lambda worker1, worker2: any(x in worker1[3] for x in worker2[3])

canGoTogether = lambda worker1, worker2: worker1[2] != worker2[2] and forRetirement(worker1) > 10 and forRetirement(worker2) > 10 and (sameBranch(worker1, worker2) or beenCasaMatriz(worker1) or beenCasaMatriz(worker2))