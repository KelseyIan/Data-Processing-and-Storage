class InMemoryDB:
    def __init__(self):
        self.Map = {}
        self.active_transaction = False
        self.temp_storage = None

    #used normal dictionary, could use defaultdic to prevent extra checks to match a key
    def begin_transaction(self):
        if self.active_transaction:
            raise Exception("Transaction already in process.")
        self.temp_storage = {}  #empty map for transaction data
        self.active_transaction = True  #set bool to true

    def put(self, key, value):  #string , value pair
        if not self.active_transaction:
            raise Exception("Can not put, no active transaction.")
        self.temp_storage[key] = value  #stores, always active map for this return

    def get(self, key):
        if self.active_transaction and key in self.temp_storage:
            return self.temp_storage[key]
        return self.Map.get(key)    #retuns null if not valid independent of active

    def commit(self):
        if not self.active_transaction:
            raise Exception("Can not commit, no active transaction.")
        for key, value in self.temp_storage.items():    #iterates through items
            self.Map[key] = value   #updates or adds value for the specific key
        self.active_transaction = False
        self.temp_storage = None

    def rollback(self):
        if not self.active_transaction:
            raise Exception("Can not rollback, no active transaction.")
        self.active_transaction = False
        self.temp_storage = None
