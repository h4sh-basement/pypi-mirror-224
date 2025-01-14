_MONITOR MONITORMANAGER ON WORKERS 3;

_MONITOR CREATE TASK task1 TAG=cpu_count;
_MONITOR CREATE TASK task1 TAG=cpu_count_physical;
_MONITOR CREATE TASK task1 TAG=cpu_percent;
_MONITOR CREATE TASK task1 TAG=cpu_times;
_MONITOR CREATE TASK task1 TAG=memory;
_MONITOR CREATE TASK task1 TAG=network NAME='eth0';
_MONITOR CREATE TASK task1 TAG=disk NAME='PhysicalDrive[12]';
_MONITOR CREATE TASK task1 TAG=process USERNAME=ldb;
_MONITOR START TASK ALL;
_SLEEP 10;
_SET TERMOUT OFF
_MONITOR LIST TASK;

-- 校验采集结果
_SET FEEDBACK OFF
_MONITOR REPORT TASK ALL;
> {%
import copy
x = copy.copy(lastCommandResult)
%}
_SET FEEDBACK ON
_ASSERT {% len(x["rows"]) >=5 %}
