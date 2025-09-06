class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = [
            'id', 'date_joined', 'is_staff', 'is_superuser', 'is_acitive'
        ]