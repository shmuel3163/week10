from database.mission_db import mission
from database.agent_db import agent
from fastapi import APIRouter
from logs.set_logger import logger

r_router = APIRouter(prefix="/reports", tags=["reports"])


@r_router.get("/missions-by-status")
def get_full_report():
    new = mission.count_by_status("NEW")
    assigned = mission.count_by_status("ASSIGNED")
    in_progress = mission.count_by_status("IN_PROGRESS")
    completed = mission.count_by_status("COMPLETED")
    failed = mission.count_by_status("FAILED")
    cancelled = mission.count_by_status("CANCELLED")
    logger.info("GET/ get_full _report ")
    return {
        "new": new,
        "assigned": assigned,
        "in_progress": in_progress,
        "completed": completed,
        "failed": failed,
        "cancelled": cancelled,
    }


@r_router.get("/summary")
def get_sumery():
    active_agents_count = agent.count_active_agents()
    total_missions = mission.count_all_missions()
    open_missions = mission.count_open_missions()
    completed_missions = mission.count_by_status("COMPLETED")
    failed_missions = mission.count_by_status("FAILED")
    cancelled = mission.count_by_status("CANCELLED")
    logger.info("GET/ get_sumery ")
    return {
        "active_agents_count": active_agents_count,
        "total_missions": total_missions,
        "open_missions": open_missions,
        "completed_missions": completed_missions,
        "failed_missions": failed_missions,
        "cancelled_missions": cancelled,
    }
