#221RDB322 Deņiss Dmitrijevs

# python3
class HashArray:
    #telephone numbers acts as hash keys, no need to handle collisions
    __hash_multiplier = 1
    __hash_term = 1

    array: list
    size: int

    def __init__(self, size):
        self.size = size
        self.array = [None] * size
    
    def get_hash(self, key):
        return (key * self.__hash_multiplier + self.__hash_term)  % self.size
    
    def get_obj(self, key):
        return self.array[self.get_hash(key)]

    #overwrites existing value
    def add_obj(self, key, value):
        self.array[self.get_hash(key)] = value

    def del_obj(self, key):
        hash = self.get_hash(key)
        if (self.array[hash] is not None):
            self.array[hash] = None

            

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = HashArray(10000);
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts.add_obj(key = cur_query.number, value = cur_query.name)
            # if we already have contact with such number,
            # we should rewrite contact's name
            # for contact in contacts:
            #     if contact.number == cur_query.number:
            #         contact.name = cur_query.name
            #         break
            # else: # otherwise, just add it
            #     contacts.append(cur_query)
        elif cur_query.type == 'del':
            contacts.del_obj(key = cur_query.number
            # for j in range(len(contacts)):
            #     if contacts[j].number == cur_query.number:
            #         contacts.pop(j)
            #         break
        else:
            response = 'not found'
            contact_name = contacts.get_obj(cur_query.number)
            # for contact in contacts:
            #     if contact.number == cur_query.number:
            #         response = contact.name
            #         break
            if contact_name is not None:
                response = contact_name
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

