from odoo import http
from odoo.http import request
from typing import Any


class TodoApp(http.Controller):
    @http.route(route="/owl/todo-app/", website=True, auth="public")
    def view_todo_app(self, **kwargs: dict) -> Any:
        return request.render("owl_todo_app.view_owl_todo_app_template", {})
