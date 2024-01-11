from app.user.adapter.output.persistence.sqlalchemy.user import UserSQLAlchemyRepo
from app.user.domain.entity.user import User
from app.user.domain.repository.user import UserRepo


class UserRepositoryAdapter:
    def __init__(self):
        self.user_repo: UserRepo = UserSQLAlchemyRepo()

    async def get_users(
        self,
        *,
        limit: int = 12,
        prev: int | None = None,
    ) -> list[User]:
        return await self.user_repo.get_users(limit=limit, prev=prev)

    async def get_user_by_email_or_nickname(
        self,
        *,
        email: str,
        nickname: str,
    ) -> User | None:
        return await self.user_repo.get_user_by_email_or_nickname(
            email=email,
            nickname=nickname,
        )

    async def get_user_by_id(self, *, user_id: int) -> User | None:
        return await self.user_repo.get_user_by_id(user_id=user_id)

    async def get_user_by_email_and_password(
        self,
        *,
        email: str,
        password: str,
    ) -> User | None:
        return await self.user_repo.get_user_by_email_and_password(
            email=email,
            password=password,
        )

    async def save(self, *, user: User) -> None:
        await self.user_repo.save(user=user)
