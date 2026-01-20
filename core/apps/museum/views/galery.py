from rest_framework import viewsets
from core.apps.museum.models import Gallery
from core.apps.museum.serializers import GallerySerializer
from rest_framework.response import Response


class GalleryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

    def list(self, request, *args, **kwargs):
        image_limit = request.query_params.get('image_limit', None)

        if image_limit is not None:
            try:
                image_limit = int(image_limit)
                if image_limit <= 0:
                    return Response({'error': 'Invalid number specified'}, status=400)
            except ValueError:
                return Response({'error': 'Image limit must be an integer'}, status=400)

            # Retrieve galleries with prefetch_related for images
            galleries = self.queryset.prefetch_related('image')
            result = []
            for gallery in galleries:
                total_image_count = gallery.image.count()
                images = gallery.image.all()[:image_limit]
                image_data = [image.image.url for image in images]

                result.append({
                    'gallery_id': gallery.id,
                    'total_image_count': total_image_count,
                    'count': len(images),
                    'images': image_data
                })

            return Response(result)

        # Default behavior when no image_limit is provided
        galleries = self.queryset.prefetch_related('image')
        result = []
        for gallery in galleries:
            total_image_count = gallery.image.count()
            result.append({
                'gallery_id': gallery.id,
                'total_image_count': total_image_count,
                'image': [image.image.url for image in gallery.image.all()]
            })

        return Response(result)