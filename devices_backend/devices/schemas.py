from ninja import ModelSchema
from devices.models import Device, Location


class LocationSchema(ModelSchema):
    class Meta:
        model = Location
        fields = ('id', 'name')

class DeviceSchema(ModelSchema):
    Location: LocationSchema | None = None
    class Meta:
        model = Device
        fields = ('id', 'name', 'slug', 'location')

    
