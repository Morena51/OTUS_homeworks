from pydantic import BaseModel


class AllureProjectCoverage(BaseModel):
    id: int = None
    name: str = None
    createdDate: str = None
    lastModifiedDate: str = None
    createdBy: str = None
    lastModifiedBy: str = None
    automatedTestCasesCount: int = None
    manualTestCasesCount: int = None
    launchesCount: int = None
    collaborators: list = []


class AllureContent(BaseModel):
    content = [AllureProjectCoverage]


class AllureAccessToken(BaseModel):
    access_token: str = None
    token_type: str = None
    refresh_token: str = None
    expires_in: int = None
    scope: str = None
    jti: str = None
