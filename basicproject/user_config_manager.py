test_settings = {
    "theme":"dark",
    "language":"korean",
    "notifications":"on"
}

def add_setting(as1,as2):
    #add a new setting to the dictionary
    key, value = as2 # get key and value from the tuple
    key = key.lower()
    value = value.lower()
    if key in as1:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    as1[key] = value # add the new key and value
    return f"Setting '{key}' added with value '{value}' successfully!" 

print(add_setting(test_settings,("volume","high"))) # test adding a new setting

def update_setting(as1,as2):
    #update an existing setting
    key, value = as2
    key = key.lower()
    value = value.lower()
    if key in as1:
        as1[key] = value #means replace old value with new one
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(as1,as2):
    #delete a setting from the dictionary
    key = as2
    key = key.lower()
    if key in as1:
        del as1[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(as1):
    #shows all the current settings
    if not as1:
        return "No settings available."
    result = "Current User Settings:\n"

    for key, value in as1.items():
        result += f"{key.capitalize()}: {value}\n" # add each setting to the result

    return result
print(view_settings(test_settings)) # view all settings
print(update_setting(test_settings, ("theme", "light"))) # update theme
print(update_setting(test_settings, ("volume", "high"))) # update volume

print(delete_setting(test_settings, "language")) # delete language
print(delete_setting(test_settings, "wifi")) # try to delete wifi