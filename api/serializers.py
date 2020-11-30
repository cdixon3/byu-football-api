from api.api_def import api
from flask_restplus import fields

linebacker_serializer = api.model('Linebackers', {
    'linebacker_rep_id': fields.Integer(
        readOnly=True,
        description='Linebacker Rep ID.'),
    'playerid': fields.String(
        readOnly=True,
        description='Player ID'
    ),
    'rep_date': fields.DateTime(
        readOnly=True,
        description='Create date for analysis'),
    'periodnum': fields.Integer(
        readOnly=True,
        description='Period Number'
    ),
    'playnum': fields.Integer(
        readOnly=True,
        description='Play Number'
    ),
    'drill': fields.String(
        readOnly=True,
        description='Drill'
    ),
    'alignmentquality': fields.Integer(
        readOnly=True,
        description='Alignment Quality'
    ),
    'assignmentquality': fields.Integer(
        readOnly=True,
        description='Assignment Quality'
    ),
    'effortquality': fields.Integer(
        readOnly=True,
        description='Effort Quality'
    ),
    'finishquality': fields.Integer(
        readOnly=True,
        description='Finish Quality'
    ),
    'position': fields.String(
        readOnly=True,
        description='Position'
    ),
    'note': fields.String(
        readOnly=True,
        description='Note'
    ),
})
