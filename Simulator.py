

# make a decrator that adds the process name to the process queue
class Process:
    def __init__(self, PID, at, bt, priority):
        self.PID = PID
        self.at = at
        self.bt = bt
        self.priority = priority

# reads from trace file and creates a single process object
def read_file(i):
    f = open("trace.txt", 'r')
    lines = list(f.readlines())
    num_processes = len(lines)
    process_queue = []
    for i, ele in enumerate(num_processes):
        txt = lines[i].strip()
        new = txt.split()
        process_obj = Process(int(new[0]), int(new[1]), int(new[2]), int(new[3]), None, None)
        process_queue.append(process_obj)
    return process_queue

