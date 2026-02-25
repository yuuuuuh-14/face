import numpy as np

def test_db_init(clean_storage):
    """Test if database initialized correctly"""
    assert clean_storage.get_name_list() == []

def test_save_and_get_face(clean_storage):
    """Test saving and retrieving a face embedding"""
    name = "Test User"
    embedding = np.random.rand(512)
    
    success = clean_storage.save_face(name, embedding)
    assert success is True
    
    names = clean_storage.get_name_list()
    assert name in names
    
    faces = clean_storage.get_all_faces()
    assert faces[0]['name'] == name
    assert len(faces[0]['embedding']) == 512

def test_delete_face(clean_storage):
    """Test face deletion"""
    name = "To Be Deleted"
    clean_storage.save_face(name, np.zeros(512))
    
    assert name in clean_storage.get_name_list()
    
    success = clean_storage.delete_face(name)
    assert success is True
    assert name not in clean_storage.get_name_list()

def test_access_logs(clean_storage):
    """Test logging access history"""
    clean_storage.log_access("Guest", "REAL")
    logs = clean_storage.get_recent_logs()
    
    assert len(logs) == 1
    assert logs[0]['name'] == "Guest"
    assert logs[0]['liveness'] == "REAL"
