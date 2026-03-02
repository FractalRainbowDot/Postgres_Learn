from fastapi import APIRouter, Depends
from typing import List
from .schemas import UserCreateRequest, UserResponse
from application.use_cases import AddUserUseCase, GetAllUsersUseCase
from .dependencies import get_add_user_use_case, get_get_all_users_use_case

router = APIRouter()

@router.post("/users", response_model=UserResponse)
async def create_user(
    user_request: UserCreateRequest,
    use_case: AddUserUseCase = Depends(get_add_user_use_case)
):
    """
    Эндпоинт для создания нового пользователя.
    """
    # Преобразуем DTO запроса в доменную сущность
    from domain.entities import User
    user_entity = User(name=user_request.name, surname=user_request.surname, age=user_request.age)
    
    # Вызываем Use Case
    created_user = await use_case.execute(user_entity)
    
    # Возвращаем DTO ответа
    return UserResponse(
        id=created_user.id,
        name=created_user.name,
        surname=created_user.surname,
        age=created_user.age
    )

@router.get("/users", response_model=List[UserResponse])
async def get_users(
    use_case: GetAllUsersUseCase = Depends(get_get_all_users_use_case)
):
    """
    Эндпоинт для получения списка всех пользователей.
    """
    users = await use_case.execute()
    
    # Преобразуем список доменных сущностей в список DTO ответов
    return [
        UserResponse(
            id=user.id,
            name=user.name,
            surname=user.surname,
            age=user.age
        ) for user in users
    ]
