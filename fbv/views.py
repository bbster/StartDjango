from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from fbv.models import Song
from fbv.serializers import SongSerializer


@api_view(['GET', 'POST'])  # 데코레이터 반복적으로 사용해야 하는 함수를 데코레이터로 사용가능
def song_list(request):
    if request.method == 'GET':
        queryset = Song.objects.all().order_by('-id')  # order_by id값 기준으로 최근 게시물 상단
        serializer = SongSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def songs_detail(request, pk):
    try:
        song = Song.objects.get(pk=pk)  # Song의 pk값 song에 저장
    except Song.DoesNotExist:  # song pk값 못찾아올때 NOT FOUND 출력
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():  # 데이터 유효성 검사
            serializer.save()  # 데이터 DB에 저장
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
