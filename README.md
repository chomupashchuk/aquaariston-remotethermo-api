# Aqua Ariston NET remotethermo API
Thin integration is a side project which works only with 1 zone climate configured. It logs in to Ariston website (https://www.ariston-net.remotethermo.com) and fetches/sets data on that site.
You are free to modify and distribute it. It is distributed 'as is' with no liability for possible damage.
See also https://pypi.org/project/aquaaristonremotethermo/ .
This API is for Aqua Ariston NET, for Ariston NET refer to https://github.com/chomupashchuk/ariston-remotethermo-api .


## Donations
If you like this app, please consider donating some sum to your local charity organizations or global organization like Red Cross. I don't mind receiving donations myself (you may conact me for more details if you want to), but please consider charity at first.

## API and Home Assistant
API was created in order to be used by Home Assistant. Example of API use for Home Assistant can be found: https://github.com/chomupashchuk/ariston-aqua-remotethermo-home-assistant

## API slow nature
API connect to the website, which then connect via gateway to the boiler. The bus has problem handling high bandwidth and thus requests are sent after some specific periods of time. Periods were selected based on tests where not much of interfence was seen when using Ariston Net application or Google Home application or using https://www.ariston-net.remotethermo.com. Still interfences occaionally take place. It is normal to occasionally get connection errors due to devices chain involved.


## AquaAristonHandler was tested works with:
  - Ariston Velis (NOTE THAT THERE ARE 2 TYPES OF VELIS. FOR VELIS WITH NUMBER OF SHOWERS IN APPLICATION USE TYPE `velis`, WHILE FOR VELIS WITH TEMPERATURE SETTING IN APPLICATION USE TYPE `lydos`).
  - Ariston Lydos
  - Ariston Lydos Hybrid

## Check which version to use
Your boiler works with `Aqua Ariston NET` and not `Ariston NET`, then potentially it could work.

## API use
### API import
Install package:
```
pip install aquaaristonremotethermo
```
Import class `AquaAristonHandler`:
```
from aquaaristonremotethermo.aristonaqua import AquaAristonHandler
```

### API dependencies
  - `requests` - used for HTTPS requests towards https://www.ariston-net.remotethermo.com.
  

### AquaAristonHandler start communication
```
from aquaaristonremotethermo.aristonaqua import AquaAristonHandler

ApiInstanceAqua = AquaAristonHandler(
            username='username',
            password='password'
        )

ApiInstanceAqua.start()
```
See `help(AquaAristonHandler)` on how to properly initiate API.


### AquaAristonHandler stop communication
```
ApiInstanceAqua.stop()
```

### API properties
See `help(AquaAristonHandler)`.


### AquaAristonHandler change of data on remote server
```
ApiInstanceAqua.set_http_data(parameter1=value1,parameter2=value2,...)
```
Method sets values for specific parameter names (see property `supported_sensors_set_values` from `help(AquaAristonHandler)`) on the remote server.

#### AquaAristonHandler change of data example
```
ApiInstanceAqua.set_http_data(mode="manual")
```
