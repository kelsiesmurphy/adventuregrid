from db.run_sql import run_sql
from models.users_experiences import Users_Experiences
import repositories.user_repository as user_repository
import repositories.experience_repository as experience_repository


# SAVE (Create in CRUD)
def save(users_experiences):
    sql = "INSERT INTO users_experiences (user_id, experience_id, review) VALUES (%s, %s, %s) RETURNING *"
    values = [users_experiences.user_id, users_experiences.experience_id, users_experiences.review]
    result = run_sql(sql, values)[0]
    result_id = result['id']
    users_experiences.id = result_id
    return users_experiences


# SELECT ALL
def select_all():
    selected_users_experiences = []
    sql = "SELECT * FROM users_experiences"
    results = run_sql(sql)
    for row in results:
        new_users_experiences = Users_Experiences(row["user_id"], row["experience_id"], row["review"], row["id"])
        selected_users_experiences.append(new_users_experiences)
    return selected_users_experiences


# DELETE ALL
def delete_all():
    sql = "DELETE FROM users_experiences"
    run_sql(sql)