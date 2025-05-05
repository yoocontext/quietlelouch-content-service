from faststream.rabbit import RabbitRouter


router = RabbitRouter()

#
# @router.subscriber("register-user", no_ack=False,)
# async def register_user(event: ...) -> None:
#     ...
