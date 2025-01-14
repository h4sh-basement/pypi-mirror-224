from .module_imports import *


@headers({"Ocp-Apim-Subscription-Key": key})
class Subscriptions(Consumer):
    """Inteface to Subscriptions resource for the RockyRoad API."""

    def __init__(self, Resource, *args, **kw):
        self._base_url = Resource._base_url
        super().__init__(base_url=Resource._base_url, *args, **kw)

    def categories(self):
        return self.Categories(self)

    def users(self):
        return self.Users(self)

    @returns.json
    @http_get("subscriptions")
    def list(
        self,
        category_1: Query(type=str) = None,
        category_2: Query(type=str) = None,
        category_3: Query(type=str) = None,
        category_4: Query(type=str) = None,
        category_5: Query(type=str) = None,
        medium: Query(type=str) = None,
    ):
        """This call will return a list of user subscriptions."""

    @headers({"Ocp-Apim-Subscription-Key": key})
    class Categories(Consumer):
        """Inteface to Subscription Categories resource for the RockyRoad API."""

        def __init__(self, Resource, *args, **kw):
            self._base_url = Resource._base_url
            super().__init__(base_url=Resource._base_url, *args, **kw)

        @returns.json
        @http_get("subscriptions/categories")
        def list(
            self,
            category_1: Query(type=str) = None,
            category_2: Query(type=str) = None,
            category_3: Query(type=str) = None,
            category_4: Query(type=str) = None,
            category_5: Query(type=str) = None,
            email: Query(type=bool) = None,
            sms: Query(type=bool) = None,
        ):
            """This call will return a list of subscription categories."""

        @delete("subscriptions/categories/{uid}")
        def delete(self, uid: str):
            """This call will delete the subscription category for the specified uid."""

        @returns.json
        @json
        @post("subscriptions/categories")
        def insert(self, subscription_category: Body):
            """This call will create the subscription category with the specified parameters."""

        @json
        @patch("subscriptions/categories/{uid}")
        def update(self, uid: str, subscription_category: Body):
            """This call will update the subscription category with the specified parameters."""

    @headers({"Ocp-Apim-Subscription-Key": key})
    class Users(Consumer):
        """Inteface to Subscription Users resource for the RockyRoad API."""

        def __init__(self, Resource, *args, **kw):
            self._base_url = Resource._base_url
            super().__init__(base_url=Resource._base_url, *args, **kw)

        @returns.json
        @http_get("subscriptions/users")
        def list_subscribed_users(
            self,
            category_1: Query(type=str) = None,
            category_2: Query(type=str) = None,
            category_3: Query(type=str) = None,
            category_4: Query(type=str) = None,
            category_5: Query(type=str) = None,
            medium: Query(type=str) = None,
        ):
            """This call will return a list of subscribed users for the specified criteria."""

        @returns.json
        @http_get("subscriptions/users/{uid}")
        def list_subscriptions_for_user(
            self,
            uid: str,
            category_1: Query(type=str) = None,
            category_2: Query(type=str) = None,
            category_3: Query(type=str) = None,
            category_4: Query(type=str) = None,
            category_5: Query(type=str) = None,
            medium: Query(type=str) = None,
        ):
            """This call will return a list of subscriptions for the specified user.."""

        @post(
            "subscriptions/categories/{subscription_category_uid}/users/{user_uid}/mediums/{medium}"
        )
        def insert(self, subscription_category_uid: str, user_uid: str, medium: str):
            """This call will create the user subscription with the specified parameters."""

        @delete(
            "subscriptions/categories/{subscription_category_uid}/users/{user_uid}/mediums/{medium}"
        )
        def delete(self, subscription_category_uid: str, user_uid: str, medium: str):
            """This call will delete the user subscription for the specified uid."""
