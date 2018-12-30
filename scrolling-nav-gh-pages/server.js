var http = require('http');
var fs = require('fs');
var url = require('url');
const ps = require('python-shell');

var app = http.createServer(function(request,response){
	var _url = request.url;
	var queryData = url.parse(_url, true).query;

	var options = {
		mode : 'text',
		pythonPath : '',
		pythonOptions : ['-u'],
		scriptPath : '',
		args: [queryData.ATOPchampion]
	};
console.log(options.args);
	/*
		/?ATOPchampion=Aatrox&AJUNGLEchampion=Barum
		&AMIDchampion=Camille&AADCARRYchampion=Cassiopeia
		&ASUPPORTchampion=Corki&ETOPchampion=Alistar
		&EJUNGLEchampion=Caitlyn&EMIDchampion=Camille
		&EADCARRYchampion=Cassiopeia&ESUPPORTchampion=ChoGath
	*/

	ps.PythonShell.run('test.py',options,function(err,results){
		//console.log("1\n");
		if(err) throw err;
		console.log('results: %j',results);
	});

	if(_url == '/'){
		_url = '/index.html';
	}
	if(_url == '/favicon.ico'){
		return response.writeHead(404);
	}
	response.writeHead(200);
	response.end(fs.readFileSync(__dirname+_url));
});
app.listen(3000);
