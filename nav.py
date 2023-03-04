def nav():
    result = '<nav class="navbar navbar-expand-sm  bg-dark"style="width: 100%;">'
    result += '<div class="container-fluid">'
    result += '<ul class="navbar-nav">'
    result += '<li class="nav-item"><a class="nav-link text-light" href="/">Home</a></li>'
    result += '<li class="nav-item"><a class="nav-link text-light" href="/genre">Genre</a></li>'
    result += '<li class="nav-item"><a class="nav-link text-light" href="/artist">Artists</a></li>'
    result += '<li class="nav-item"><a class="nav-link text-light" href="/album">Album</a></li>'
    result += '<li class="nav-item"><a class="nav-link text-light" href="/track">Track</a></li>'
    result += '<li class="nav-item"><a class="nav-link text-light" href="/media">Media type</a></li>'
    result += '<li class="nav-item"><a class="nav-link text-light" href="/playlist">Playlist</a></li>'
    result += '</ul>'
    result += '</div>'
    result += '</nav>'
    return result