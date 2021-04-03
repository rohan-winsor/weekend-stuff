"""
My interpretation of linkedlist in z2m 
"""


class LinkedList:
    def __init__(self, value):
        self.head = {
            "value": value,
            "next": None
        }
        self.tail = self.head

    def append(self, app_value, item=None):
        if item == None:
            item = self.head
        for key, value in item.items():
            if key == "next" and value == None:
                item["next"] = {
                    "value": app_value,
                    "next": None
                }
            elif key == "next" and value != None:
                self.append(app_value, item["next"])
        return None

    def prepend(self, value):
        self.head = { "value" : value , "next" : self.head}

    def __repr__(self):
        return str(self.head)


"""Better Linked List
"""


class Nodee:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList2:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        self.head = Nodee(value, self.head)

    def __repr__(self):
        linkedlist = self.head
        out = []
        while linkedlist.next is not None:
            out.append(str(linkedlist.data))
            linkedlist = linkedlist.next
        out.append(str(linkedlist.data))
        return " --> ".join(out)


linkded_list = LinkedList(2)
linkded_list.prepend(5)
linkded_list.prepend(6)
linkded_list.prepend(7)
linkded_list.prepend(8)
linkded_list.prepend(9)
linkded_list.prepend(10)
linkded_list.prepend(11)
linkded_list.prepend(12)
print(linkded_list)
