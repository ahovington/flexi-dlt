class MissingEnvironemntVariable(Exception):
    def __str__(envar: str):
        return f"Missing environment variable {envar}"
