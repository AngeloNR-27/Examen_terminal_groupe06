def nav():
    result = '<nav class="navbar navbar-expand-lg  bg-light"style="width: 100%;">'
    result += '<div class="container-fluid">'
    result += '<ul class="navbar-nav">'
    result += '<li class="nav-item"><a class="nav-link text-dark" href="/">Menu</a></li>'
    result += '<li class="nav-item"><a class="nav-link text-dark" href="/main">Main</a></li>'
    result += '<li class="nav-item"><a class="nav-link text-dark" href="/genre">Genre</a></li>'
    result += '<li class="nav-item"><a class="nav-link text-dark" href="/artist">Artists</a></li>'
    result += '<li class="nav-item"><a class="nav-link text-dark" href="/album">Album</a></li>'
    result += '<li class="nav-item"><a class="nav-link text-dark" href="/track">Track</a></li>'
    result += '<li class="nav-item"><a class="nav-link text-dark" href="/media">Media type</a></li>'
    result += '<li class="nav-item"><a class="nav-link text-dark" href="/playlist">Playlist</a></li>'
    result += '</ul>'
    result += '</div>'
    result += '</nav>'
    return result