var { spawn } = require('child_process');

//py = spawn('python', ['./utils/tfs.py'])
const py = spawn('python3', ['./utils/test.py']);
var data = [1,2,3,4,5,6,7,8,9]
var dataString = ''

py.stdout.on('data', function(data){
    dataString += data.toString()
})

py.stdout.on('close', function(){
    console.log('Sum of numbers=', dataString);
});

py.stdin.write(JSON.stringify(data));
py.stdin.end();

//This functions kill the process (SHOULD BE USED)
setTimeout(() => {
    py.kill();
}, 2000);