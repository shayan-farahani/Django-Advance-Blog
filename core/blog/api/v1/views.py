
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly
)
from .serializers import PostSerializers, CategorySerializers
from ...models import Post, Category

from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .paginations import DefaultPagination


# from rest_framework.generics import (
#     ListCreateAPIView,
#     RetrieveUpdateDestroyAPIView,
# )
# api with function base
"""@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.filter(status=True)
        serializers = PostSerializers(posts, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = PostSerializers(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)"""


"""@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id, status=True)
    if request.method == 'GET':
        serializers = PostSerializers(post)
        return Response(serializers.data)
    elif request.method == 'PUT':
        serializers = PostSerializers(post, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response({'detail':'item removed successfully'}, status=status.HTTP_204_NO_CONTENT)"""


# api with APIView

"""class PostList(APIView):
    ''' getting a list of posts and creating posts '''

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializers
    def get(self, request):
        '''retrieving a list of posts'''
        posts = Post.objects.filter(status=True)
        serializers = PostSerializers(posts, many=True)
        return Response(serializers.data)
    def post(self, request):
        '''creating a post with provided'''
        serializers = PostSerializers(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
"""

"""class PostDetail(APIView):
    '''getting detail a post and editing plus removing it'''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializers

    def get(self, request, id):
        ''' retrieving the post data '''
        post = get_object_or_404(Post, pk=id, status=True)
        serializers = self.serializer_class(post)
        return Response(serializers.data)
    
    def put(self, request, id):
        ''' editing the post data '''
        post = get_object_or_404(Post, pk=id, status=True)
        serializers = self.serializer_class(post, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
    
    def delete(self, request, id):
        ''' deleting the post object '''
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({'detail':'item removed successfully'}, status=status.HTTP_204_NO_CONTENT)"""

"""
class PostList(ListCreateAPIView):
    ''' getting a list of posts and creating posts '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializers


class PostDetail(RetrieveUpdateDestroyAPIView):
    '''getting detail a post and editing plus removing it'''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializers
    queryset = Post.objects.filter(status=True)

        """
# view set


class PostViewSet(viewsets.ModelViewSet):
    """getting a list of posts and creating posts"""

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializers
    queryset = Post.objects.filter(status=True)
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = {
        "category": ["exact", "in"],
        "author": ["exact"],
        "status": ["exact"],
    }
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = DefaultPagination


class CategoryViewSet(viewsets.ModelViewSet):
    """getting a list of posts and creating posts"""

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
