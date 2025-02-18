from rest_framework.views import APIView
from rest_framework.response import Response



class HelloApiView(APIView):
    """Test API view"""


    def get(self, request, format=None):
        """returns a list of api view fitures"""

        an_apiview = [
            'Uses Http methods as functions(post, get, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
