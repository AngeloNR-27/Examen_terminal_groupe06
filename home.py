import web
import navH
from DB import Db
web.config.debug = True

urls = (
     '/home', 'home',
     '/', 'index'
    
)

class home:
    def GET(self):
        db=Db().getDb()
        album06=db.select('Album', limit=10) 
        artists=db.select('Artist', limit=10)
        genres=db.select('Genre',limit=10)
        tracks=db.select('Track',limit=10)
        media_types=db.select('MediaType',limit=10)
        playlists=db.select('Playlist',limit=10)


        """ajout du fichier style.css"""
        result = '<html><head><title>Server.py G06</title></head>'

        result = '<html><head><title>test</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">'
        result += '<link rel="stylesheet" href="style.css">'

        result += '</head>'

        result += '<body>'
        result += navH.nav()
        

        result += '<body>'
        """for a in a2:
         result += a.Title + ',(' + str(a.ArtistId) + ') <br/>' """

        
        """ for a in a2:
            result += a.Title + ',(' + str(a.ArtistId) + ') <br/>' """

        result += '</body></html>'
        return result

        

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


