# app/config_parser.py
import configparser

def process_config_file(config_content):
    """
    Parse config files and grade based on expected configurations.
    """
    config = configparser.ConfigParser()
    config.read_string(config_content.decode("utf-8"))

    feedback = ""
    grade = 0

    # Example grading logic (check for a specific config section)
    if "server" in config and config["server"].get("port") == "8080":
        feedback = "Correct server configuration."
        grade = 100
    else:
        feedback = "Incorrect server configuration. Expected port 8080."
        grade = 50
    
    return feedback, grade
