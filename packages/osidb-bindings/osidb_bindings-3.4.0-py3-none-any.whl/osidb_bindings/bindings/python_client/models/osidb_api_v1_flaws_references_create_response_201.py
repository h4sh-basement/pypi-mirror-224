import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.flaw_reference_type import FlawReferenceType
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="OsidbApiV1FlawsReferencesCreateResponse201")


@attr.s(auto_attribs=True)
class OsidbApiV1FlawsReferencesCreateResponse201(OSIDBModel):
    """ """

    flaw: str
    url: str
    uuid: str
    embargoed: bool
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    description: Union[Unset, str] = UNSET
    type: Union[Unset, FlawReferenceType] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        flaw = self.flaw
        url = self.url
        uuid = self.uuid
        embargoed = self.embargoed
        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        description = self.description
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):

            type = FlawReferenceType(self.type).value

        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env
        revision = self.revision
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if flaw is not UNSET:
            field_dict["flaw"] = flaw
        if url is not UNSET:
            field_dict["url"] = url
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if embargoed is not UNSET:
            field_dict["embargoed"] = embargoed
        if created_dt is not UNSET:
            field_dict["created_dt"] = created_dt
        if updated_dt is not UNSET:
            field_dict["updated_dt"] = updated_dt
        if description is not UNSET:
            field_dict["description"] = description
        if type is not UNSET:
            field_dict["type"] = type
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
        flaw = d.pop("flaw", UNSET)

        url = d.pop("url", UNSET)

        uuid = d.pop("uuid", UNSET)

        embargoed = d.pop("embargoed", UNSET)

        _created_dt = d.pop("created_dt", UNSET)
        created_dt: datetime.datetime
        if isinstance(_created_dt, Unset):
            created_dt = UNSET
        else:
            created_dt = isoparse(_created_dt)

        _updated_dt = d.pop("updated_dt", UNSET)
        updated_dt: datetime.datetime
        if isinstance(_updated_dt, Unset):
            updated_dt = UNSET
        else:
            updated_dt = isoparse(_updated_dt)

        description = d.pop("description", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, FlawReferenceType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = FlawReferenceType(_type)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        osidb_api_v1_flaws_references_create_response_201 = cls(
            flaw=flaw,
            url=url,
            uuid=uuid,
            embargoed=embargoed,
            created_dt=created_dt,
            updated_dt=updated_dt,
            description=description,
            type=type,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        osidb_api_v1_flaws_references_create_response_201.additional_properties = d
        return osidb_api_v1_flaws_references_create_response_201

    @staticmethod
    def get_fields():
        return {
            "flaw": str,
            "url": str,
            "uuid": str,
            "embargoed": bool,
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
            "description": str,
            "type": FlawReferenceType,
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
