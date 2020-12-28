# app/admin/forms.py

#from app.admin.views import check_admin
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import Department, Employee, Role


class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RoleForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EmployeeAssignForm(FlaskForm):
    """
    Form For Admin to assign department and roles to emloyees
    """

    department = QuerySelectField(query_factory=lambda: Department.query.all(),
                                get_label="name") 
    
    role = QuerySelectField(query_factory=lambda: Role.query.all(),
                            get_label="name")

    submit = SubmitField('Submit')


