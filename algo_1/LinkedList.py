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

    def __repr__(self):
        return str(self.head)


linkded_list = LinkedList(2)
linkded_list.append(5)
linkded_list.append(6)
linkded_list.append(5)
linkded_list.append(6)
linkded_list.append(5)
linkded_list.append(6)
linkded_list.append(5)
linkded_list.append(6)
print(linkded_list)
