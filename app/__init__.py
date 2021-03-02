from eve import Eve
from flask import request, abort

from app.hooks import pre_get_all, pre_post_all, pre_put_all, pre_patch_all, pre_delete_all
from app.services.mongodb_service import MongodbService
from app.services.token_service import TokenService


def create_app():
    app = Eve()

    MongodbService.global_init(app=app)

    @app.route('/authenticate', methods=['POST'])
    def post_authenticates_api_code():
        json_input = request.json
        user = MongodbService.find_one_by_resource(
            resource="users",
            lookup={"username": json_input["username"]}
        )

        if not user or user["password"] != json_input["password"]:
            abort(401, {"message": "Unauthorized access"})

        return TokenService.create_user_token(user=user)

    # Hooks
    app.on_pre_GET += pre_get_all
    app.on_pre_POST += pre_post_all
    app.on_pre_PUT += pre_put_all
    app.on_pre_PATCH += pre_patch_all
    app.on_pre_DELETE += pre_delete_all

    @app.before_first_request
    def before_first_request():
        user = MongodbService.find_one_by_resource(
            resource="users",
            lookup={
                "username": "visma"
            }
        )
        if not user:
            MongodbService.insert_one_by_resource(
                resource="users",
                data={
                    "username": "visma",
                    "password": "visma"
                }
            )

    @app.after_request
    def after_request(response):
        response.headers.set("Access-Control-Allow-Origin", "*")
        response.headers.set("Access-Control-Allow-Headers", "Cache-Control,Content-Type,Authorization,"
                                                             "token,If-Match")
        response.headers.set("Access-Control-Allow-Methods", "GET,PUT,POST,PATCH,DELETE")

        return response

    return app
