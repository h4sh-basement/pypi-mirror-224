from __future__ import annotations

import datetime
import pydantic
import typing

from pydantic import BaseModel

from feedancy.lib.base import BaseApi
from feedancy.lib.request import ApiRequest
from feedancy.lib import json
class Contact(BaseModel):
    data: str 
    id: int 
    name: typing.Optional[typing.Union[str, None]]  = None
    type: str 

class VacancyContact(BaseModel):
    contact: typing.Union[Contact, None] 

class Currency(BaseModel):
    code: str 
    id: int 
    name: str 

class Salary(BaseModel):
    currency: Currency 
    id: int 
    max_value: typing.Optional[typing.Union[int, None]]  = None
    min_value: typing.Optional[typing.Union[int, None]]  = None

class Internship(BaseModel):
    city: str 
    company: typing.Union[str, None] 
    contacts: typing.Union[typing.List[VacancyContact], None] 
    duration: typing.Optional[typing.Union[int, None]]  = None
    external_id: str 
    has_employment: typing.Optional[typing.Union[bool, None]]  = None
    has_portfolio: typing.Optional[typing.Union[bool, None]]  = None
    has_test_task: typing.Optional[typing.Union[bool, None]]  = None
    id: int 
    is_paid: typing.Optional[typing.Union[bool, None]]  = None
    link: str 
    name: str 
    publicated_at: typing.Optional[typing.Union[datetime.datetime, None]]  = None
    raw_description: typing.Optional[typing.Union[str, None]]  = None
    recruitment_end_date: typing.Optional[typing.Union[datetime.datetime, None]]  = None
    requirement: typing.Optional[typing.Union[str, None]]  = None
    responsibility: typing.Optional[typing.Union[str, None]]  = None
    salary: typing.Union[Salary, None] 
    source: str 
    test_task_link: typing.Optional[typing.Union[str, None]]  = None
    work_format: typing.Optional[typing.Union[typing.Union[str, str, str], None]]  = None

class PaginatedInternshipList(BaseModel):
    count: typing.Optional[int]  = None
    next: typing.Optional[typing.Union[str, None]]  = None
    previous: typing.Optional[typing.Union[str, None]]  = None
    results: typing.Optional[typing.List[Internship]]  = None

def make_request(self: BaseApi,


    page: int = ...,

) -> PaginatedInternshipList:
    

    
    body = None
    

    m = ApiRequest(
        method="GET",
        path="/api/v1/internship/".format(
            
        ),
        content_type=None,
        body=body,
        headers=self._only_provided({
        }),
        query_params=self._only_provided({
                "page": page,
            
        }),
        cookies=self._only_provided({
        }),
    )
    return self.make_request({
    
        "200": {
            
                "application/json": PaginatedInternshipList,
            
        },
    
    }, m)