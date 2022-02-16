#     Copyright 2021 Invana
#  #
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at
#  #
#      http:www.apache.org/licenses/LICENSE-2.0
#  #
#      Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#     http:www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Route
from invana_engine.server.views import homepage_view
# from ..gremlin import InvanaEngineClient
from invana_engine.settings import gremlin_server_url, shall_debug, \
    gremlin_traversal_source

print(".................................................")
print("Starting Invana Engine server")
print(f"Using GREMLIN_SERVER_URL: {gremlin_server_url}")
print(f"Using GREMLIN_TRAVERSAL_SOURCE: {gremlin_traversal_source}")
print(f"Using DEBUG: {shall_debug}")
print(".................................................")

if gremlin_server_url is None:
    print("ERROR: GREMLIN_SERVER_URL environment variable not set. Please fix it .")
    print("Exiting the program now. Please refer the documentation at https://github.com/invanalabs/invana-engine")
    exit()

routes = [
    Route('/', endpoint=homepage_view),
    # Route('/graphql', GraphQLApp(
    #     schema=Schema(query=GremlinQuery, mutation=GremlinMutation),
    # ))
]

middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'], allow_methods=["GET", "POST", "PUT", "DELETE"])
]

app = Starlette(routes=routes, middleware=middleware, debug=shall_debug)
