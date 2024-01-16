from flask import Blueprint
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher
from .schema import TeacherSchema

principal_teacher_blueprint = Blueprint('principal_teacher_blueprint',__name__)

@principal_teacher_blueprint.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def get_all_teachers(p):
    """Return all teachers"""
    teachers = Teacher.list_teachers()
    teachers_dump = TeacherSchema().dump(teachers,many=True)
    return APIResponse.respond(data=teachers_dump)