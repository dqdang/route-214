# packs/models.py

from django.db import models

class BoosterPack(models.Model):
    tier = models.CharField(max_length=50)
    set_name = models.CharField(max_length=100)
    release_date = models.DateField()
    price_range = models.CharField(max_length=50, blank=True, null=True)
    price_charting_link = models.URLField(blank=True, null=True)

    # New fields for numerical price sorting
    low_price = models.IntegerField(blank=True, null=True, help_text="Lower end of the price range (for sorting)")
    high_price = models.IntegerField(blank=True, null=True, help_text="Higher end of the price range (for sorting)")

    def __str__(self):
        return self.set_name

    # Add a method to parse the price_range string
    def save(self, *args, **kwargs):
        self._parse_price_range()
        super().save(*args, **kwargs)

    def _parse_price_range(self):
        if self.price_range:
            # Remove '$', ',', and any non-numeric characters except '-' for ranges
            cleaned_price_range = self.price_range.replace('$', '').replace(',', '').strip()

            if '-' in cleaned_price_range:
                try:
                    low_str, high_str = cleaned_price_range.split('-', 1)
                    self.low_price = int(float(low_str.strip())) # Use float to handle potential decimals, then int
                    # Handle cases like "$100 - $200+" where high_str might end with '+'
                    self.high_price = int(float(high_str.strip().replace('+', '')))
                except (ValueError, IndexError):
                    self.low_price = None
                    self.high_price = None
            else: # Handle single price like "$150"
                try:
                    self.low_price = int(float(cleaned_price_range.strip().replace('+', '')))
                    self.high_price = self.low_price # If only one price, low and high are the same
                except ValueError:
                    self.low_price = None
                    self.high_price = None
        else:
            self.low_price = None
            self.high_price = None
