from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name')
    
    class Meta:
        model = WatchList
        fields = "__all__"
        #field = ['id', 'name', 'description']
        #exlude = ['name'] -> gets all the fields excluding the name field 
    
    
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)


    class Meta:
        model = StreamPlatform
        fields = "__all__"

        
    
    # def get_len_name(self, object):
    #     return len(object.name)
   
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Names should be different from description")
    #     else:
    #         return data
    
    

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     else: 
    #         return value
    















# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short")


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length]) 
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#                     #old value   #new value 
#     def update(self, instance, validated_data):
#         #old value is uptaded with the new one and .get takes the name and instance.name(old name)
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     #object level validation , when we need more than one field which means the object
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Names should be different from description")
#         else:
#             return data
    
    
    # #field level validation ,  a specified field
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     else: 
    #         return value