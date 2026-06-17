from db_connection import db


class Mission_db:
    def __init__(self):
        self.conn = db.get_connection()

    def create_mission(self, data):
        pass

    def get_all_missions(self):
        cur = self.conn.cursor()
        cur.execute("select * FROM missions")
        list_of_missions = cur.fetchall()
        cur.close()
        return list_of_missions

    def get_mission_by_id(self, id):
        cur = self.conn.cursor(dictionary=True)
        str_to_exe = "select * FROM missions WHERE `id`= %s"
        values_to_exe = (id,)
        cur.execute(str_to_exe, values_to_exe)
        return cur.fetchone()

    def assign_mission(self, m_id, a_id):
        cur = self.conn.cursor()
        str_to_exe = "update missions SET assigned_agent_id = %s WHERE `id` = %s"
        values_to_exe = (a_id, m_id)
        cur.execute(str_to_exe, values_to_exe)
        self.conn.commit()
        result_of_exc = cur.rowcount
        cur.close()

        if result_of_exc == 0:
            return {"massage :": f" assign mission {m_id} to agent {a_id} failed"}
        else:
            return {
                "massage :": f" assign mission {m_id} to agent {a_id} was successful"
            }

    def update_mission_status(self, id, status):
        cur = self.conn.cursor()
        str_to_exe = "update missions SET status = %s WHERE `id` = %s"
        values_to_exe = (status, id)
        cur.execute(str_to_exe, values_to_exe)
        result_of_exc = cur.rowcount
        self.conn.commit()
        cur.close()

        if result_of_exc == 0:
            return {"massage :": f'update mission {id} with status :{status}  failed'}
        else:
            return {
                "massage :": f'update mission {id} with status :{status} success'}

    def get_open_missions_by_agent(self, id):
        cur = self.conn.cursor()
        str_to_exe = "select * FROM missions where status = 'ASSIGNED' or status ='IN_PROGRESS' AND assigned_agent_id = %s "
        values_to_exe = (id,)
        cur.execute(str_to_exe, values_to_exe)
        open_missions = cur.fetchall()
        cur.close()
        return open_missions

    def count_all_missions(self):
        cur = self.conn.cursor()
        cur.execute("select COUNT(*) FROM missions")
        num_of_missions = cur.fetchone()
        cur.close()
        return num_of_missions

    def count_by_status(self, status):
        cur = self.conn.cursor()
        str_to_exe = "select COUNT(*) FROM missions where status = %s "
        values_to_exe = (status,)
        cur.execute(str_to_exe, values_to_exe)
        num_of_missions = cur.fetchone()
        cur.close()
        return num_of_missions

    def count_open_missions(self):
        cur = self.conn.cursor()
        str_to_exe = "select COUNT(*) FROM missions where status = 'ASSIGNED' or status ='IN_PROGRESS'"
        cur.execute(str_to_exe)
        num_of_open_missions = cur.fetchone()
        cur.close()
        return num_of_open_missions
    
    def count_critical_missions(self):
        cur = self.conn.cursor()
        str_to_exe = "select COUNT(*) FROM missions where difficulty ='critical'"
        cur.execute(str_to_exe)
        num_of_critical_missions = cur.fetchone()
        cur.close()
        return num_of_critical_missions

    def get_top_agent(self):
        pass 
        
        
