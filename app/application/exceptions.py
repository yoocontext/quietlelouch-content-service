from fastapi import FastAPI, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

from domain.exceptions import ApplicationException
from domain.values.exceptions import (
    MediaTypeNotExistException,
    TextTooLongException,
    TextTooShortException,
)
from infra.pg.repository.common.exceptions import (
    ObjectNotFoundException,
    MissingRequiredFieldException,
)
from infra.s3.exceptions import (
    ContentNotExistException,
)

exceptions_map: dict[type[ApplicationException], int] = {
    MediaTypeNotExistException: HTTP_404_NOT_FOUND,
    TextTooShortException: HTTP_400_BAD_REQUEST,
    TextTooLongException: HTTP_400_BAD_REQUEST,
    ObjectNotFoundException: HTTP_404_NOT_FOUND,
    MissingRequiredFieldException: HTTP_404_NOT_FOUND,
    ContentNotExistException: HTTP_404_NOT_FOUND,

}

def register_exception_handlers(app: FastAPI):
    @app.exception_handler(ApplicationException)
    async def handler(request, exc: ApplicationException):
        if exceptions_map.get(type(exc), None):
            status: int = exceptions_map.get(type(exc))
            raise HTTPException(status_code=status, detail=exc.message)
        else:
            raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Unknown error")
