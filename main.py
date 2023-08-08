from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title='Cursos API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ =="__main__":
    import uvicorn
    uvicorn.run('main:app', port=8000,
                log_level='info', reload=True)
    



#token-gabi
#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNlc3NfdG9rZW4iLCJleHAiOjE2OTE0NDY4NDksImlhdCI6MTY5MTQ0NTA0OSwic3ViIjoiNCJ9.XyCOtpwRRmWtPM3_pNwiDDKFafdmSTw88faGTWaJSP0

#token nicholas
#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNlc3NfdG9rZW4iLCJleHAiOjE2OTIwNTQ5NjEsImlhdCI6MTY5MTQ1MDE2MSwic3ViIjoiNSJ9.zYxL6d9fec_LuXriTIurY5DcwoKZDkfqpXq8kM8KXJQ
"""eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNlc3NfdG9rZW4iLCJleHAiOjE2OTIwNTYyMTgsImlhdCI6MTY5MTQ1MTQxOCwic3ViIjoiNSJ9.CScFfafg_FRz3I8gAEedJ8PYYzEVkF2pQrcObH1PUYo"""

"""
caio
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNlc3NfdG9rZW4iLCJleHAiOjE2OTIwNTc1NzYsImlhdCI6MTY5MTQ1Mjc3Niwic3ViIjoiNiJ9.HRMmQqakPbZLLIwjhetbeq6z_XR5noNimQ7lUYkukt0"""
"""$2b$12$PdwffZzizN6lLDwdCfA7L.RVBcD/Nd5/mBTmSbT831mKb14tIelE."""