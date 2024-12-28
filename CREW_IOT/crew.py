from crewai import Crew
from tasks import iot_research_task
from agents import iot_research_agent
from crewai import Process

crew=Crew(
    agents=[iot_research_agent],
    tasks=[iot_research_task],
    process=Process.sequential,
)
iot_device_detail=crew.kickoff(inputs={'input':'working on portable device that can connect with any device and tell the energy consumption with bill'})
print(iot_device_detail)
