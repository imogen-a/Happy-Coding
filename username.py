# Usernames Prohibited to use -
reserved_usernames = {
    "admin", "administrator", "root", "support", "moderator", "sysadmin", "hostmaster", "postmaster", "api", "www", "ftp", "dns", "http", "mailto", "ssl", "localhost", "abuse", "security", "spam", "spamtrap", "mailer-daemon", "snapchat", "instagram"
}

# converts to lowercase to catch the prohibited names -
def is_valid_username(username):
    cleaned_username = username.strip().lower()

    if cleaned_username in reserved_usernames:
        return False
    return True

