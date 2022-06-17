const http = require('http');
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');

const app = express();

const ads = [
    {
        title: 'Hello, world (again)!'
    }
];

app.use(helmet());
app.use(bodyParser.json());
app.use(cors());
app.use(morgan('combined'));


app.get('/operate', (req, res) => {
    res.send(ads)
});

app.listen(1337, () => {
    console.log('Listening on port 1337')
})