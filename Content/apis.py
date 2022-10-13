from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import BlogSerializer
from .models import Blog
class BlogList(APIView):
    def get(self,request):
        qs=Blog.objects.all()


        return Response(BlogSerializer(qs, many=True, context={'request': request}).data)


class BlogView(APIView):
    def get(self,request,pk):
        qs = Blog.objects.get(id=pk)

        return Response(BlogSerializer(qs, many=False, context={'request': request}).data)
class SearchBlog(APIView):
    def get(self,request):
        searchkey = request.GET.get('q')

        qs =Blog.objects.filter(title__contains=searchkey)
        if not qs:
            context=[
                {
                    "title":"No blog Found"
                }
            ]
            return Response(context)
        serializer=BlogSerializer(qs, many=True, context={'request': request}).data

        return Response(serializer)