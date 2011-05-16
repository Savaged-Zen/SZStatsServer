from szstats.database.schema.devices import Device
from szstats.resources import Root
from pyramid.view import view_config


@view_config(context=Root, name="submit", renderer="string")
def submit(request):
    device_hash = request.params.get('device_hash', None)
    device_name = request.params.get('device_name', None)
    device_version = request.params.get('device_version', None)
	kernel_version = request.params.get('kernel_version', None)
    device_country = request.params.get('device_country', None)
    device_carrier_id = request.params.get('device_carrier_id', None)

    kwargs = {
        'hash': device_hash,
        'name': device_name,
        'version': device_version,
		'kernel_version': kernel_version,
        'country': device_country,
        'carrier_id': device_carrier_id,
    }

    if device_hash == "":
        return "Incomplete Data"

    for v in kwargs.itervalues():
        if v == None:
            return "Incomplete Data"

    # Create device record.
    Device.add(**kwargs)

    return "Thanks!"
