from .module_imports import *


@headers({"Ocp-Apim-Subscription-Key": key})
class Oracle_Users(Consumer):
    """Inteface to Oracle users resource for the RockyRoad API."""

    def __init__(self, Resource, *args, **kw):
        self._base_url = Resource._base_url
        super().__init__(base_url=Resource._base_url, *args, **kw)

    @returns.json
    @http_get("oracle-users")
    def list(
        self,
        email: Query(type=str) = None,
        userName: Query(type=str) = None,
    ):
        """This call will return Oracle user information for the specified criteria."""

    @returns.json
    @http_get("oracle-users/{email}")
    def get(
        self,
        email: str,
    ):
        """This call will return the Oracle user for the specified email."""

    @returns.json
    @json
    @post("oracle-users")
    def insert(
        self,
        oracle_user: Body,
    ):
        """This call will insert a new Oracle user."""

    @returns.json
    @json
    @patch("oracle-users/batch")
    def batch_update(
        self,
        oracle_user_batch: Body,
    ):
        """This call will update a batch of Oracle users."""

    @json
    @patch("oracle-users/{email}")
    def update(
        self,
        email: str,
        oracle_user: Body,
    ):
        """This call will update a Oracle user."""

    @json
    @delete("oracle-users/{email}")
    def delete(
        self,
        email: str,
    ):
        """This call will delete a Oracle user."""
