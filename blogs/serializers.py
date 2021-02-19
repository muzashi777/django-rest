from rest_framework import serializers
from blogs.models import Article, Article_Image, Article_Content


class ArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article_Image
        fields = ["url"]


class ArticleContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article_Content
        fields = ["content"]


class ArticleSerializer(serializers.ModelSerializer):

    # urls = ArticleImageSerializer(many=True)
    # urls = serializers.StringRelatedField(many=True)
    img = serializers.SerializerMethodField('get_img')
    title_img = serializers.SerializerMethodField('get_title_img')
    desc = serializers.SerializerMethodField('get_content')

    def get_img(self, articleID):
        qs = Article_Image.objects.filter(topic=False, articleID=articleID)
        imageData = ArticleImageSerializer(instance=qs, many=True)
        my_list = []
        for x in imageData.data:
            my_list.append(x["url"])
        return my_list

    def get_title_img(self, articleID):
        qs = Article_Image.objects.filter(topic=True, articleID=articleID)
        imageData = ArticleImageSerializer(instance=qs, many=True)
        my_list = []
        for x in imageData.data:
            my_list.append(x["url"])

        if len(my_list) > 0:
            return my_list[0]
        else:
            return ""

    def get_content(self, articleID):
        qs = Article_Content.objects.filter(isShow=True, articleID=articleID)
        imageData = ArticleContentSerializer(instance=qs, many=True)
        my_list = []
        for x in imageData.data:
            my_list.append(x["content"])
        if len(my_list) > 0:
            return my_list[0]
        else:
            return ""

    class Meta:
        model = Article

        fields = ['id', 'title',  "desc", "title_img", "img", "createBy",
                  "updateAt", "typeID", 'isRecommend', ]
