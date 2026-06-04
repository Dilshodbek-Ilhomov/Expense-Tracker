from django.urls import path
from analytics_app.views import AnalyticsAPIView

from .views import (
    TransactionListCreateAPIView,
)

urlpatterns = [
    path(
        "",
        TransactionListCreateAPIView.as_view(),
        name="transactions"
    ),

    path(
        "analytics/",
        AnalyticsAPIView.as_view(),
        name="analytics"
    ),
]