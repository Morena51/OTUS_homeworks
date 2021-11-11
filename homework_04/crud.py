"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
from datetime import datetime

import asyncpg
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, joinedload, selectinload

from models import User, Post


async def create_user(user_in: UserIn, db_session: AsyncSession) -> User:
    user = User(username=user_in.username)
    async with db_session.begin():
        db_session.add(user)
    return user


async def create_many_users(users_to_create: int, db_session: AsyncSession) -> List[User]:
    rnd_elem = datetime.now().microsecond
    users = [
        User(username=f"user_{rnd_elem}_{i:03}")
        for i in range(1, users_to_create + 1)
    ]
    async with db_session.begin():
        db_session.add_all(users)
    return users

    async def create_users_and_and_authors():

        async with async_session() as session:
            async with session.begin():
                sam_author = Author(name="Sam White", bio="I like docker")
                session.add_all(
                    [
                        User(username="john", author=Author(name="John Smith", bio="I like Python")),
                        User(username="sam", author=sam_author),
                    ]
                )

    async def query_authors():
        stmt = select(User).options(joinedload(User.author))

        async with async_session() as session:
            result = await session.execute(stmt)

        for user in result.scalars():
            user: User
            print(user)
            print(f"username #{user.id} {user.username} created at: {user.created_at}")
            print("user author:", user.author)


async def create_posts(posts: list[Post]):
        async with async_session() as session:
            async with session.begin():
                session.add_all(posts)
