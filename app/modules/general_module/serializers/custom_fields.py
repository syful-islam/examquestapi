# your_app/utils/fields.py
from rest_framework import serializers
from datetime import datetime
  
class ANDateField(serializers.DateField):
    """
    A custom DateField that supports configurable input/output formats.
    Default format is dd-MM-yyyy (e.g., 01-01-2023).
    """
    DEFAULT_FORMAT = '%Y-%m-%d'

    def __init__(self, input_format=None, output_format=None, **kwargs):
        self.input_format = input_format or self.DEFAULT_FORMAT
        self.output_format = output_format or self.DEFAULT_FORMAT
        # Set DRF's built-in format handling
        kwargs['format'] = self.output_format
        super().__init__(**kwargs)

    def to_internal_value(self, value):
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, self.input_format).date()
            except ValueError:
                self.fail('invalid', format=self.input_format)
        return super().to_internal_value(value)
    
class ANDateTimeField(serializers.DateTimeField):
    """
    A custom DateTimeField that supports configurable input/output formats.
    Default format is dd-MM-yyyy HH:mm (e.g., 01-01-2023 14:30).
    """
    DEFAULT_FORMAT = '%Y-%m-%d %H:%M'

    def __init__(self, output_format=None, **kwargs):
        self.output_format = output_format or self.DEFAULT_FORMAT
        # Set DRF's built-in format for serialization
        kwargs['format'] = self.output_format
        super().__init__(**kwargs)