from flask import Blueprint
from core.apis import decorators
from core.models.assignments import Assignment
from .schema import AssignmentSchema, AssignmentGradeSchema
from core.apis.responses import APIResponse
from core import db

principal_assignment_resources = Blueprint('principal_assignment_resources',__name__)

@principal_assignment_resources.route('/', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """List all submitted and graded assignments"""
    assignments = Assignment.get_all_submitted_assignments()
    assignments_dump = AssignmentSchema().dump(assignments, many=True)
    return APIResponse.respond(data=assignments_dump)

@principal_assignment_resources.route('/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def re_grade_assignment(p, incoming_payload):
    """Grade or re-grade an assignment"""
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)
    graded_assignment = Assignment.mark_grade(
        _id=grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
        auth_principal=p
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)
    