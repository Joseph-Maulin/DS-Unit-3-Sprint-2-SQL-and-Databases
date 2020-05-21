import sqlite3

connection = sqlite3.connect("rpg_db.sqlite3")
# connection.row_factory = sqlite3.Row

cursor = connection.cursor()


cursor.execute("""
                SELECT COUNT(*) as Character_Count
                FROM charactercreator_character;
            """)


print(f"Character Count: {cursor.fetchall()[0][0]}")


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


print(f"Character Count Per Class: {cursor.fetchall()[0]}")


connection.close()
