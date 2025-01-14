from typing import Any, List, Optional, Dict
from pydantic import BaseModel, Field
from enum import Enum

class IOPortType(str, Enum):
    BOOLEAN = "boolean"
    NUMBER = "number"
    INTEGER = "integer"
    STRING = "string"
    ARRAY = "array"
    OBJECT = "object"
    NULL = "null"

class HykoExtraTypes(str, Enum):
    IMAGE = "image"
    AUDIO = "audio"
    VIDEO = "video"
    
    
class JsonSchemaEnum(BaseModel):
    enum: list[str]
    type: str
    
class Property(BaseModel):
    type: Optional[IOPortType | HykoExtraTypes] = None
    anyOf: Optional [List['Property']] = None
    items: Optional['Property'] = None
    prefixItems: Optional[List['Property']] = None
    minItems: Optional[int] = None
    maxItems: Optional[int] = None
    description: Optional[str] = None
    default: Optional[Any] = None
    ref: Optional[str] = Field(default=None, alias="$ref") 
    
class HykoJsonSchema(BaseModel):
    properties: Dict[str, Property] = {}
    required: List[str] = []
    defs: Optional[Dict[str, JsonSchemaEnum]] = Field(default=None, alias="$defs")
    
class HykoJsonSchemaExt(HykoJsonSchema):
    friendly_property_types: Dict[str, str] = {}
    
class MetaDataBase(BaseModel):
    description: str
    inputs: HykoJsonSchemaExt
    outputs: HykoJsonSchemaExt
    params: HykoJsonSchemaExt
    requires_gpu: bool

class MetaData(MetaDataBase):
    version: str
    name: str
    category: str

class CoreModel(BaseModel):
    pass