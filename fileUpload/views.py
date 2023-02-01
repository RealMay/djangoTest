import json

from django.http import FileResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from fileUpload import models, serializer
import xlrd
from rest_framework import permissions


class FileViewSet(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    queryset = models.FilesModel.objects.all()
    serializer_class = serializer.FilesSerializer

    """下载文件"""

    @action(methods=['get', 'post'], detail=True)
    def download(self, request, pk=None, *args, **kwargs):
        file_obj = self.get_object()
        print(file_obj.file)
        print("====")
        print(file_obj.file.path)
        response = FileResponse(open(file_obj.file.path, 'rb'))
        return response

    """获取保存的文件的数据"""

    @action(methods=['get', 'post'], detail=True)
    def file_list(self, request, pk=None, *args, **kwargs):
        file_obj = self.get_object()
        file = file_obj.file
        work_book = xlrd.open_workbook(str(file))
        # 拿到第一张表
        table = work_book.sheets()[0]

        # 将excel转换为json   undo:抽离出来成utls
        rows = table.nrows
        keys = []
        result = []

        for i in range(rows):
            if i == 0:
                keys = table.row_values(i)
                print(keys)
                print("keys")
            else:
                record = {}
                cnt = 0
                for item in table.row_values(i):
                    record[keys[cnt]] = item
                    cnt += 1
                result.append(record)
                print(result)
                json.dump(result, ensure_ascii=False)
                print("res")

        return Response(result)
