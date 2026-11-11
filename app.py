"""Generate a project blueprint from a structured specification."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel,Field
app=FastAPI(title="AI App Builder")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
class Spec(BaseModel):name:str=Field(min_length=2,max_length=50);frontend:str="React";backend:str="FastAPI";database:str="PostgreSQL";features:list[str]=Field(min_length=1,max_length=12)
@app.post("/blueprint")
def blueprint(s:Spec):
 return {"project":s.name,"architecture":{"frontend":s.frontend,"backend":s.backend,"database":s.database},"suggested_structure":["frontend/src/components","frontend/src/pages","backend/app/api","backend/app/services","backend/tests","infra"],"milestones":[{"name":"Foundation","tasks":["Initialize repositories","Configure linting and tests","Add environment configuration"]},{"name":"Core features","tasks":[f"Implement {f}" for f in s.features]},{"name":"Release","tasks":["Add integration tests","Configure CI","Document deployment"]}],"security":["Keep secrets in environment variables","Validate all API inputs","Add authentication and authorization before production"]}