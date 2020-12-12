from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return f'{self.name}'


class Establishment(models.Model):
    name = models.CharField(max_length=50, blank=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.city}'


class Place(models.Model):
    VACANT = 'vacant'
    OCCUPIED = 'occupied'
    TIMEOUT = 'timeout'
    UNKNOWN = 'unknown'

    STATUS_TYPES = (
        (VACANT, 'Vacant'),
        (OCCUPIED, 'Occupied'),
        (TIMEOUT, 'Timeout'),
        (UNKNOWN, 'Unknown'),
    )

    status = models.CharField(max_length=8, choices=STATUS_TYPES, default=UNKNOWN)
    room_number = models.CharField(max_length=5, blank=False)
    floor_number = models.CharField(max_length=2, blank=False)
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.status} - {self.establishment}'
