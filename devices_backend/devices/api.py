from ninja import NinjaAPI
from devices.models import Device, Location
from devices.schemas import (
    DeviceSchema,
    LocationSchema,
    DeviceCreateSchema,
    Error,
    DeviceLocationPatch,
)
from django.shortcuts import get_object_or_404

app = NinjaAPI()


@app.get("devices/", response=list[DeviceSchema])
def list_devices(request):
    devices = Device.objects.all()
    return devices


@app.get("devices/{slug}/", response=DeviceSchema)
def get_device(request, slug: str):
    device = get_object_or_404(Device, slug=slug)
    return device


@app.get("location/", response=list[LocationSchema])
def list_locations(request):
    return Location.objects.all()


@app.post("devices/", response={200: DeviceSchema, 404: Error})
def create_device(request, device: DeviceCreateSchema):
    if device.location_id:
        location = Location.objects.filter(id=device.location_id).exists()
        if not location:
            return 404, {"message": "Location not found"}
    device_obj = device.model_dump()
    device = Device.objects.create(**device_obj)
    return device


@app.post("devices/{device_slug}/set-location/", response=DeviceSchema)
def update_device_location(request, location: DeviceLocationPatch, device_slug):
    device = get_object_or_404(Device, slug=device_slug)
    if location.location_id:
        location = get_object_or_404(Location, id=location.location_id)
        device.location = location
    else:
        device.location = None
    device.save()
    return device