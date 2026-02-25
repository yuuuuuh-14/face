import pytest
import json

def test_health_endpoint(client):
    """Test the health check endpoint"""
    response = client.get('/system/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'ok'
    assert 'camera_connected' in data

def test_face_list_empty(client, clean_storage):
    """Test getting face list when empty"""
    response = client.get('/face/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['names'] == []

def test_logs_endpoint(client, clean_storage):
    """Test the access logs endpoint"""
    # Log something first
    clean_storage.log_access("TestUser", "REAL")
    
    response = client.get('/logs/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data['logs']) == 1
    assert data['logs'][0]['name'] == "TestUser"

def test_swagger_json(client):
    """Test if swagger.json is generated"""
    response = client.get('/swagger.json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'swagger' in data or 'openapi' in data
    assert 'BCC Biometric API' in data['info']['title']
