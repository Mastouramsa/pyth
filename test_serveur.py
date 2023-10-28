import requests
api_base_url = "http://127.0.0.1:8000/" 

def test_Album():
    query = requests.get(api_base_url + "albums/?artist_id=3")

    assert query.status_code == 200
    assert query.json() == [{"albumId":5,"title":"Big Ones","artistId":3}]


def test_artist():
    query = requests.get(api_base_url + "artists/?artist_name=Kiss")

    assert query.status_code == 200
    assert query.json() == [{"name":"Kiss","artistId":52}]

def test_tracks():
    query = requests.get(api_base_url + "tracks/?album_id=10")

    assert query.status_code == 200
    assert query.json() == [{"unitPrice":0.99,"trackId":85,"name":"Cochise","milliseconds":222380,"albumId":10},{"unitPrice":0.99,"trackId":86,"name":"Show Me How to Live","milliseconds":277890,"albumId":10},{"unitPrice":0.99,"trackId":87,"name":"Gasoline","milliseconds":279457,"albumId":10},{"unitPrice":0.99,"trackId":88,"name":"What You Are","milliseconds":249391,"albumId":10},{"unitPrice":0.99,"trackId":89,"name":"Like a Stone","milliseconds":294034,"albumId":10},{"unitPrice":0.99,"trackId":90,"name":"Set It Off","milliseconds":263262,"albumId":10},{"unitPrice":0.99,"trackId":91,"name":"Shadow on the Sun","milliseconds":343457,"albumId":10},{"unitPrice":0.99,"trackId":92,"name":"I am the Highway","milliseconds":334942,"albumId":10},{"unitPrice":0.99,"trackId":93,"name":"Exploder","milliseconds":206053,"albumId":10},{"unitPrice":0.99,"trackId":94,"name":"Hypnotize","milliseconds":206628,"albumId":10},{"unitPrice":0.99,"trackId":95,"name":"Bring'em Back Alive","milliseconds":329534,"albumId":10},{"unitPrice":0.99,"trackId":96,"name":"Light My Way","milliseconds":303595,"albumId":10},{"unitPrice":0.99,"trackId":97,"name":"Getaway Car","milliseconds":299598,"albumId":10},{"unitPrice":0.99,"trackId":98,"name":"The Last Remaining Light","milliseconds":317492,"albumId":10}]