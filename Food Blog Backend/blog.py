import sqlite3
import sys

def get_pk_key(databasename, name, value):

    connect_sqlite3 = sqlite3.connect(databasename)
    cursor_sqlite3 = connect_sqlite3.cursor()

    if name == "meals":
        meal_name = ""
        # 1) breakfast  2) brunch  3) lunch  4) supper
        if int(value) == 1:
            meal_name = "breakfast"
        if int(value) == 2:
            meal_name = "brunch"
        if int(value) == 3:
            meal_name = "lunch"
        if int(value) == 4:
            meal_name = "supper"
        sqlite_insert_with_param = "SELECT meal_id FROM meals WHERE meal_name = '{}'".format(meal_name)

    if name == "measures":
        sqlite_insert_with_param = "SELECT measure_id FROM measures WHERE measure_name = '{}'".format(value)

    if name == "ingredients":
        sqlite_insert_with_param = "SELECT ingredient_id FROM ingredients WHERE ingredient_name like '%{}%'".format(value)

    if name == "recipes":
        sqlite_insert_with_param = "SELECT recipe_id FROM recipes WHERE recipe_name = '{}'".format(value)

    cursor_sqlite3.execute(sqlite_insert_with_param)

    results = cursor_sqlite3.fetchone()

    if connect_sqlite3:
        connect_sqlite3.close()

    # meals_id doesn't exists
    if results is None:
        return 0

    # meals_id
    return results[0]

def validate_parameters(measure, ingredient, databasename):

    # not pass
    if not get_pk_key(databasename, "measures", measure):
        print("The measure is not conclusive!")
        return 0

    # not pass
    if not get_pk_key(databasename, "ingredients", ingredient):
        print("The ingredient is not conclusive!")
        return 0

    # pass
    return 1

def insert_value(name, databasename, value1, value2, meals):

    try:
        connect = sqlite3.connect(databasename)
        connect.execute("PRAGMA foreign_keys = 1")
        cursor = connect.cursor()

        sqlite_insert_with_param = ""

        if name == "measures":
            sqlite_insert_with_param = "INSERT INTO measures (measure_name) VALUES ('{}');".format(value1)

        if name == "ingredients":
            sqlite_insert_with_param = "INSERT INTO ingredients (ingredient_name) VALUES ('{}');".format(value1)

        if name == "meals":
            sqlite_insert_with_param = "INSERT INTO meals (meal_name) VALUES ('{}');".format(value1)

        if name == "recipes":
            sqlite_insert_with_param = "INSERT INTO recipes (recipe_name, recipe_description) VALUES ('{}', '{}');"\
                                                                                                .format(value1, value2)

        result = cursor.execute(sqlite_insert_with_param).lastrowid
        connect.commit()

        if name == "recipes":

            for meal in meals:

                # serve
                meal_id = get_pk_key(databasename, "meals", meal)
                sqlite_insert_with_param = "INSERT INTO serve (meal_id, recipe_id) VALUES ({}, {});"\
                                                                                            .format(meal_id, result)
                cursor.execute(sqlite_insert_with_param)
                connect.commit()

            while True:

                input_value = input("Input quantity of ingredient <press enter to stop>:").split()

                if input_value == "" or len(input_value) == 0:
                    break

                if len(input_value) == 2:
                    quantity    = input_value[0]
                    measure     = ""
                    ingredient  = input_value[1]

                if len(input_value) == 3:
                    quantity    = input_value[0]
                    measure     = input_value[1]
                    ingredient  = input_value[2]

                if validate_parameters(measure, ingredient, databasename) == 0:
                    continue

                measure_id = get_pk_key(databasename, "measures", measure)
                ingredients_id = get_pk_key(databasename, "ingredients", ingredient)

                #quantity
                sqlite_insert_with_param = "INSERT INTO quantity (quantity, recipe_id, measure_id, ingredient_id) " \
                                           "VALUES ({}, {}, {}, {});".format(quantity, result, measure_id, ingredients_id)
                print(" ### quantity " + sqlite_insert_with_param)
                cursor.execute(sqlite_insert_with_param)
                connect.commit()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if connect:
            connect.close()


def populate_db(data, databasename):

    for name, keys in data.items():
        for value in keys:
            insert_value(name, databasename, value, "", "")


