from db.run_sql import run_sql
from models.user import User
from models.experience import Experience


# SAVE (Create in CRUD)
def save(user):
    sql = "INSERT INTO users (name, email, username, image) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [user.name, user.email, user.username, user.image]
    result = run_sql(sql, values)[0]
    result_id = result['id']
    user.id = result_id
    return user


# SELECT BY ID (Read in CRUD)
def select_by_id(id):
    selected_user = None
    sql = "SELECT * FROM users WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        selected_user = User(result["name"], result["email"], result["username"], result["image"])
    return selected_user


# SELECT ALL
def select_all():
    selected_users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        new_user = User(row["name"], row["email"], row["username"], row["image"], row["id"])
        selected_users.append(new_user)
    return selected_users


# UPDATE (Update in CRUD)
def update(user):    
    sql = "UPDATE users SET (name, email, username, image) = (%s, %s, %s, %s) WHERE id = %s"
    values = [user.name, user.email, user.username, user.image, user.id]
    run_sql(sql, values)


# DELETE BY ID (Delete in CRUD)
def delete_by_id(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# DELETE ALL
def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)