import sqlite3

connection = sqlite3.connect("rpg_db.sqlite3")
connection.row_factory = sqlite3.Row

cursor = connection.cursor()


cursor.execute("""
                SELECT COUNT(*) as Character_Count
                FROM charactercreator_character;
            """)



print(dict(cursor.fetchall()[0]))


cursor.execute("""
                SELECT(
                SELECT COUNT(charactercreator_cleric.character_ptr_id)
                	FROM charactercreator_cleric)
                	as Cleric_Count,
                (SELECT COUNT(charactercreator_mage.character_ptr_id)
                	FROM charactercreator_mage)
                	as Mage_Count,
                (SELECT COUNT(charactercreator_fighter.character_ptr_id)
                	FROM charactercreator_fighter)
                	as Fighter_Count,
                (SELECT COUNT(charactercreator_thief.character_ptr_id)
                	FROM charactercreator_thief)
                	as Thief_Count;
            """)


print(dict(cursor.fetchall()[0]))


cursor.execute("""
                SELECT COUNT(item_id) AS item_count
                FROM armory_item;
              """)

print(dict(cursor.fetchall()[0]))


cursor.execute("""
                SELECT COUNT(item_ptr_id) AS weapon_count
                FROM armory_weapon;
                """)

print(dict(cursor.fetchall()[0]))

cursor.execute("""
                SELECT COUNT(item_id) - COUNT(item_ptr_id) AS not_weapons FROM
                armory_item
                LEFT JOIN armory_weapon
                ON armory_weapon.item_ptr_id = armory_item.item_id;
                """)

print(dict(cursor.fetchall()[0]))

cursor.execute("""
                SELECT charactercreator_character_inventory.character_id, COUNT(charactercreator_character_inventory.item_id) AS item_count FROM charactercreator_character_inventory
                JOIN armory_item
                ON charactercreator_character_inventory.item_id = armory_item.item_id
                GROUP BY character_id
                LIMIT 20;
                """)
print(dict(cursor.fetchall()[0:20]))

cursor.execute("""
                SELECT charactercreator_character_inventory.character_id, COUNT(charactercreator_character_inventory.item_id) AS item_count FROM charactercreator_character_inventory
                JOIN armory_weapon
                ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
                GROUP BY character_id
                LIMIT 20;
                """)
print(dict(cursor.fetchall()[0:20]))

cursor.execute("""
                SELECT AVG(count) AS inventory_avg_items
                FROM
                (SELECT COUNT(charactercreator_character_inventory.item_id) AS count
                FROM charactercreator_character_inventory
                GROUP BY charactercreator_character_inventory.character_id)
                """)

print(dict(cursor.fetchall()[0]))

connection.close()
