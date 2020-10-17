# Comment 1,2
class KQueues: 
    def __init__(self, number_of_queues, array_length): 
        self.number_of_queues = number_of_queues 
        self.array_length = array_length 
        self.array = [-1] * array_length 
        self.front = [-1] * number_of_queues 
        self.rear = [-1] * number_of_queues 
        self.next_array = list(range(1, array_length)) 
        self.next_array.append(-1) 
        self.free = 0
  
    # To check whether the current queue_number is empty or not  
    def is_empty(self, queue_number): 
        return True if self.front[queue_number] == -1 else False
