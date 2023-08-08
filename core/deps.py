from typing import Generator, Optional
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel
from core.database import Session
from core.auth import oauth2_schema
from core.configs import settings
from models.usuario_model import UsuarioModel


# utilizar como dado
class TokenData(BaseModel):
    username:Optional[str] = None


async def get_session() -> Generator:
    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()

# retorna o usuario pelo token de acesso
# atraves do token descobrir a pessoa

async def get_current_user(db:Session=Depends(get_session),
                           token:str=Depends(oauth2_schema)
                           )-> UsuarioModel:
    credential_exception:HTTPException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Não foi possivel autenticar a credencial',
        headers={'WWW-Authenticate': 'Bearer'},)
    
    # Pegar o token e decodificar ele
    print("Entrei TRY")
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.ALGORITHM],
            options={"verify_aud":False}
            )
        
        username: str = payload.get('sub')

        if username is None:
            print("Username None")
            raise credential_exception
        # pegar os dados do token
        token_data:TokenData = TokenData(username=username)

    # ERRO AQUI
    except JWTError as erro: # se nao conseguir decodificar
        print('Foi aqui jwtERRO', erro)
        raise credential_exception
    
    async with db as session:
        try:
            query = select(UsuarioModel).filter(UsuarioModel.id == int(token_data.username))
            result = await session.execute(query)
            usuario:UsuarioModel = result.scalars().unique().one_or_none()

            if usuario is None:
                print('Usuario Erro')
                raise credential_exception
        except Exception as erro:
            print('Erro na busca')
            raise erro
        return usuario

    