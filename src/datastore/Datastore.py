import pickledb

class Datastore():

    db_name = "app_db"
    db_sessions = "sessions"
    db_users = "users"
    db = pickledb.load(db_name, False)

    def create_users_db(self):
        users = self.db.get(self.db_users)

        if users:
            print(f"Dictionary is not empty! {users}")
        else:
            print("Dictionary is empty!, create databases")
            self.db.dcreate(self.db_users)
            self.db.dump()
    
    def create_sessions_db(self):
        sessions = self.db.get(self.db_sessions)

        if sessions:
            print(f"Dictionary is not empty! {sessions}")
        else:
            print("Dictionary is empty!, create databases")
            self.db.dcreate(self.db_sessions)
            self.db.dump()
        
    def get_user_data_by_key(self, key:str):
        user_data = self.db.dget(self.db_sessions, key)

        return user_data

    def addKeyValue(self, key: str, value: str):
        values = (key, value)

        self.db.dadd(self.db_sessions, values)
        self.db.dump()

    def addUser(self, email: str, json_user: str):
        values = (email, json_user)

        self.db.dadd(self.db_users, values)
        self.db.dump()

    def check_if_exists(self, session_key:str):
        is_already_present = self.db.dexists(self.db_sessions, session_key)

        if(is_already_present):
            return True
        
        return False

    def check_if_user_exists(self, email:str):
        is_already_present = self.db.dexists(self.db_users, email)

        if(is_already_present):
            return True
        
        return False

    def updateSession(self, session_id):

        exists = self.check_if_exists(session_id)

        if exists:
            # Get values
            values = self.db.dget(self.db_sessions, session_id)
            # Set logged_in to False
            values['is_logged_in'] = False

            self.db.dump()

   

        
