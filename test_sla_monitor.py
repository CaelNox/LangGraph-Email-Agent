from agents.intent_classifier import intent_classifier
from agents.urgency_estimator import urgency_estimator
from agents.action_router import action_router
from agents.followup_scheduler import followup_scheduler
from agents.sla_monitor import sla_monitor
from data.sample_emails import sample_emails

state = {
    **sample_emails[9],  # email_id 010
    "intent": None,
    "urgency": None,
    "action": None,
    "draft_reply": None,
    "approval_required": None,
    "approved": None,
    "follow_up_date": None,
    "sla_deadline": None,
    "sla_violated": None,
    "history": []
}

state = intent_classifier(state)
state = urgency_estimator(state)
state = action_router(state)
state = followup_scheduler(state)
state = sla_monitor(state)

print("SLA violated:", state["sla_violated"])
print("History:")
for h in state["history"]:
    print("-", h)
