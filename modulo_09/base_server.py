from http.server import HTTPServer, BaseHTTPRequestHandler
from usuario import Usuario
import hashlib


def hash_string(texto):
    return hashlib.sha256(texto.encode()).hexdigest() 

u1 = Usuario("Alice", "alice@codar.me", hash_string("123"))
u2 = Usuario("Luíza", "luiza@codar.me", hash_string("465"))
u3 = Usuario("Marcos", "marcos@codar.me", hash_string("777"))
u4 = Usuario("Carla", "carla@codar.me", hash_string("485"))
u5 = Usuario("Milton", "milton@codar.me", hash_string("701"))

lista_usuario = [u1, u2, u3, u4, u5]

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/usuarios":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            
            stylesheet_html = """<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <style>
    .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
    }

    @media (min-width: 768px) {
        .bd-placeholder-img-lg {
        font-size: 3.5rem;
        }
    }
    
    body{font-size:.875rem}.feather{width:16px;height:16px;vertical-align:text-bottom}.sidebar{position:fixed;top:0;bottom:0;left:0;z-index:100;padding:48px 0 0;box-shadow:inset -1px 0 0 rgba(0,0,0,.1)}@media (max-width:767.98px){.sidebar{top:5rem}}.sidebar-sticky{position:relative;top:0;height:calc(100vh - 48px);padding-top:.5rem;overflow-x:hidden;overflow-y:auto}.sidebar .nav-link{font-weight:500;color:#333}.sidebar .nav-link .feather{margin-right:4px;color:#727272}.sidebar .nav-link.active{color:#2470dc}.sidebar .nav-link.active .feather,.sidebar .nav-link:hover .feather{color:inherit}.sidebar-heading{font-size:.75rem;text-transform:uppercase}.navbar-brand{padding-top:.75rem;padding-bottom:.75rem;font-size:1rem;background-color:rgba(0,0,0,.25);box-shadow:inset -1px 0 0 rgba(0,0,0,.25)}.navbar .navbar-toggler{top:.25rem;right:1rem}.navbar .form-control{padding:.75rem 1rem;border-width:0;border-radius:0}.form-control-dark{color:#fff;background-color:rgba(255,255,255,.1);border-color:rgba(255,255,255,.1)}.form-control-dark:focus{border-color:transparent;box-shadow:0 0 0 3px rgba(255,255,255,.25)}
    </style>"""
            
            usuario_html = ""

            for c in lista_usuario:
                usuario_html += f"""<tr>
                            <td>{c.id}</td>
                            <td>{c.nome}</td>
                            <td>{c.email}</td>
                            <td>{c.senha}</td>
                        </tr>"""
            
            data = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <title>Usuários</title>
    {stylesheet_html}
  </head>
  <body>
    <header class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow">
    <a class="navbar-brand col-md-3 col-lg-2 me-0 px-3" href="#">Company name</a>
    <button class="navbar-toggler position-absolute d-md-none collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#sidebarMenu" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <input class="form-control form-control-dark w-100" type="text" placeholder="Search" aria-label="Search">
    <div class="navbar-nav">
        <div class="nav-item text-nowrap">
        <a class="nav-link px-3" href="#">Sign out</a>
        </div>
    </div>
    </header>
    <div class="container-fluid">
        <div class="row">
            <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
                <div class="position-sticky pt-3">
                    <ul class="nav flex-column">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">
                        <span data-feather="home"></span>
                        Dashboard
                        </a>
                    </li>
                    </ul>
                </div>
            </nav>
            <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
                <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
                    <h1 class="h2">Dashboard</h1>
                    <div class="btn-toolbar mb-2 mb-md-0">
                    <div class="btn-group me-2">
                        <button type="button" class="btn btn-sm btn-outline-secondary">Share</button>
                        <button type="button" class="btn btn-sm btn-outline-secondary">Export</button>
                    </div>
                    <button type="button" class="btn btn-sm btn-outline-secondary dropdown-toggle">
                        <span data-feather="calendar"></span>
                        This week
                    </button>
                    </div>
                </div>
                <h2>Usuários</h2>
                <div class="table-responsive">
                    <table class="table table-striped table-sm">
                        <thead>
                            <tr>
                                <th scope="col">Id</th>
                                <th scope="col">Nome</th>
                                <th scope="col">Email</th>
                                <th scope="col">Senha</th>
                            </tr>
                        </thead>
                        <tbody>
                            {usuario_html}
                        </tbody>
                    </table>
                </div>
            </main>
        </div>
    </div>
    </body>
</html>""".encode()

            return self.wfile.write(data)

server = HTTPServer(('localhost', 8000), SimpleHandler)
server.serve_forever()
