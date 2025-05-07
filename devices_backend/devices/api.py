from ninja import NinjaAPI
from devices.models import Device, Location
from devices.schemas import DeviceSchema, LocationSchema

app = NinjaAPI()


@app.get("devices/", response=list[DeviceSchema])
def list_devices(request):
    devices = Device.objects.all()
    return devices

@app.get("location/", response=list[LocationSchema])
def list_locations(request):
    return Location.objects.all()