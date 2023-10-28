import requests 

# Remplacez par l'URL de votre API 
api_base_url = "http://127.0.0.1:8000/" 
 
# def main(): 
# print("Bienvenue dans le script de récupération de données.") 

# It allows you to retrieve the artist ID then displays the corresponding name

def search_artist_by_name(): 
    artist_name = input("Entrez le nom de l'artiste : ")
    response = requests.get(api_base_url + "artists/?artist_name="+ artist_name) 
        
    if response.status_code == 200: 
        artists = response.json() 
        print("Résultat de la recherche :\n") 
        
        for artist in artists:
            print(f"\nID de l'artiste: {artist['artistId']}, Nom: {artist['name']}") 

    else: 
        print("Aucun résultat trouvé.") 

#It allows you to retrieve an artist name, it displays artists who have the same name

def get_albums_by_artist_id(): 
    artist_id = input("Entrez l'identifiant de l'artiste : ") 
    response = requests.get(api_base_url + "albums/?artist_id="+ artist_id)

    if response.status_code == 200:
      albums = response.json() 
      print ("Albums correspondants :") 
    
      for album in albums: 
            print(f"ID de l'album: {album['albumId']},Titre: {album['title']}") 

    else: 
     print("Aucun résultat trouvé.") 

#It asks for the ID of an album and displays the titles corresponding to the album
#I followed the synthase to create the routes and get which allows me to find the names to access the routes.

def get_tracks_by_album_id():
    album_id = input("Entrez l'identifiant de l'album : ") 
    response = requests.get(api_base_url +"tracks/?album_id="+ album_id)
    
    if response.status_code == 200:
        tracks = response.json() 
        print("Pistes correspondantes :") 
    
        for track in tracks: 
             print(f"ID de la piste: {track['trackId']}, Titre: {track['name']}") 
    
    else:
     print("Aucun résultat trouvé.") 
while True:
    print("\n1. Rechercher des artistes par nom") 
    print("2. Obtenir des albums par identifiant d'artiste") 
    print("3. Obtenir des pistes par identifiant d'album")
    print("0. Quitter\n") 
    choice = input("\nChoisissez une option : ") 
    
    if choice == "1": 
        search_artist_by_name() 

    elif choice == "2": 
        get_albums_by_artist_id() 

    elif choice == "3": 
        get_tracks_by_album_id() 

    elif choice == "0": 
        break 

    else:
        print("Option invalide. Réessayez.") 
    