ENDPOINT_CONFIGS = {
    "all-today": {
        "query": "SELECT * FROM viw_AllValues_Today WHERE pot_id = %s",
    },
    "sunlight-30days": {
        "query": "SELECT * FROM viw_SunlightPerDay_last30Days WHERE pot_id = %s",
    },
    "latest-value": {
        "query": "SELECT * FROM viw_LatestValuePerPot WHERE pot_id = %s"
    },
    "average-mtd": {
        "query": "SELECT * FROM viw_AverageMeasurements_MTD WHERE pot_id = %s"
    },
    "pots": {
        "query": "SELECT * FROM viw_PotsForUser WHERE user_mail = %s"
    },
    "plants": {
        "query": "SELECT * FROM viw_PlantsForUser WHERE user_mail = %s OR user_mail IS NULL"
    },
    "password_hash": {
        "query": "SELECT password_hash FROM user_profile WHERE user_mail = %s"
    },
    "insert-user": {
        "query": "INSERT INTO user_profile(user_mail, password_hash) VALUES(?,?)",
        "params": ["user_mail", "password_hash"]
    },
    "insert-plant": {
        "query": "INSERT INTO plant_profile (name, description, irrigation_cycle_days, target_temperature_celsius, target_sunlight_hours, target_air_humidity_percent, target_soil_moisture_percent) VALUES (?,?,?,?,?,?,?)",
        "params": ["name", "description", "irrigation_cycle_days", "target_temperature_celsius", "target_sunlight_hours", "target_air_humidity_percent", "target_soil_moisture_percent"]
    },
    "insert-user_pot_assignment": {
        "query": "INSERT INTO user_pot_assignment(pot_id, user_id) VALUES(?,?)",
        "params": ["pot_id", "user_id"]
    },
    "insert-plant_pot_assignment": {
        "query": "INSERT INTO plant_pot_assignment(pot_id, plant_id) VALUES(?,?)",
        "params": ["pot_id", "plant_id"]
    },
    "delete-plant_pot_assignment": {
        "query": "UPDATE plant_pot_assignment SET assigned_to = CURRENT_TIMESTAMP WHERE pot_id = ? AND plant_id = ?",
        "params": ["pot_id", "plant_id"]
    },
    "delete-user": {
        "query": "DELETE FROM user_profile WHERE user_mail = ?",
        "params": ["user_mail"]
    },
    "delete-plant": {
        "query": "DELETE FROM plant_profile WHERE plant_id = ?",
        "params": ["plant_id"]
    },
    "delete-pot": {
        "query": "DELETE FROM plant_pot WHERE pot_id = ?",
        "params": ["pot_id"]
    },
    "delete-user_pot_assignment": {
        "query": "DELETE FROM user_pot_assignment WHERE pot_id = ? AND user_id = ?",
        "params": ["pot_id", "user_id"]
    },
    "update-pot": {
        "query": "UPDATE plant_pot SET pot_name = ? WHERE pot_id = ?",
        "params": ["pot_name","pot_id"]
    },
    "update-user_mail": {
        "query": "UPDATE user_profile SET user_mail = ? WHERE user_mail = ?",
        "params": ["user_mail_new","user_mail"]
    },
    "update-user_password": {
        "query": "UPDATE user_profile SET password_hash = ? WHERE user_mail = ?",
        "params": ["password_hash","user_mail"]
    }
}


