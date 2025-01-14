"""SQL Sensors for Airflow"""
from uuid import uuid4
from typing import Literal

from airflow.sensors.sql import SqlSensor

from regscale.airflow.sessions.sql import SQLQuery


class SqlSensorXcon(SqlSensor):
    def __init__(self, step_name: str = "sql_sensor_xcon", **kwargs):
        super().__init__(**kwargs)
        self.step_name = step_name

    def poke(self, context):
        self.log.info(f"Poking: {self.sql}")
        records = self._get_hook().get_first(self.sql, parameters=self.parameters)
        if not records:
            return False
        context["task_instance"].xcom_push(key=self.step_name, value=records)
        return True


def build_sql_sensor_xcon(
    sql: SQLQuery,
    name: str = None,
    conn_id: str = "platform_db",
    unique: bool = False,
    mode: Literal["reschedule", "poke"] = "poke",
    step_name: str = "sql_sensor_xcon",
    timeout: int = 60 * 60 * 24 * 7,
    poke_interval: int = 60 * 5,
    **kwargs,
) -> SqlSensorXcon:
    """Build a SQL Sensor that will push its results to XCom
    :param str sql: the SQL query to run
    :param str name: the name of the sensor
    :param str conn_id: the connection id to use
    :param bool unique: whether to make the sensor unique
    :param str mode: the mode of the sensor
    :param str step_name: the name of the step
    :param int timeout: the timeout of the sensor
    :param int poke_interval: the poke interval of the sensor
    :param dict kwargs: keyword arguments to pass to the sensor
    :return: the SQL Sensor
    :rtype: SqlSensorXcon
    """
    dag_run_dict = dict(zip(sql.dag_run_vars, sql.dag_run_vars))
    params_dict = dict(zip(sql.params, sql.params))
    if unique and name is not None:
        name = f"{name}-{str(uuid4())[:8]}"

    return SqlSensorXcon(
        task_id=name or f"sql_sensor-{name or str(uuid4())[:8]}",
        sql=sql.raw,
        conn_id=conn_id,
        params=params_dict or dag_run_dict,
        mode=mode,
        step_name=step_name,
        timeout=timeout,
        poke_interval=poke_interval,
        **kwargs,
    )


def build_sql_sensor(
    sql: SQLQuery,
    name: str = None,
    conn_id: str = "platform_db",
    unique: bool = False,
    mode: Literal["reschedule", "poke"] = "poke",
    timeout: int = 60 * 60 * 24 * 7,
    poke_interval: int = 60 * 5,
    **kwargs,
) -> SqlSensor:
    """Build a SQL Sensor from a SQLQuery object
    :param str sql: the SQL query to run
    :param str name: the name of the sensor
    :param str conn_id: the connection id to use
    :param bool unique: whether to make the sensor unique
    :param str mode: the mode of the sensor
    :param int timeout: the timeout of the sensor
    :param int poke_interval: the poke interval of the sensor
    :return: the SQL Sensor
    :rtype: SqlSensor
    """
    dag_run_dict = dict(zip(sql.dag_run_vars, sql.dag_run_vars))
    params_dict = dict(zip(sql.params, sql.params))
    if unique and name:
        name = f"{name}-{str(uuid4())[:8]}"
    if unique and name is None:
        name = f"sql_sensor-{str(uuid4())[:8]}"

    return SqlSensor(
        task_id=name,
        sql=sql.raw,
        conn_id=conn_id,
        params=params_dict or dag_run_dict,
        mode=mode,
        timeout=timeout,
        poke_interval=poke_interval,
        **kwargs,
    )
