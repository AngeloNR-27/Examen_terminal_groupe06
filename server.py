import web
from DB import Db
web.config.debug = True

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        db=Db().getDb()
        album06=db.select('Album', limit=10) 
        artists=db.select('Artist', limit=10)
        genres=db.select('Genre',limit=10)
        tracks=db.select('Track',limit=10)
        media_types=db.select('MediaType',limit=10)
        playlists=db.select('Playlist',limit=10)
        result = '<html><head><title>test</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">'
        result += '<style>'
        result += 'body {'
        result += 'background-image: url(https://cdn.pixabay.com/photo/2015/12/27/05/48/turntable-1109588_960_720.jpg);'
        result += 'background-size: cover;'
        result += '}'
        result += '#h1 {'
        result += 'margin-top: 315px;'
        result += 'font-size: 70px;'
        result += 'color: #000;'
        result += '}'
        result += '</style>'
        result += '</head>'
        result += '<body>'
        result += '<nav class="navbar navbar-expand-lg navbar-light bg-light">'
        result += '<div class="container-fluid d-flex justify-content-center">'
        result += '<ul class="navbar-nav">'
        result += '<li class="nav-item dropdown">'
        result += '<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Menu</a>'
        result += '<ul class="dropdown-menu" aria-labelledby="navbarDropdown">'
        result += '<li><a class="dropdown-item" href="/home">Home</a></li>'
        result += '<li><a class="dropdown-item" href="/main">Main</a></li>'
        result += '</ul>'
        result += '</li>'
        result += '</ul>'
        result += '</div>'
        result += '</nav>'
        result += '<div class="container">'
        result += '<h1 class="text-center" id="h1">Bienvenue dans The Music</h1>'
        # for a in a2:
        #     result += '<p>' + a.Title + ',(' + str(a.ArtistId) + ')</p>'
        result += '</div>'
        result += '<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>'
        result += '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>'
        result += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>'
        result += '</body></html>'


        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
