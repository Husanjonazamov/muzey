from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.apps.museum import views

router = DefaultRouter()
router.register(r'news', views.NewsViewSet, basename='news')
router.register(r'news-types', views.NewsTypeViewSet, basename='news-type')
router.register(r'galleries', views.GalleryViewSet, basename='gallery')
router.register(r'exhibits', views.ExhibitViewSet, basename='exhibit')
router.register(r'exhibit-types', views.ExhibitTypeViewSet, basename='exhibit-type')
router.register(r'museum-history', views.MuseumHistoryViewSet)
router.register(r'images', views.ImageViewSet)
router.register(r'working-times', views.WorkingTimeViewSet)

# router.register(r'events', views.EventsViewSet, basename='events')
router.register(r'event-types', views.EventTypeViewSet, basename='event-type')
router.register(r'management', views.ManagementViewSet, basename='management')
# router.register(r'supporters', views.SupportersView, basename='supporters')
router.register(r'about', views.AboutReadOnlyViewSet, basename='about')
router.register(r'location', views.LocationReadOnlyViewSet, basename='location')
router.register(r'address', views.AddressReadOnlyViewSet,  basename='address')
router.register(r'symbols', views.SymbolViewSet, basename='symbol')
router.register(r'videogallery', views.VideoGalleryViewSet, basename='videogallery')
router.register(r'products', views.ProductViewSet, basename='product')
router.register(r'useful-contents', views.UsefulContentViewSet)
router.register(r'price-sections', views.PriceSectionListView,  basename='price-sections')
router.register(r'price-text', views.PriceTextView,  basename='price-text')
router.register(r'social-media', views.SocialMediaViewSet, basename='socialmedia')

urlpatterns = [
    path('', include(router.urls)),
    path('connect/', views.ConnectCreateView.as_view(), name='connect-create'),
    path('events/', views.EventsListView.as_view(), name='events'),
    path('events/<int:id>/', views.EventDetailView.as_view(), name='event-detail'),
    path('search/', views.UnifiedSearchView.as_view(), name='unified-search'),
    path('random-exhibits/', views.RandomExhibitView.as_view(), name='random-exhibits'),
    path('supporters/', views.SupportersListView.as_view(), name='supporters-list'),
    path('supporters/<int:pk>/', views.SupportersDetailView.as_view(), name='supporters-detail'),
]
