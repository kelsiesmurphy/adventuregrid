from db.run_sql import run_sql
from models.experience import Experience


# SAVE (Create in CRUD)
def save(experience):
    sql = "INSERT INTO experiences (title, description, location, image, price, is_featured) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [experience.title, experience.description, experience.location, experience.image, experience.price, experience.is_featured]
    result = run_sql(sql, values)[0]
    result_id = result['id']
    experience.id = result_id
    return experience


# SELECT BY ID (Read in CRUD)
def select_by_id(id):
    selected_experience = None
    sql = "SELECT * FROM experiences WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        selected_experience = Experience(result["title"], result["description"], result["location"], result["image"], result["price"], result["is_featured"])
    return selected_experience


# SELECT ALL
def select_all():
    selected_experiences = []
    sql = "SELECT * FROM experiences"
    results = run_sql(sql)
    for row in results:
        new_experience = Experience(row["title"], row["description"], row["location"], row["image"], row["price"], row["is_featured"], row["id"])
        selected_experiences.append(new_experience)
    return selected_experiences


# UPDATE (Update in CRUD)
def update(experience):    
    sql = "UPDATE experiences SET (title, description, location, image, price, is_featured) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [experience.title, experience.description, experience.location, experience.image, experience.price, experience.is_featured, experience.id]
    run_sql(sql, values)


# DELETE BY ID (Delete in CRUD)
def delete_by_id(id):
    sql = "DELETE FROM experiences WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# DELETE ALL
def delete_all():
    sql = "DELETE FROM experiences"
    run_sql(sql)