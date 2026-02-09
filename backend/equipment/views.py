from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import pandas as pd
from .models import EquipmentDataset
from .serializers import EquipmentDatasetSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_csv(request):
    if 'file' not in request.FILES:
        return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
    
    file = request.FILES['file']
    
    if not file.name.endswith('.csv'):
        return Response({'error': 'Only CSV files allowed'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        df = pd.read_csv(file)
        
        required_columns = ['Equipment Name', 'Type', 'Flowrate', 'Pressure', 'Temperature']
        if not all(col in df.columns for col in required_columns):
            return Response({'error': f'CSV must contain: {", ".join(required_columns)}'}, 
                          status=status.HTTP_400_BAD_REQUEST)
        
        df = df.dropna()
        
        total_records = len(df)
        avg_flowrate = float(df['Flowrate'].mean())
        avg_pressure = float(df['Pressure'].mean())
        avg_temperature = float(df['Temperature'].mean())
        type_distribution = df['Type'].value_counts().to_dict()
        
        dataset = EquipmentDataset.objects.create(
            original_filename=file.name,
            total_records=total_records,
            avg_flowrate=avg_flowrate,
            avg_pressure=avg_pressure,
            avg_temperature=avg_temperature,
            type_distribution=type_distribution,
            user=request.user
        )
        
        serializer = EquipmentDatasetSerializer(dataset)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_latest_summary(request):
    dataset = EquipmentDataset.objects.filter(user=request.user).first()
    if not dataset:
        return Response({'error': 'No datasets available'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EquipmentDatasetSerializer(dataset)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_history(request):
    datasets = EquipmentDataset.objects.filter(user=request.user)
    serializer = EquipmentDatasetSerializer(datasets, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_dataset_detail(request, pk):
    try:
        dataset = EquipmentDataset.objects.get(pk=pk)
        serializer = EquipmentDatasetSerializer(dataset)
        return Response(serializer.data)
    except EquipmentDataset.DoesNotExist:
        return Response({'error': 'Dataset not found'}, status=status.HTTP_404_NOT_FOUND)
