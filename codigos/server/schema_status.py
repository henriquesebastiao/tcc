from pydantic import BaseModel

class CpuFreq(BaseModel):
    current: float
    min: float
    max: float

class Memory(BaseModel):
    total: int
    available: int
    percent: float
    used: int
    free: int
    active: int
    inactive: int
    buffers: int
    cached: int
    shared: int
    slab: int

class StatusPerCore(BaseModel):
    cpu_frequency: CpuFreq
    cpu_percent: float

class StatusSchema(BaseModel):
    number_of_cores: int
    cpu_frequency: CpuFreq
    cpu_percent: float
    status_per_core: list[StatusPerCore]
    memory: Memory