

class Queue():
    def calculate_queue(self, queue):
        size = self.check_queue_size(queue)
        return size

    def check_queue_size(self, queue):
        if len(queue) == 1:
            return 1
        else:
            return 1 + self.check_queue_size(queue[1:])


obj = Queue()
print(obj.calculate_queue([0]*10))

