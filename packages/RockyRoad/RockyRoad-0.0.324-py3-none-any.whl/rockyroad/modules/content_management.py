from .module_imports import *


@headers({"Ocp-Apim-Subscription-Key": key})
class _Content_Management(Consumer):
    """Inteface to Content Management resource for the RockyRoad API."""

    def __init__(self, Resource, *args, **kw):
        self._base_url = Resource._base_url
        super().__init__(base_url=Resource._base_url, *args, **kw)

    def cms_pages(self):
        """Inteface to Cms_Page resource for the RockyRoad API."""
        return self._Cms_Pages(self)

    @headers({"Ocp-Apim-Subscription-Key": key})
    class _Cms_Pages(Consumer):
        """Inteface to Cms_Page resource for the RockyRoad API."""

        def __init__(self, Resource, *args, **kw):
            self._base_url = Resource._base_url
            super().__init__(base_url=Resource._base_url, *args, **kw)

        def cms_page_fields(self):
            """Inteface to Cms_Page_Field resource for the RockyRoad API."""
            return self._Cms_Page_Fields(self)

        @returns.json
        @http_get("content-management/pages")
        def list(
            self,
            page_type: Query(type=str) = None,
            title: Query(type=str) = None,
            subtitle: Query(type=str) = None,
            category_1: Query(type=str) = None,
            category_2: Query(type=str) = None,
            category_3: Query(type=str) = None,
            field: Query(type=str) = None,
            is_published: Query(type=bool) = None,
            is_searchable: Query(type=bool) = None,
            authAll: Query(type=bool) = None,
            authBti: Query(type=bool) = None,
            authCarlson: Query(type=bool) = None,
            authPeterson: Query(type=bool) = None,
            authRoadtec: Query(type=bool) = None,
            authBtiBreakerAttach: Query(type=bool) = None,
            authBtiSystems: Query(type=bool) = None,
            authBtiMining: Query(type=bool) = None,
            authKpiJciAmsFullLine: Query(type=bool) = None,
            authKpiJciAmsNonTrack: Query(type=bool) = None,
            authKpiJciAmsTrack: Query(type=bool) = None,
            authTelsmith: Query(type=bool) = None,
            authConeco: Query(type=bool) = None,
            authHeatec: Query(type=bool) = None,
            authPreview: Query(type=bool) = None,
            limit: Query(type=int) = None,
        ):
            """This call will return list of Cms_Page_Objects."""

        @returns.json
        @http_get("content-management/pages/{uid}")
        def get(self, uid: str):
            """This call will get the Cms_Page_Object for the specified uid."""

        @delete("content-management/pages/{uid}")
        def delete(self, uid: str):
            """This call will delete the Cms_Page_Object for the specified uid."""

        @returns.json
        @json
        @post("content-management/pages")
        def insert(self, cms_page_object: Body):
            """This call will create the Cms_Page_Object with the specified parameters."""

        @json
        @patch("content-management/pages/{uid}")
        def update(self, uid: str, cms_page_object: Body):
            """This call will update the Cms_Page_Object with the specified parameters."""

        @headers({"Ocp-Apim-Subscription-Key": key})
        class _Cms_Page_Fields(Consumer):
            """Inteface to Cms_Page_Field resource for the RockyRoad API."""

            def __init__(self, Resource, *args, **kw):
                self._base_url = Resource._base_url
                super().__init__(base_url=Resource._base_url, *args, **kw)

            @returns.json
            @http_get("content-management/pages/{cms_page_uid}/fields")
            def list(self, cms_page_uid: str):
                """This call will return list of Cms_Page_Fields."""

            @returns.json
            @http_get("content-management/pages/fields/{uid}")
            def get(self, uid: str):
                """This call will return list of Cms_Page_Fields."""

            @delete("content-management/pages/fields/{uid}")
            def delete(self, uid: str):
                """This call will the Cms_Page_Field."""

            @returns.json
            @json
            @post("content-management/pages/{cms_page_uid}/fields")
            def insert(self, cms_page_uid: str, cms_page_field_object: Body):
                """This call will create the Cms_Page_Field."""

            @json
            @patch("content-management/pages/fields/{uid}")
            def update(self, uid: str, cms_page_field_object: Body):
                """This call will update the Cms_Page_Field."""
