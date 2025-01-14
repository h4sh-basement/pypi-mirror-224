import os

import jwt

import datetime

from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


class JWT():
    security = HTTPBearer()
    secret = os.getenv("SECRET_JWT_API")
    user = os.getenv("JWT_USER")
    password = os.getenv("JWT_PASSWORD")

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=["HS256"])
            return payload["user"]

        except jwt.ExpiredSignatureError as e:
            raise HTTPException(status_code=401, detail="Token Expirado") from e
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=401, detail="Token Invalido") from e

    def auth_wrapper(
        self,
        auth: HTTPAuthorizationCredentials = Security(security)
    ):
        return self.decode_token(auth.credentials)

    def create_access_token(self, exp_time):
        context = {
            "user": self.user,
            "password": self.password,
            "exp": exp_time + datetime.timedelta(minutes=5)
        }


        return jwt.encode(context, self.secret, algorithm="HS256")
