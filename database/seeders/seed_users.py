import hashlib

def _hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def run(conn):
    conn.execute(
        "INSERT OR IGNORE INTO users (id, name, email, password) VALUES (1, ?, ?, ?)",
        ('Root User', 'root@example.com', _hash('rootpass'))
    )
    conn.execute("INSERT OR IGNORE INTO users (name, email, password) VALUES (?, ?, ?)", ('Souvik', 'svk@example.com', _hash('souvik123')))
    conn.execute("INSERT OR IGNORE INTO users (name, email, password) VALUES (?, ?, ?)", ('Sourav', 'srv@example.com', _hash('sourav123')))
    conn.execute("INSERT OR IGNORE INTO users (name, email, password) VALUES (?, ?, ?)", ('Prasun', 'prsb@example.com', _hash('prasun123')))
    conn.execute("INSERT OR IGNORE INTO users (name, email, password) VALUES (?, ?, ?)", ('Rupankar', 'rpk@example.com', _hash('rupankar123')))
    conn.execute("INSERT OR IGNORE INTO users (name, email, password) VALUES (?, ?, ?)", ('Samya', 'sdk@example.com', _hash('samya123')))
    conn.commit()
