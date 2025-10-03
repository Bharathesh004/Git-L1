class Backend:
    def __init__(self):
        self.settings = {
            "database": "sqlite",
            "host": "localhost",
            "port": 5432,
            "user": "admin",
            "password": "admin"
        }
    
    def message(self, msg):
        print(f"[Backend] {msg}")

backend = Backend()
backend.message("Backend configured successfully.")