def create_db(arg):

    try:
        connect = sqlite3.connect(arg)
        connect.execute("PRAGMA foreign_keys = 1")
        cursor = connect.cursor()
        cursor.execute("DROP TABLE IF EXISTS measures;")
        cursor.execute('''CREATE TABLE IF NOT EXISTS measures (measure_id integer not null primary key autoincrement, 
                                                            measure_name text unique);''')

        cursor.execute("DROP TABLE IF EXISTS ingredients;")
        cursor.execute('''CREATE TABLE IF NOT EXISTS ingredients (ingredient_id integer not null primary key autoincrement, 
                                                            ingredient_name text not null unique);''')

        cursor.execute("DROP TABLE IF EXISTS meals;")
        cursor.execute('''CREATE TABLE IF NOT EXISTS meals (meal_id integer not null primary key autoincrement, 
                                                            meal_name text not null unique);''')

        cursor.execute("DROP TABLE IF EXISTS recipes;")
        cursor.execute('''CREATE TABLE IF NOT EXISTS recipes (recipe_id integer not null primary key autoincrement, 
                                                            recipe_name text not null,
                                                            recipe_description text);''')

        cursor.execute("DROP TABLE IF EXISTS serve;")
        cursor.execute('''CREATE TABLE IF NOT EXISTS serve (serve_id integer not null primary key autoincrement, 
                                                            meal_id integer not null,
                                                            recipe_id integer not null,
                                                            FOREIGN KEY(meal_id) REFERENCES meals(meal_id),
                                                            FOREIGN KEY(recipe_id) REFERENCES recipes(recipe_id));''')

        cursor.execute("DROP TABLE IF EXISTS quantity ;")
        cursor.execute('''CREATE TABLE IF NOT EXISTS quantity (quantity_id integer not null primary key autoincrement, 
                                                            quantity integer not null,
                                                            recipe_id integer not null,
                                                            measure_id integer not null,
                                                            ingredient_id integer not null,
                                                            FOREIGN KEY(recipe_id) REFERENCES recipes(recipe_id),
                                                            FOREIGN KEY(measure_id) REFERENCES measures(measure_id),
                                                            FOREIGN KEY(ingredient_id) REFERENCES ingredients(ingredient_id));''')
        connect.commit()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if connect:
            connect.close()


def check_recipes(database, ingredients, meals):
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    """

    connect = sqlite3.connect(database)
    cursor = connect.cursor()

    ingredients_sql = ""
    for value in ingredients:
        ingredients_sql += "'" + value + "',"

    if ingredients_sql != "":
        ingredients_sql += "''"

    meals_sql = ""
    for value in meals:
        meals_sql += "'" + value + "',"

    if meals_sql != "":
        meals_sql += "''"


    # ----- first sql

    sql_with_param = "SELECT recipes.recipe_id, recipes.recipe_name FROM recipes WHERE recipes.recipe_id IN ( \
                                                                SELECT serve.recipe_id FROM serve, meals WHERE \
                                                    serve.meal_id = meals.meal_id AND meals.meal_name IN ({}));" \
                                                                                                    .format(meals_sql)
    cursor.execute(sql_with_param)

    recipes_list = []
    rows = cursor.fetchall()
    for row in rows:
        recipes_list.append(row)


    # ----- second sql

    sql_with_param = "SELECT quantity.recipe_id,ingredients.ingredient_name FROM quantity, ingredients \
                                WHERE quantity.ingredient_id = ingredients.ingredient_id \
                                AND ingredients.ingredient_name in ({});" \
                                .format(ingredients_sql)
    cursor.execute(sql_with_param)

    ingredients_list = []
    rows = cursor.fetchall()
    for row in rows:
        ingredients_list.append(row)

    lenght = len(ingredients)

    recipes = []
    for x, y in recipes_list:
        result = [i for i,j in ingredients_list if i==x ]

        if len(result) == lenght:
            recipes.append(y)

    if len(recipes) > 0:
        print("Recipes selected for you: " + " and ".join(recipes))
    else:
        print("There are no such recipes in the database.")

    connect.close()


if __name__ == "__main__":

    data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
            "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
            "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}

    args = sys.argv

    if len(args) == 4:

        # database name
        database = str(args[1])

        # --ingredients
        if args[2].split("=")[0] == "--ingredients":
            ingredients = args[2].split("=")[1].split(",")
            #print("ingredients : " + str(ingredients))

        # --meals
        if args[3].split("=")[0] == "--meals":
            meals = args[3].split("=")[1].split(",")
            #print("meals : " + str(meals))

        check_recipes(database, ingredients, meals)

    elif len(args) == 2:

        database = str(args[1])
        create_db(database)

        populate_db(data, database)

        print("Pass the empty recipe name to exit.")

        while True:

            print("Recipe name:")
            name = input()
            if name == "":
                break

            print("Recipe description:")
            description = input()
            if description == "":
                break

            print("1) breakfast  2) brunch  3) lunch  4) supper")
            print("When the dish can be served:")
            serve = input().split()

            insert_value("recipes", database, name, description, serve)

