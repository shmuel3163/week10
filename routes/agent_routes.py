from fastapi import APIRouter, HTTPException
from logs.set_logger import logger
from database.agent_db import agent


a_router = APIRouter(prefix="/agents", tags=["agents"])


@a_router.get("/")
def get_all_agent():
    logger.info("GET/get_all agent from table")
    return (agent.get_all_agents())


@a_router.get("/{id}")
def get_agent_by_id(id: int):
    logger.info("GET/get_agent_by_id=", id)
    search = agent.get_agent_by_id(id)
    if not search:
        logger.error(f'Agent not found id = {id}:')
        raise HTTPException(status_code=404, detail=f'Agent not found id = {id}:')
    else:
        logger.info(f'Agent id {id} found')
        return search


@a_router.post("/")
def add_new_agent(data: dict):
    agent_ranks = ["junior", "senior", "commander"]
    try:
        for key,val in data.items():
            data[key]=str(data[key]).lower()
        if data["agent_rank"] in agent_ranks:
            new_obj = agent.create_agent(data)
            logger.info("POST/ add_new_agent, secsessfull")
            return new_obj
        else:
            raise HTTPException()
        print(data)
    except Exception as e:
        logger.error(f'POST/add new agent filed : {e}')
        raise HTTPException(status_code=422, detail="e")
     
@a_router.put("/{id}")
def update_agent(id:int, data:dict):
    id_found = get_agent_by_id(id)
    if id_found:
        agent_ranks = ["junior", "senior", "commander"]
        if data["agent_rank"].lower() in agent_ranks:
            logger.info("PUT/updating agent with id =", id)
            result_of_exc = agent.update_agent(id, data)
            if result_of_exc == 0:
                logger.error("POST/f'Agent update with ID {id} failed'")
                raise HTTPException(status_code=404,detail=f'Agent update with ID {id} failed')
            else:
                logger.info(f'Agent update with ID {id} was successful')
                return f'Agent update with ID {id} was successful' 

@a_router.put("/{id}/deactivate")
def deactivate_agent(id:int):
    id_found = get_agent_by_id(id)
    if id_found:
        result_of_exc = agent.deactivate_agent(id)
        if result_of_exc == 0:
            logger.error("POST/f'Agent deactivate with ID {id} failed'")
            raise HTTPException(status_code= 404 ,detail=f'Agent deactivate with ID {id} failed')
        else:
            logger.info(f'Agent deactivate with ID {id} was successful')
            return f'Agent deactivate with ID {id} was successful' 

@a_router.get("/{id}/performance")
def get_performance(id: int):
    id_found = get_agent_by_id(id)
    if id_found:
        performance = agent.get_agent_performance(id)
        logger.info("GET/ agent_performance", performance)
        return performance






        
    



    




