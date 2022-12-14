from db import db

def add_admin(user_name):
    sql = "UPDATE users SET admin=TRUE WHERE username = :user_name RETURNING id"
    result = db.session.execute(sql, {"user_name":user_name})
    db.session.commit()
    user = result.fetchone()
    if user:
        return True
    return False

def add_restaurant(restaurant_name, restaurant_address, description):
    try:
        sql = """
            INSERT INTO restaurants (name, description, visible, address) 
            VALUES (:restaurant_name, :description, TRUE, :restaurant_address)
            """
        db.session.execute(sql, {"restaurant_name":restaurant_name, "description":description,
        "restaurant_address":restaurant_address})
        db.session.commit()
    except:
        return False
    return True

def add_dish(restaurant_id, dish_name, price):
    try:
        sql = """
        INSERT INTO dishes (restaurant_id, dish_name, visible, price) 
        VALUES (:restaurant_id, :dish_name, TRUE, :price)
        """
        db.session.execute(sql, {"restaurant_id":restaurant_id, "dish_name":dish_name, "price":price})
        db.session.commit()
    except:
        return False
    return True

# Deletions are done by updating database column Visible to False.

def delete_reviews(review_id):
    sql = "UPDATE reviews SET visible=FALSE WHERE id = :review_id RETURNING id"
    result = db.session.execute(sql, {"review_id":review_id})
    db.session.commit()
    review = result.fetchone()
    if review:
        return True
    return False

def delete_restaurant(restaurant_id):
    sql = "UPDATE restaurants SET visible=FALSE WHERE id = :restaurant_id RETURNING id"
    result = db.session.execute(sql, {"restaurant_id":restaurant_id})
    db.session.commit()
    restaurant = result.fetchone()
    if restaurant:
        return True
    return False

def delete_dish(dish_id):
    sql = "UPDATE dishes SET visible=FALSE WHERE id = :dish_id RETURNING id"
    result = db.session.execute(sql, {"dish_id":dish_id})
    db.session.commit()
    dish = result.fetchone()
    if dish:
        return True
    return False

def delete_user(user_id):
    sql = "UPDATE users SET visible=FALSE WHERE id = :user_id RETURNING id"
    result = db.session.execute(sql, {"user_id":user_id})
    db.session.commit()
    user = result.fetchone()
    if user:
        return True
    return False

def get_user_id(username):
    sql = "SELECT id FROM users WHERE username = :username"
    result = db.session.execute(sql, {"username":username})
    user_id = result.fetchone()
    if user_id:
        return user_id[0]
    return 0
