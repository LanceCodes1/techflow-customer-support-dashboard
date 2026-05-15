from faker import Faker
import random

from database import SessionLocal
from models import SupportCall

fake = Faker()

session = SessionLocal()

issue_types = [
    "Billing",
    "Technical Support",
    "Account Access",
    "Service Outage",
]

resolution_statuses = [
    "Resolved",
    "Escalated",
    "Pending",
]

for _ in range(1000):

    wait_time = random.randint(1, 45)

    call = SupportCall(
        customer_name=fake.name(),
        issue_type=random.choice(issue_types),
        resolution_status=random.choice(resolution_statuses),
        call_duration=round(random.uniform(2.0, 60.0), 2),
        satisfaction_score=random.randint(1, 5),
    )

    session.add(call)

session.commit()
session.close()

print("Successfully seeded 1,000 support call records.")