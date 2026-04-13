# ============ 复制进 web 端时省略这些导入 ============
from magnus import submit_job, JobType, FileSecret
from typing import Annotated, Literal, Optional, List
# =====================================================
# 本蓝图用于agent利用shell命令自主执行简易的计算任务。

UserName = Annotated[str, {
    "label": "User Name",
    "placeholder": "your username on the cluster",
    "allow_empty": False,
}]

InputData = Annotated[Optional[FileSecret], {
    "label": "Analyzed Data",
    "description": "Upload via: magnus send data.tar.gz",
    "placeholder": "file secret code",
}]

Memory = Annotated[str, {
    "label": "Memory",
    "description": "Memory demand, e.g. 16G, 32G.",
    "placeholder": "16G",
}]

Priority = Annotated[Literal["A1", "A2", "B1", "B2"], {
    "label": "Priority",
    "description": "A1/A2: high priority (non-preemptible), B1/B2: low priority (preemptible by A)",
    "options": {
        "A1": {"label": "A1", "description": "Highest priority"},
        "A2": {"label": "A2", "description": "High priority"},
        "B1": {"label": "B1", "description": "Low priority"},
        "B2": {"label": "B2", "description": "Lowest priority"},
    },
}]

Runner = Annotated[Optional[str], {
    "label": "Runner",
    "description": "Override the default runner user",
    "placeholder": "leave empty for default",
}]

EntryCommand = Annotated[str, {
    "label": "Entry Command",
    "description": "Command to be executed.",
    "placeholder": "e.g. python main.py", 
}]


def blueprint(
    user_name: UserName,
    input_data: InputData,
    memory: Memory = "16G",
    priority: Priority = "B2",
    runner: Runner = None,
    entry_command: EntryCommand = f"echo No command provided",
):
    submit_job(
        task_name=f"Agent-Test",
        entry_command= entry_command,
        repo_name="your-repo",
        memory=memory,
        job_type=getattr(JobType, priority),
        runner=runner,
    )
