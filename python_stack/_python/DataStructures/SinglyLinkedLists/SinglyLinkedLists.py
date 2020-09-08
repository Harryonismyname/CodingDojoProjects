class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    def print_values(self):
        runner   = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self
    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        
        new_node = SLNode(val)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self

    def validator(self):
        if self.head == None:
            return False
        else:
            return True

    def remove_from_front(self):
        if self.validator():
            self.head = self.head.next
        return self
    
    def remove_from_end(self):
        if self.validator():
            runner = self.head
            while(runner.next != None):
                previous = runner
                runner = runner.next
            previous.next = None
        return self

    def remove_val(self, val):
        if self.validator():
            if self.head.value == val:
                self.remove_from_front()
            else:
                runner = self.head
                while(runner.value != val and runner.next != None):
                    previous = runner
                    runner = runner.next
                previous.next = runner.next
        return self

    def insert_at(self, val, n):
        if self.validator():
            if n == 0:
                self.add_to_front(val)
            else:
                new_node = SLNode(val)
                runner = self.head
                counter = 0
                while(runner.next != None and counter != n):
                    previous = runner
                    runner = runner.next
                    counter+=1
                if runner.next == None:
                    runner.next = new_node
                else:
                    previous.next = new_node
                    new_node.next = runner
        return self


class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None



sl = SList()

sl.add_to_back(10).add_to_back(9).add_to_front(10).add_to_front(9).add_to_front(8).add_to_front(7).add_to_front(6).add_to_front(5).add_to_front(4).add_to_front(3).add_to_front(2).add_to_front(1).add_to_front(0).add_to_back(8).add_to_back(7).add_to_back(6).add_to_back(5).add_to_back(4).add_to_back(3).add_to_back(2).add_to_back(1).add_to_back(0).insert_at(900, 400).print_values().remove_from_front().remove_from_end().remove_val(900)
print("\n"*3)
sl.print_values()

