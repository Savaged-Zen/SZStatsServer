<%def name="javascript()"></%def>
<%def name="onload()"></%def>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>SZStats</title>
        <link rel="stylesheet" type="text/css" href="/static/css/core.css" />
        <script type="text/javascript" src="http://www.google.com/jsapi"></script>
        <script type="text/javascript">
            ${self.javascript()}
            google.setOnLoadCallback(function(){
                ${self.onload()}
            });
        </script>
    </head>
    <body>
        <nav><a href="/">Home</a><a href="/map">Installations by Country</a></nav>
        ${next.body()}
    </body>
</html>
