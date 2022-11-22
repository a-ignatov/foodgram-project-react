from rest_framework import mixins, viewsets


class ViewOnlyViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    pagination_class = None
