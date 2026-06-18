from database.db_connection import db


class AgentDB:
    def __init__(self):
        self.conn = db.get_connection()
        pass

    def create_agent(self, data):
        print(data)
        cur = self.conn.cursor()
        str_to_exe = (
            "INSERT INTO agents(`name`,specialty,agent_rank) VALUES (%s, %s, %s)"
        )
        values_to_exe = (
            str(data["name"]),
            str(data["specialty"]),
            str(data["agent_rank"]),
        )

        print(values_to_exe)
        cur.execute(str_to_exe, values_to_exe)
        new_agent_id = cur.lastrowid
        self.conn.commit()
        cur.close()
        return self.get_agent_by_id(new_agent_id)

    def get_all_agents(self):
        cur = self.conn.cursor(dictionary=True)
        cur.execute("select * FROM agents")
        list_of_agents = cur.fetchall()
        cur.close()
        return list_of_agents

    def get_agent_by_id(self, id):
        cur = self.conn.cursor(dictionary=True)
        str_to_exe = "select * FROM agents WHERE `id`= %s"
        values_to_exe = (id,)
        cur.execute(str_to_exe, values_to_exe)
        return cur.fetchone()

    def update_agent(self, id, data):
        cur = self.conn.cursor(dictionary=True)
        str_to_exe = (
            "update agents SET `name` = %s ,"
            "specialty = %s ,agent_rank = %s WHERE `id` = %s"
        )
        values_to_exe = (
            str(data["name"]),
            str(data["specialty"]),
            str(data["agent_rank"]),
            id,
        )
        cur.execute(str_to_exe, values_to_exe)
        result_of_exc = cur.rowcount
        self.conn.commit()
        cur.close()
        return result_of_exc

    def deactivate_agent(self, id):
        cur = self.conn.cursor()

        str_to_exe = "update agents SET is_active = False WHERE `id` = %s"
        values_to_exe = (id,)
        cur.execute(str_to_exe, values_to_exe)
        result_of_exc = cur.rowcount
        self.conn.commit()
        cur.close()
        return result_of_exc

    def increment_completed(self, id):
        agent_data = self.get_agent_by_id(id)
        num_of_completed = agent_data["completed_missions"]

        cur = self.conn.cursor()
        str_to_exe = "update agents SET completed_missions = %s  WHERE `id` = %s"
        values_to_exe = (
            num_of_completed + 1,
            id,
        )
        cur.execute(str_to_exe, values_to_exe)
        result_of_exc = cur.rowcount
        self.conn.commit()
        cur.close()

        if result_of_exc == 0:
            return {"massage :": f" update completed_missions number in ID {id} failed"}
        else:
            return {
                "massage :": f"update completed_missions number in {id} was successful"
            }

    def increment_failed(self, id):

        agent_data = self.get_agent_by_id(id)
        num_of_failed = agent_data["failed_missions"]

        cur = self.conn.cursor()
        str_to_exe = "update agents SET failed_missions = %s  WHERE `id` = %s"
        values_to_exe = (
            num_of_failed + 1,
            id,
        )
        cur.execute(str_to_exe, values_to_exe)
        result_of_exc = cur.rowcount
        self.conn.commit()
        cur.close()

        if result_of_exc == 0:
            return {"massage :": f" update failed_missions number in ID {id} failed"}
        else:
            return {
                "massage :": f"update failed_missions number in {id} was successful"
            }

    def get_agent_performance(self, id):
        agent_data = self.get_agent_by_id(id)
        print(agent_data)
        sum_missions = int(agent_data["completed_missions"]) + int(
            agent_data["failed_missions"]
        )
        print(sum_missions)
        if sum_missions == 0:
            return {
                "completed_missions": 0,
                "failed_missions": 0,
                "success_rate ": 0,
            }
        else:
            calculteted_success_rate = (
                int(agent_data["completed_missions"]) / sum_missions * 100
            )

            new_calculeted_dict = {
                "completed_missions": agent_data["completed_missions"],
                "failed_missions": agent_data["failed_missions"],
                "success_rate ": f"{calculteted_success_rate} %",
            }
            return new_calculeted_dict

    def count_active_agents(self):

        cur = self.conn.cursor()
        cur.execute("select COUNT(*) FROM agents where is_active = True")
        num_of_active = cur.fetchone()
        cur.close()
        return num_of_active


agent = AgentDB()
