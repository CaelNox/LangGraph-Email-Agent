from graph.email_graph import build_email_graph
from data.sample_emails import sample_emails
from langsmith import trace
from evaluations.log_feedback import log_feedback

graph = build_email_graph()

state = {
    **sample_emails[0],
    "intent": None,
    "urgency": None,
    "action": None,
    "draft_reply": None,
    "approval_required": None,
    "approved": None,
    "follow_up_date": None,
    "sla_deadline": None,
    "sla_violated": None,
    "history": [],
    "retry_count": 0,
    "max_retries": 2,
    "approval_feedback": None,
    "previous_drafts": [],
    "escalated": False,
    "escalation_reason": None,
}

final_state = graph.invoke(state)
from evaluations.evaluators import (
    eval_action_routing,
    eval_urgency,
    eval_approval,
    eval_sla,
)

eval_action_routing(final_state)
eval_urgency(final_state)
eval_approval(final_state)
eval_sla(final_state)


print("\nFINAL STATE")
for k, v in final_state.items():
    print(f"{k}: {v}")

with trace(name="email_ops_run") as run:
    final_state = graph.invoke(state)

log_feedback(run.id, final_state)