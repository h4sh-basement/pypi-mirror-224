from .resource import *


class V2(object):
    def __init__(self, config: Config) -> None:
        self.department: Department = Department(config)
        self.employee: Employee = Employee(config)
        self.job_change: JobChange = JobChange(config)
        self.person: Person = Person(config)
        self.pre_hire: PreHire = PreHire(config)
