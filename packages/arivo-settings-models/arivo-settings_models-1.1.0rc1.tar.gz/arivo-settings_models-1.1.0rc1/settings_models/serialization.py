import re
from decimal import Decimal
from typing import Union, Type, Optional, Any, TypeVar

import orjson
import pydantic
from dateutil.tz import gettz

from settings_models.doc import Setting
from settings_models.settings.common import SettingsModel, Gates, Rates, ParkingAreas, Parksettings, CostGroups, \
    PrivacySettings, BillingSettings, Location, SupportSettings, RefsModel, GarageSettings, GarageName, Urls
from settings_models.settings.device_keys import PairingKey, Certificate, Otp
from settings_models.settings.enforcement import EnforcementSettings
from settings_models.settings.gate_control import GateMode, DayMode
from settings_models.settings.intercom import IntercomSettings

T = TypeVar('T')

_model_mapping = {
    "common/gates": Setting(Gates, "Has one entry for each gate of the garage."),
    "common/rates": Setting(Rates, "Defines the parking costs."),
    "common/parking_areas2": Setting(ParkingAreas, "Defines the physical areas of parking lot by specifying the gates."
                                                   "Also specifies settings for shortterm users."),
    "common/parksettings2": Setting(Parksettings, "Defines the terms and conditions for parking sessions of "
                                                  "registered users (not including registered shortterm users)."),
    "common/privacy_settings": Setting(PrivacySettings),
    "common/cost_groups": Setting(CostGroups, "Defines the costs for different activities."),
    "common/currency": Setting(str, "Defines the currency in which the parking costs are calculated."),
    "common/language": Setting(str, "Defines the language used for the user interface."),
    "common/timezone": Setting(str, "Defines the timezone in which the garage is located."),
    "common/garage_settings": Setting(GarageSettings),
    "common/location": Setting(Location),
    "common/billing": Setting(BillingSettings),
    "common/support": Setting(SupportSettings),
    "common/garage_name": Setting(GarageName),
    "common/urls": Setting(Urls),
    "gate_control/mode": Setting(GateMode, scoped=True),
    "gate_control/day_mode": Setting(DayMode),
    "enforcement/basic_settings": Setting(EnforcementSettings),
    "intercom/basic_settings": Setting(IntercomSettings),
    "device_keys/pairing": Setting(PairingKey),
    "device_keys/cert": Setting(Certificate),
    "device_keys/otp": Setting(Otp),
    "feature_flags": Setting(dict, "A dictionary of custom values that can be used to enable or "
                                   "disable features in various places."),
}


def _get_type(key: str, custom_type: Optional[Type[T]]) -> Type[T]:
    if custom_type:
        return custom_type
    if "/refs/" in key:
        return RefsModel
    if key not in _model_mapping:
        raise KeyError(f"No model for setting {key} found")
    return _model_mapping[key].settings_model


def _key_equal_id_in_value(k: str, v: Any, id_field: str = "id"):
    if k != getattr(v, id_field):
        raise ValueError(f"key must match field {id_field}")


def _special_validation(key: str, obj: Any):
    if key in ["common/rates", "common/parking_areas2", "common/parksettings2", "common/cost_groups"]:
        for k, v in obj.items():  # those settings are always dicts
            _key_equal_id_in_value(k, v)
    elif key == "common/gates":
        for k, v in obj.items():  # those settings are always dicts
            _key_equal_id_in_value(k, v, "gate")
    elif key == "common/timezone":
        if gettz(obj) is None:
            raise ValueError(f"timezone {obj} unknown")
    elif key == "common/language":
        if re.search(r"^[a-z]{2}(-[A-Z]{2})?$", obj) is None:
            raise ValueError(f"{obj} is no valid language code")
    elif key == "common/currency":
        if len(obj) != 3 or not obj.isalpha() or not obj.isupper():
            raise ValueError("Currency must be 3 uppercase letters")


def parse_setting_from_obj(key: str, value: Any, custom_type: Optional[Type[T]] = None) -> Any:
    """
    Parses setting into model of given key performing model validations and some additional validations for basic
    datatypes.
    :param key: Key of setting: is used to select the SettingsModel
    :param value: Settings value as json decoded object (or even already parsed object)
    :param custom_type: If your service uses only some field within a setting, a less specific model can be passed
    :return: Value parsed as correct model for given key
    :raises: ValueError if validation of setting fails
    """
    target_type = _get_type(key, custom_type)
    obj = pydantic.parse_obj_as(target_type, value)
    if not custom_type:
        _special_validation(key, obj)
    return obj


def parse_setting(key: str, value: Union[str, bytes], custom_type: Optional[Type[T]] = None) -> Any:
    """
    Parses setting into model of given key performing model validations and some additional validations for basic
    datatypes.
    :param key: Key of setting: is used to select the SettingsModel
    :param value: Settings value as string or byte array. Must be JSON decodable!
    :param custom_type: If your service uses only some field within a setting, a less specific model can be passed
    :return: Value parsed as correct model for given key
    :raises: ValueError if validation of setting fails
    """
    try:
        value_obj = orjson.loads(value)
    except orjson.JSONDecodeError as e:
        raise ValueError(f"{key} requires json decodable value") from e
    return parse_setting_from_obj(key, value_obj, custom_type)


def _default(obj):
    if isinstance(obj, SettingsModel):
        return obj.dict()
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError


_ESCAPE_ASCII = re.compile(r'([^ -~])')


def _replace(match):
    s = match.group(0)
    n = ord(s)
    if n < 0x10000:
        return '\\u%04x' % (n,)
    else:
        # surrogate pair
        n -= 0x10000
        s1 = 0xd800 | ((n >> 10) & 0x3ff)
        s2 = 0xdc00 | (n & 0x3ff)
        return '\\u%04x\\u%04x' % (s1, s2)


def _unicode_escape(data):
    return _ESCAPE_ASCII.sub(_replace, data)


def dump_setting(obj: Any) -> bytes:
    """
    Serializes settings model into bytearray for sending messages and writing into databases
    :param obj: setting as parsed model
    :return: byte array of serialized setting
    """
    return _unicode_escape(orjson.dumps(obj, default=_default).decode()).encode("ascii")
