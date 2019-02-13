from app import api
from routes.base import BaseApi


class DeployApi(BaseApi):
    col_name = 'deploys'

    arguments = (
    )


api.add_resource(DeployApi,
                 '/api/deploys',
                 '/api/deploys/<string:id>',
                 '/api/deploys/<string:id>/<string:action>')