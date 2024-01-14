class SettingsError(Exception):
    def __init__(self, setting_name, value, acceptable_values_string):
        self._message = f"Invalid {setting_name}, {value} is not an acceptable value for {setting_name}. {setting_name} must be {acceptable_values_string}"

    @property
    def message(self):
        return self._message