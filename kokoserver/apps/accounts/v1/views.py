"""
Generated by 'esmerald createapp' using Esmerald 2.4.0.
"""
from typing import List

from accounts.models import User
from pydantic import BaseModel

from esmerald import get
from esmerald.openapi.datastructures import OpenAPIResponse


class Error(BaseModel):
    detail: str


@get(
    "/users",
    summary="Returns a list of users",
    responses={
        200: OpenAPIResponse(model=[User]),
        401: OpenAPIResponse(model=Error),
    },
)
async def get_all_users() -> List[User]:
    """
    Returns the list of users in the system.
    """
    users = await User.query.all()
    return users
