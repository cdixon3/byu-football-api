import settings
from database.models import *
from flask_restplus import Resource
from api.api_def import api
from api.serializers import *

linebacker_nmsp = settings.linebacker_nmsp


@linebacker_nmsp.route('/reps', methods=["GET"])
class GetLinebackers(Resource):

    @api.marshal_with(linebacker_serializer)
    def get(self):
        """
        Returns metadata about linebackers
        """

        linebackers = LinebackerReps.query.all()

        return linebackers, 200
