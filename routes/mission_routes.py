from fastapi import APIRouter, HTTPException
from logs.set_logger import logger
from database.mission_db import mission
from database.agent_db import agent


m_router = APIRouter(prefix="/mission", tags=["missions"])


@m_router.get("")
def get_all_missions():
    logger.info("GET/get_all missins from table")
    return mission.get_all_missions()


@m_router.get("/{id}")
def get_mission_by_id(id: int):
    logger.info("GET/get_mission_by_id=", id)
    search = mission.get_mission_by_id(id)
    if not search:
        logger.error(f"Mission not found id = {id}:")
        raise HTTPException(status_code=404, detail=f"Mission not found id = {id}")
    else:
        logger.info(f"Mission id {id} found")
        return search


@m_router.post("")
def add_new_mission(data: dict):
    try:
        for key in data.keys():
            data[key] = str(data[key]).lower()
            new_obj = mission.create_mission(data)
            logger.info("POST/ add_new_mission, secsessfull")
            return new_obj
        else:
            raise HTTPException()
    except Exception as e:
        logger.error(f"POST/add new mission filed : {e}")
        raise HTTPException(status_code=422, detail="e")


@m_router.put("/{id}/start")
def start_mission(id: int):
    logger.info("PUT/updating mission with id =", id)
    result_of_exc = mission.update_mission_status(id, status="IN_PROGRESS")
    if result_of_exc == 0:
        logger.error("Put/f'mission update with ID {id} failed'")
        raise HTTPException(
            status_code=404, detail=f"mission update with ID {id} failed"
        )
    else:
        logger.info(f"mission update with ID {id} was successful")
        return f"mission update with ID {id} was successful"


@m_router.put("/{id}/complete")
def mark_completed(id: int):
    logger.info("PUT/updating mission with id =", id)
    result_of_exc = mission.update_mission_status(id, status="COMPLETED")
    agent.increment_completed(id)
    if result_of_exc == 0:
        logger.error(f"POST/mission update with ID {id} failed")
        raise HTTPException(
            status_code=404, detail=f"mission update with ID {id} failed"
        )
    else:
        logger.info(f"mission update with ID {id} was successful")
        return f"mission update with ID {id} was successful"


@m_router.put("/{id}/fail")
def mark_failed(id: int):
    logger.info("PUT/updating mission with id =", id)
    result_of_exc = mission.update_mission_status(id, status="FAILED")
    agent.increment_failed(id)
    if result_of_exc == 0:
        logger.error(f"POST/mission update with ID {id} failed")
        raise HTTPException(
            status_code=404, detail=f"mission update with ID {id} failed"
        )
    else:
        logger.info(f"mission update with ID {id} was successful")
        return f"mission update with ID {id} was successful"


@m_router.put("/{id}/cancel")
def mark_cancel(id: int):
    logger.info("PUT/canceling mission with id =", id)
    result_of_exc = mission.update_mission_status(id, status="CANCELLED")
    if result_of_exc == 0:
        logger.error(f"POST/mission update with ID {id} cancel")
        raise HTTPException(
            status_code=404, detail=f"mission update with ID {id} cancel"
        )
    else:
        logger.info(f"mission update with ID {id} was successful")
        return f"mission update with ID {id} was successful"
