import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="AuthTokenRefreshCreateResponse200")


@attr.s(auto_attribs=True)
class AuthTokenRefreshCreateResponse200(OSIDBModel):
    """ """

    access: str
    refresh: str
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access = self.access
        refresh = self.refresh
        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env
        revision = self.revision
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if access is not UNSET:
            field_dict["access"] = access
        if refresh is not UNSET:
            field_dict["refresh"] = refresh
        if dt is not UNSET:
            field_dict["dt"] = dt
        if env is not UNSET:
            field_dict["env"] = env
        if revision is not UNSET:
            field_dict["revision"] = revision
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access = d.pop("access", UNSET)

        refresh = d.pop("refresh", UNSET)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        auth_token_refresh_create_response_200 = cls(
            access=access,
            refresh=refresh,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        auth_token_refresh_create_response_200.additional_properties = d
        return auth_token_refresh_create_response_200

    @staticmethod
    def get_fields():
        return {
            "access": str,
            "refresh": str,
            "dt": datetime.datetime,
            "env": str,
            "revision": str,
            "version": str,
        }

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
