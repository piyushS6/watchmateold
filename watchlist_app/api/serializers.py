from rest_framework import serializers
from watchlist_app.models import Watchlist, StreamPlatform, Review

# Model Serializer

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        exclude = ['watchlist']
        # fields = '__all__'

class WatchlistSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Watchlist
        fields = '__all__'
        # fields = ['id', 'name']
        # exclude = ['active']
        
    # def get_len_name(self, object):
    #     return len(object.name)

    # # field level validation
    # def validate_name(self, value):
        
    #     if len(value)<2:
    #         raise serializers.ValidationError('Name is too short!')
    #     else:
    #          return value
         
         
    # # object level validation
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError('Name and Description should be different!')
    #     else:
    #         return data

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchlistSerializer(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie-detail'
    # )
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'


# Serializer

# def length_of_name(value):
#     if len(value)<2:
#             raise serializers.ValidationError('Name is too short!')
#     else:
#             return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[length_of_name])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
    
#     # field level validation
#     def validate_name(self, value):
        
#         if len(value)<2:
#             raise serializers.ValidationError('Name is too short!')
#         else:
#              return value
         
         
#     # object level validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Name and Description should be different!')
#         else:
#             return data